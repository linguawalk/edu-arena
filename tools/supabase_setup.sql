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
