"""코스6 독립 검산: 문장에서 수치를 다시 읽어 정답을 새로 계산해 비교"""
import json, glob, re, sys, math
from fractions import Fraction as F
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
TR = standard_transformations + (implicit_multiplication_application,)
PE = lambda t: parse_expr(t.replace('−', '-').replace('²', '**2'), transformations=TR, local_dict={'x': sp.Symbol('x'), 'y': sp.Symbol('y'), 'z': sp.Symbol('z')})
N = lambda s: int(s.replace('−', '-'))
def A(q):
    if 'answer' in q: return [str(q['answer'])]
    return [b['answers'][0] for b in q['blanks']]
x, y, z = sp.symbols('x y z')
def P(s): return sp.sympify(s.replace('−', '-').replace('²', '**2').replace(' ', '').replace('x**2', '*x**2').replace('y**2', '*y**2').lstrip('*').replace('(*', '(').replace('+*', '+').replace('-*', '-').replace('=*', '='), locals={'x': x, 'y': y, 'z': z}) if False else None
num = r'(−?\d+)'
def chk(p, a):
    a = [s.replace('−', '-') for s in a]
    def eqv(v): return F(a[0]) == F(str(sp.nsimplify(v))) if len(a) == 1 else None
    R = lambda pat: re.search(pat, p)
    if m := R(r'점 \((−?\d+), (−?\d+)\)에서의 접선은 (.*) = \{\{1\}\}') :
        x0, y0 = N(m[1]), N(m[2]); lhs = sp.sympify(m[3].replace('−', '-').replace('x', '*x').replace('y', '*y').replace(' ', '').replace('(*', '(').lstrip('*').replace('+*', '+').replace('-*', '-'))
        cur = re.search(r'(타원|쌍곡선|원) (.*?) 위의', p)[2].replace('−', '-').replace('²', '**2').replace(' ', '')
        L, Rr = cur.split('='); g = sp.sympify(L) - sp.sympify(Rr)
        assert g.subs({x: x0, y: y0}) == 0, 'not on curve'
        # tangent normal ∝ gradient
        gx, gy = sp.diff(g, x).subs({x: x0, y: y0}), sp.diff(g, y).subs({x: x0, y: y0})
        cx, cy = lhs.coeff(x), lhs.coeff(y)
        assert sp.simplify(cx * gy - cy * gx) == 0, 'not tangent dir'
        return F(a[0]) == F(str(lhs.subs({x: x0, y: y0})))
    if m := R(r'타원 x²/(\d+) \+ y²/(\d+) = 1'):
        a2, b2 = int(m[1]), int(m[2]); A2, B2 = max(a2, b2), min(a2, b2); c = math.isqrt(A2 - B2)
        if '장축의 길이' in p: return eqv(2 * math.isqrt(A2))
        if '단축의 길이' in p: return eqv(2 * math.isqrt(B2))
        if '초점은' in p: return eqv(c) and c * c == A2 - B2
        if '두 초점 사이' in p: return eqv(2 * c)
        if '넓이' in p: return eqv(math.isqrt(a2) * math.isqrt(b2))
        if m2 := R(r'y = (\d*)x \+ k'):
            mm = int(m2[1] or 1); k = sp.symbols('k'); dis = sp.discriminant(sp.expand(x**2 / a2 + (mm * x + k)**2 / b2 - 1) * a2 * b2, x)
            return set(sp.solve(dis, k)) == {sp.sqrt(F(a[0])), -sp.sqrt(F(a[0]))} or sp.solve(dis, k)[0]**2 == F(a[0])
        if '기울기가 0' in p: return eqv(math.isqrt(b2))
    p2 = re.sub(r'([xy])²(?!/)', r'\1²/1', p) if '쌍곡선' in p else p
    if m := re.search(r'쌍곡선 x²/(\d+) − y²/(\d+) = (−?1)', p2):
        a2, b2, s = int(m[1]), int(m[2]), N(m[3]); c = math.isqrt(a2 + b2); aa = math.isqrt(a2 if s == 1 else b2)
        if '초점은' in p: return eqv(c) and c * c == a2 + b2
        if '주축' in p: return eqv(2 * aa)
        if '꼭짓점' in p: return eqv(aa)
        if '점근선' in p: return eqv(sp.sqrt(b2) / sp.sqrt(a2))
    if m := R(r'쌍곡선 x²/(\d+) − y²/(\d+) = 1의 점근선'): pass
    if m := R(r'포물선 (y²|x²) = (−?\d+)(x|y)'):
        p_ = F(N(m[2]), 4)
        if '초점' in p and '좌표는' in p: return eqv(p_)
        if '준선' in p: return eqv(-p_)
        if m2 := R(r'기울기가 (−?\d+)인 것의 접점'): return eqv(2 * p_ * N(m2[1]))
        if m2 := R(r'기울기가 (−?\d+)인 직선의 y절편'): return eqv(p_ / N(m2[1]))
        if m2 := R(r'x좌표가 (\d+)인 점과 초점'): return eqv(int(m2[1]) + p_)
        if m2 := R(r'점 \((\d+), (−?\d+)\)에서의 접선은 y = (.*)x \+ \{\{1\}\}'):
            x0, y0 = int(m2[1]), N(m2[2]); return F(a[0]) == y0 - F(2 * p_, y0) * x0
    if m := R(r'초점이 \((−?\d+), 0\), 준선이 x = (−?\d+)인 포물선의 꼭짓점'): return eqv(F(N(m[1]) + N(m[2]), 2))
    if m := R(r'초점이 \(0, (\d+)\), 준선이 y = −\d+인 포물선 위에서 x좌표가 (\d+)'): return eqv(F(int(m[2])**2, 4 * int(m[1])))
    if m := R(r'초점이 \(?(.*?)\)?, 준선이 (x|y) = (−?\d+)인 포물선이'): return eqv(-4 * N(m[3]))
    if m := R(r'지름 (\d+)m, 깊이 (\d+)m'): return eqv(F((int(m[1]) // 2)**2, 4 * int(m[2])))
    if m := R(r'a = (\d+), c = (\d+)인 타원'): a_, c_ = int(m[1]), int(m[2]); b_ = math.isqrt(a_ * a_ - c_ * c_); return eqv(2 * b_ if '단축' in p else b_)
    if m := R(r'a = (\d+), b = (\d+)인 타원'): return eqv(math.isqrt(int(m[1])**2 - int(m[2])**2))
    if m := R(r'a = (\d+), c = (\d+)인 쌍곡선'): a_, c_ = int(m[1]), int(m[2]); return eqv(F(c_, a_) if '이심률' in p else math.isqrt(c_ * c_ - a_ * a_))
    if m := R(r'a = (\d+), b = (\d+)인 쌍곡선'): return eqv(math.isqrt(int(m[1])**2 + int(m[2])**2))
    if m := R(r'장반경 a = (\d+), 초점 거리 c = (\d+)'): return eqv(int(m[1]) + (1 if '먼' in p else -1) * int(m[2]))
    if m := R(r'두 초점이 \(±(\d+), 0\)이고 (장축|주축)의 길이가 (\d+)'): c_, a_ = int(m[1]), int(m[3]) // 2; return eqv(a_ * a_ - c_ * c_ if m[2] == '장축' else c_ * c_ - a_ * a_)
    if m := R(r'거리의 합이 (\d+)인 타원 위의 점 P에서 PF = (\d+)'): return eqv(int(m[1]) - int(m[2]))
    if m := R(r'거리의 차가 (\d+)인 쌍곡선 위의 점 P에서 PF = (\d+)'): return eqv(int(m[1]) + int(m[2]))
    if m := R(r'^(.*?)[은는] 어떤 곡선'):
        e = m[1].replace('−', '-').replace('²', '**2'); L, Rr = e.split('=')
        g = sp.Poly(PE(L) - PE(Rr), x, y)
        ax, ay = g.coeff_monomial(x**2), g.coeff_monomial(y**2)
        k = 3 if ax * ay == 0 else 4 if ax * ay < 0 else 1 if ax == ay else 2
        return eqv(k)
    vre = r'\((−?\d+), (−?\d+)\)'
    if m := R(r'^A\((−?\d+), (−?\d+)\), B\((−?\d+), (−?\d+)\)일 때 \|AB\|'): return eqv(sp.sqrt((N(m[3]) - N(m[1]))**2 + (N(m[4]) - N(m[2]))**2))
    if m := R(r'^A\((−?\d+), (−?\d+)\), B\((−?\d+), (−?\d+)\)일 때 AB ='): return a == [str(N(m[3]) - N(m[1])), str(N(m[4]) - N(m[2]))]
    if m := R(r'\|a\| = (\d+), \|b\| = (\d+)이고 a와 b가 수직'): return eqv(sp.sqrt(int(m[1])**2 + int(m[2])**2))
    if m := R(r'\|a\| = (\d+), \|b\| = (\d+)이고 이루는 각이 (\d+)°'): return eqv(sp.nsimplify(int(m[1]) * int(m[2]) * sp.cos(sp.rad(int(m[3])))))
    if m := R(r'\|a\| = (\d+)일 때 \|(−?\d*)a\|'): return eqv(abs(N(m[2] or '1')) * int(m[1]))
    if m := R(r'\(k( [+−] \d+)?\)a \+ (\d*)b = (−?\d+)a \+ mb일 때 (k|m)') or R(r'ka \+ (\d*)b = (−?\d+)a \+ mb일 때 (k|m)'):
        if m.re.pattern.startswith('ka'): c, d, pp, w = 0, int(m[1] or 1), N(m[2]), m[3]
        else: c, d, pp, w = N(m[1].replace(' ', '')) if m[1] else 0, int(m[2] or 1), N(m[3]), m[4]
        return eqv(pp - c if w == 'k' else d)
    if m := R(r'^' + vre + r'·' + vre + r'의 값'): return eqv(N(m[1]) * N(m[3]) + N(m[2]) * N(m[4]))
    if m := R(r'^\((−?\d+), (−?\d+), (−?\d+)\)·\((−?\d+), (−?\d+), (−?\d+)\)의 값'): return eqv(sum(N(m[i]) * N(m[i + 3]) for i in (1, 2, 3)))
    if m := R(r'^\((−?\d+), k\)[와과] ' + vre + r'[이가] 수직'): return eqv(F(-N(m[1]) * N(m[2]), N(m[3])))
    if m := R(r'^\((−?\d+), (−?\d+), k\)[와과] \((−?\d+), (−?\d+), (−?\d+)\).? 수직'): return eqv(F(-(N(m[1]) * N(m[3]) + N(m[2]) * N(m[4])), N(m[5])))
    if m := R(r'^\((−?\d+), k\)[와과] ' + vre + r'[이가] 평행'): return eqv(F(N(m[1]) * N(m[3]), N(m[2])))
    if m := R(r'^\(k, (−?\d+)\)[와과] ' + vre + r'[이가] 평행'): return eqv(F(N(m[1]) * N(m[2]), N(m[3])))
    if m := R(r'^' + vre + r'.? ' + vre + r'.? 이루는 각'):
        u, w = sp.Matrix([N(m[1]), N(m[2])]), sp.Matrix([N(m[3]), N(m[4])]); return eqv(sp.deg(sp.acos(u.dot(w) / (u.norm() * w.norm()))))
    if m := R(r'^' + vre + r'.? 같은 방향의 단위벡터는 \(\{\{1\}\}/(\d+), (\d+)/(\d+)\)'): return sp.sqrt(N(m[1])**2 + N(m[2])**2) == int(m[3]) and a == [str(N(m[1]))] and m[2] == m[4]
    if m := R(r'^(−?\d*)' + vre + r' \+ (?:\((−?\d+)\)|(\d+))?' + vre + r' = \(\{\{1\}\}, \{\{2\}\}\)') or R(r'^(−?\d*)' + vre + r' − ()()' + vre + r' = '):
        k = N(m[1]) if m[1] not in ('', '−') else (1 if m[1] == '' else -1); l = N(m[4] or m[5] or '1') if '−' not in p.split(')', 1)[1][:4] or m[4] else -1
        if m[4] is None and m[5] is None and ' − (' in p: l = -1
        return a == [str(k * N(m[2]) + l * N(m[6])), str(k * N(m[3]) + l * N(m[7]))]
    if m := R(r'방향벡터가 ' + vre + r'인 직선의 기울기'): return eqv(F(N(m[2]), N(m[1])))
    if m := R(r'점 ' + vre + r'.? 지나고 법선벡터가 ' + vre): return eqv(N(m[1]) * N(m[3]) + N(m[2]) * N(m[4]))
    if m := R(r'\+ t' + vre + r'에서 t = (−?\d+)일 때'):
        x0 = N(re.search(r'= \((−?\d+),', p)[1]); return eqv(x0 + N(m[1]) * N(m[3]))
    if m := R(r'\|p − \((−?\d+), (−?\d+)\)\| = (\d+)'): return eqv(int(m[3]))
    if m := R(r'A\((−?\d+), 0\), B\((−?\d+), 0\)에 대해 \(p'): return eqv(F(N(m[2]) - N(m[1]), 2))
    if m := R(r'A\(0, 0\), B\((\d+), 0\)에 대해 \|PA\| = 2\|PB\|'):
        d = int(m[1]); g = sp.expand(x**2 + y**2 - 4 * ((x - d)**2 + y**2)); cx = sp.solve(sp.diff(g, x), x)[0]; r2 = cx**2 - g.subs({x: 0, y: 0}) / (-3)
        return eqv(sp.sqrt(r2) if '반지름' in p else cx)
    if m := R(r'원 x² \+ y² = (\d+) 위의 점 ' + vre + r'에서의 접선은 (.*) = \{\{1\}\}'): return N(m[2])**2 + N(m[3])**2 == int(m[1]) and eqv(int(m[1]))
    if m := R(r'세 점 A' + vre + r', B' + vre + r', C\((−?\d+), k\)'):
        x1, y1, x2, y2, x3 = map(N, m.groups()); return eqv(y1 + F(y2 - y1, x2 - x1) * (x3 - x1))
    if m := R(r'a = \((\d+), (\d+)\)[을를] b = \((\d), (\d)\) 방향'): return eqv(int(m[1]) * int(m[3]) + int(m[2]) * int(m[4]))
    if m := R(r'(\d) : (\d)(?:으로|로) 내분하는 점의 위치벡터는 \((\d*)a \+ \{\{1\}\}b\)/(\d+)'): return a == [m[1]] and int(m[3] or 1) == int(m[2]) and int(m[4]) == int(m[1]) + int(m[2])
    if m := R(r'세 점 ' + vre + ', ' + vre + ', ' + vre + r'[을를] 꼭짓점'): return eqv(F(N(m[1]) + N(m[3]) + N(m[5]), 3))
    if '정육면체' in p:
        V = dict(zip("ABCDEFGH", [(0,0,0),(1,0,0),(1,1,0),(0,1,0),(0,0,1),(1,0,1),(1,1,1),(0,1,1)]))
        E = [(u, w) for u in V for w in V if u < w and sum(abs(i - j) for i, j in zip(V[u], V[w])) == 1]
        def d(e): return tuple(abs(i - j) for i, j in zip(V[e[0]], V[e[1]]))
        def meet(e, f): return bool(set(e) & set(f))
        def ed(s): return tuple(sorted(s))
        if '이면각' in p: return eqv(45)
        if m := R(r'모서리 ([A-H]{2})와 ([A-H]{2})의 위치'):
            e, f = ed(m[1]), ed(m[2]); return eqv(1 if meet(e, f) else 2 if d(e) == d(f) else 3)
        if m := R(r'모서리 ([A-H]{2})와 (꼬인 위치에 있는|평행한|만나는) 모서리'):
            e = ed(m[1]); fn = {'꼬인 위치에 있는': lambda f: not meet(e, f) and d(e) != d(f), '평행한': lambda f: d(e) == d(f) and f != e, '만나는': lambda f: meet(e, f) and f != e}[m[2]]
            return eqv(sum(fn(f) for f in E))
        if m := R(r'면 ([A-H]{4})와 (평행한 모서리|수직인 모서리|포함된 모서리|수직인 면|평행한 면)'):
            pts = [V[c] for c in m[1]]; ax = [i for i in range(3) if len({q[i] for q in pts}) == 1][0]; lv = pts[0][ax]
            faces = [(i, l) for i in range(3) for l in (0, 1)]
            k = m[2]
            if k == '평행한 모서리': v = sum(all(V[c][ax] != lv for c in e) for e in E)
            elif k == '수직인 모서리': v = sum(d(e)[ax] == 1 for e in E)
            elif k == '포함된 모서리': v = sum(all(V[c][ax] == lv for c in e) for e in E)
            elif k == '수직인 면': v = sum(i != ax for i, l in faces)
            else: v = sum(i == ax and l != lv for i, l in faces)
            return eqv(v)
    if m := R(r'PO = (\d+), OH = (\d+)일 때 PH'): return eqv(sp.sqrt(int(m[1])**2 + int(m[2])**2))
    if m := R(r'PO = (\d+), PH = (\d+)일 때 OH'): return eqv(sp.sqrt(int(m[2])**2 - int(m[1])**2))
    if m := R(r'OH = (\d+), PH = (\d+)일 때 PO'): return eqv(sp.sqrt(int(m[2])**2 - int(m[1])**2))
    if m := R(r'길이 (\d+)인 선분이 평면과 (\d+)°'): return eqv(sp.nsimplify(int(m[1]) * sp.cos(sp.rad(int(m[2])))))
    if m := R(r'넓이 (\d+)인 도형이 평면과 (\d+)°를 이룰 때 정사영의 넓이는 \{\{1\}\}√3'): return eqv(sp.nsimplify(int(m[1]) * sp.cos(sp.rad(int(m[2]))) / sp.sqrt(3)))
    if m := R(r'넓이 (\d+)인 도형이 평면과 (\d+)°'): return eqv(sp.nsimplify(int(m[1]) * sp.cos(sp.rad(int(m[2])))))
    if m := R(r'넓이 (\d+)인 도형의 정사영의 넓이가 (\d+)(√2)?일'): return eqv(sp.deg(sp.acos(int(m[2]) * (sp.sqrt(2) if m[3] else 1) / int(m[1]))))
    v3 = r'\((−?\d+), (−?\d+), (−?\d+)\)'
    if m := R(r'점 ' + v3 + r'.? (xy평면|yz평면|zx평면|원점|x축|z축)에 대하여'):
        X = [N(m[i]) for i in (1, 2, 3)]; s = {'xy평면': (1, 1, -1), 'yz평면': (-1, 1, 1), 'zx평면': (1, -1, 1), '원점': (-1, -1, -1), 'x축': (1, -1, -1), 'z축': (-1, -1, 1)}[m[4]]
        return a == [str(i * j) for i, j in zip(X, s)]
    if m := R(r'두 점 ' + v3 + ', ' + v3 + r' 사이의 거리'): return eqv(sp.sqrt(sum((N(m[i]) - N(m[i + 3]))**2 for i in (1, 2, 3))))
    if m := R(r'A' + v3 + r', B' + v3 + r'(?:[을를] (\d) : (\d)(?:으로|로) 내분하는 점|의 중점)의 (x|y|z)좌표'):
        k = 'xyz'.index(m[9]); pp, qq = int(m[7] or 1), int(m[8] or 1); return eqv(F(pp * N(m[k + 4]) + qq * N(m[k + 1]), pp + qq))
    if m := R(r'구 (.*) = 0의 (중심|반지름)'):
        g = PE(m[1]); cx, cy, cz = [sp.solve(sp.diff(g, s_), s_)[0] for s_ in (x, y, z)]
        if m[2] == '중심': return a == [str(cx), str(cy), str(cz)]
        return eqv(sp.sqrt(-g.subs({x: cx, y: cy, z: cz})))
    if m := R(r'중심이 ' + v3 + r'이고 (xy|yz|zx)평면에 접하는'): return eqv(abs(N(m[{'xy': 3, 'yz': 1, 'zx': 2}[m[4]]])))
    if m := R(r'중심이 ' + v3 + r'이고 원점을 지나는'): return eqv(sum(N(m[i])**2 for i in (1, 2, 3)))
    if m := R(r'^벡터 \((\d+), (\d+), (\d+)\)의 크기'): return eqv(sp.sqrt(sum(int(m[i])**2 for i in (1, 2, 3))))
    if m := R(r'^' + v3 + r' (\+|−) (?:\((−?\d+)\)|(\d+))?' + v3 + ' = '):
        c = N(m[5] or m[6] or '1') * (-1 if m[4] == '−' else 1); return a == [str(N(m[i]) + c * N(m[i + 6 - 0])) for i in (1, 2, 3)] if False else a == [str(N(m[i]) + c * N(m[i + 6])) for i in (1, 2, 3)]
    if m := R(r'^' + v3 + r'·' + v3): return eqv(sum(N(m[i]) * N(m[i + 3]) for i in (1, 2, 3)))
    if m := R(r'점 P와 초점 사이의 거리가 (\d+)'): return eqv(int(m[1]))
    if m := R(r'초점과 준선 사이의 거리가 (\d+)'): return eqv(F(int(m[1]), 2))
    return 'skip'
bad = skip = ok = 0
for f in sys.argv[1:]:
    for q in json.load(open(f))['questions']:
        try: r = chk(q['prompt'], A(q))
        except Exception as e: r = f'ERR {e}'
        if r == 'skip': skip += 1; print('SKIP', f[-13:], q['prompt'][:90])
        elif r is True: ok += 1
        else: bad += 1; print('BAD', f[-13:], r, q['prompt'][:120], A(q))
print('ok', ok, 'bad', bad, 'skip', skip)
