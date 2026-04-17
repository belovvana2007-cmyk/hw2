#5
def z_function(S):
  zf = [0] * len(S)
  left, right = 0, 0
  for i in range(1, len(S)):
    zf[i] = max(0, min(zf[i-left], right - i))
    while i + zf[i] < len(S) and S[zf[i]] == S[i+zf[i]]:
      zf[i] += 1
    if i + zf[i] > right:
      left, right = i, i + zf[i]
  return zf

s = input()
p = input()

p1 = p
sl = []
pos = []
k = 0
res = 0

for i in range(len(p)):
    if p[i] == '?':
        if len(p1[k:i]) > 0:
            sl.append((p1[k:i], k))
        k = i + 1

if k < len(p):
    slice = p1[k:]
    if len(slice) > 0:
        sl.append((slice, k))

if len(sl) == 0:
    pos = list(range(len(s) - len(p) + 1))
else:
    for i in range(len(s) - len(p) + 1):
        for j in range(len(sl)):
            l, m = sl[j]
            s_work = l + '#' + s[i:]
            z = z_function(s_work)
            pos_num = len(l) + 1 + m
            if pos_num >= len(s_work) or z[pos_num] < len(l):
                break
        else:
            pos.append(i)
if pos:
    print(*pos)


