#4
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
sl = {i: 0 for i in range(1, len(s) + 1)}

for i in range(len(s)):
    if i == 0:
        sl[len(s)] += 1
    else:
        if z_function(s)[i] != 0:
            sl[z_function(s)[i]] += 1
for i in reversed(range(1, len(s))):
    sl[i] += sl[i+1]

res = {s[:i]: sl[i] for i in range(1, len(s) + 1)}
for i in res:
    print(f"{i} - {res[i]}")

