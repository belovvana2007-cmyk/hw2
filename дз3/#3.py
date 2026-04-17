#3
def prefix(s):
    p = [0] * len(s)
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    return p

s = input().split()
s_work = list(set(s))
sl = []
adj = {}
f2 = None

for i in range(len(s_work)):
    f1 = False
    for j in range(len(s_work)):
        if i != j and s_work[i] in s_work[j]:
            f1 = True
    if not f1:
        sl.append(s_work[i])

if len(sl) == 0:
    print("")
    exit()

if len(sl) == 1:
    print(sl[0])
    exit()

visited = [False] * len(sl)

for i in range(len(sl)):
    for j in range(len(sl)):
        if i != j:
            s_new = sl[j] + '#' + sl[i]
            p = prefix(s_new)
            adj[(i, j)] = p[-1]

def ans(a):
    if len(a) == len(sl):
        s = sl[a[0]]
        for i in range(1, len(sl)):
            s += sl[a[i]][adj[(a[i - 1], a[i])]:]
        return s
    f3 = None
    for i in range(len(sl)):
        if not visited[i]:
            visited[i] = True
            cand = ans(a + [i])
            visited[i] = False
            if f3 is None or len(cand) < len(f3):
                best = cand
    return best


print(ans([]))