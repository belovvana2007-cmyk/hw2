#2
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

res = 0

for i in range(len(s)):
    s_work = (s[i:] + s[:i]) + '#' + p
    for j in range(len(s_work)):
        if z_function(s_work)[j] == len(s[i:] + s[:i]):
            res += 1

print(res)