-- edu-arena Supabase 초기 설정
-- Supabase 대시보드 → SQL Editor → New query에 전체를 붙여 넣고 Run 하세요. 한 번만 실행하면 됩니다.

-- 1) 회원 동의 기록(만 14세 이상 확인, 약관·방침 동의 일시)
create table if not exists public.profiles (
  id uuid primary key references auth.users (id) on delete cascade,
  age14_confirmed boolean not null default false,
  agreed_at timestamptz,
  created_at timestamptz not null default now()
);

alter table public.profiles enable row level security;

-- 로그인한 회원만 이 테이블에 접근(어떤 행인지는 아래 RLS 정책이 본인 것으로 제한)
-- 프로젝트 생성 때 "Automatically expose new tables"를 꺼 두었으므로 직접 권한을 준다
revoke all on public.profiles from anon;
grant select, insert, update on public.profiles to authenticated;

-- 본인 행만 읽고 쓸 수 있음
drop policy if exists "profiles_select_own" on public.profiles;
create policy "profiles_select_own" on public.profiles
  for select using (auth.uid() = id);

drop policy if exists "profiles_insert_own" on public.profiles;
create policy "profiles_insert_own" on public.profiles
  for insert with check (auth.uid() = id);

drop policy if exists "profiles_update_own" on public.profiles;
create policy "profiles_update_own" on public.profiles
  for update using (auth.uid() = id) with check (auth.uid() = id);

-- 2) 회원 탈퇴: 로그인한 본인 계정만 삭제(동의 기록도 함께 삭제됨)
create or replace function public.delete_my_account()
returns void
language plpgsql
security definer
set search_path = public
as $$
begin
  if auth.uid() is null then
    raise exception 'not signed in';
  end if;
  delete from auth.users where id = auth.uid();
end;
$$;

revoke all on function public.delete_my_account() from public, anon;
grant execute on function public.delete_my_account() to authenticated;

-- 3) 학습 진도(회원): 브라우저의 *:progress 기록을 계정에 맞춰 저장
create table if not exists public.user_progress (
  user_id uuid not null references auth.users (id) on delete cascade,
  store text not null,          -- 예: lit-arena:progress
  lesson_id text not null,      -- 예: c14-ch01-l01, c14-ch01-l01-essay
  rec jsonb not null,           -- {done, first, total, at}
  updated_at timestamptz not null default now(),
  primary key (user_id, store, lesson_id)
);
alter table public.user_progress enable row level security;
revoke all on public.user_progress from anon;
grant select, insert, update on public.user_progress to authenticated;

drop policy if exists "progress_select_own" on public.user_progress;
create policy "progress_select_own" on public.user_progress for select using (auth.uid() = user_id);
drop policy if exists "progress_insert_own" on public.user_progress;
create policy "progress_insert_own" on public.user_progress for insert with check (auth.uid() = user_id);
drop policy if exists "progress_update_own" on public.user_progress;
create policy "progress_update_own" on public.user_progress for update using (auth.uid() = user_id) with check (auth.uid() = user_id);

-- 4) 관리자: admins 표에 들어 있는 회원만. 표 자체는 아무도 직접 읽지 못하고 아래 함수로만 확인한다.
create table if not exists public.admins (
  user_id uuid primary key references auth.users (id) on delete cascade,
  created_at timestamptz not null default now()
);
alter table public.admins enable row level security;
revoke all on public.admins from anon, authenticated;

create or replace function public.is_admin()
returns boolean language sql security definer set search_path = public stable as $$
  select exists (select 1 from public.admins where user_id = auth.uid());
$$;
revoke all on function public.is_admin() from public, anon;
grant execute on function public.is_admin() to authenticated;

create or replace function public.admin_overview()
returns json language plpgsql security definer set search_path = public as $$
declare r json;
begin
  if not public.is_admin() then raise exception 'forbidden'; end if;
  select json_build_object(
    'members', (select count(*) from auth.users),
    'new_7d', (select count(*) from auth.users where created_at > now() - interval '7 days'),
    'new_30d', (select count(*) from auth.users where created_at > now() - interval '30 days'),
    'consented', (select count(*) from public.profiles where age14_confirmed),
    'learners', (select count(distinct user_id) from public.user_progress),
    'records', (select count(*) from public.user_progress),
    'active_7d', (select count(distinct user_id) from public.user_progress where updated_at > now() - interval '7 days'),
    'providers', coalesce((select json_object_agg(p, c) from (select coalesce(raw_app_meta_data->>'provider','email') p, count(*) c from auth.users group by 1) t), '{}'::json),
    'stores', coalesce((select json_object_agg(store, c) from (select store, count(*) c from public.user_progress group by 1) t), '{}'::json),
    'daily', coalesce((select json_agg(json_build_object('d', d, 'n', n) order by d) from (
        select g::date d, (select count(*) from auth.users u where u.created_at::date = g::date) n
        from generate_series(current_date - 13, current_date, interval '1 day') g) t), '[]'::json)
  ) into r;
  return r;
end $$;
revoke all on function public.admin_overview() from public, anon;
grant execute on function public.admin_overview() to authenticated;

create or replace function public.admin_members(p_limit int default 200, p_offset int default 0)
returns table (id uuid, email text, provider text, created_at timestamptz, last_sign_in_at timestamptz,
               age14 boolean, agreed_at timestamptz, done_count bigint, last_activity timestamptz)
language plpgsql security definer set search_path = public as $$
begin
  if not public.is_admin() then raise exception 'forbidden'; end if;
  return query
    select u.id, u.email::text, coalesce(u.raw_app_meta_data->>'provider','email'), u.created_at, u.last_sign_in_at,
           coalesce(p.age14_confirmed, false), p.agreed_at,
           coalesce(g.n, 0), g.last_at
    from auth.users u
    left join public.profiles p on p.id = u.id
    left join (select user_id, count(*) n, max(updated_at) last_at from public.user_progress group by 1) g on g.user_id = u.id
    order by u.created_at desc
    limit least(greatest(p_limit,1), 500) offset greatest(p_offset,0);
end $$;
revoke all on function public.admin_members(int,int) from public, anon;
grant execute on function public.admin_members(int,int) to authenticated;

create or replace function public.admin_member_progress(p_user uuid)
returns table (store text, done bigint, last_at timestamptz)
language plpgsql security definer set search_path = public as $$
begin
  if not public.is_admin() then raise exception 'forbidden'; end if;
  return query select s.store, count(*), max(s.updated_at) from public.user_progress s where s.user_id = p_user group by s.store order by 1;
end $$;
revoke all on function public.admin_member_progress(uuid) from public, anon;
grant execute on function public.admin_member_progress(uuid) to authenticated;

-- 관리자 지정(본인 이메일로 바꿔 한 번만 실행):
-- insert into public.admins (user_id) select id from auth.users where email = '내 이메일@example.com';
