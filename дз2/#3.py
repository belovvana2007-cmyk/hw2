n = int(input())
pr = list(map(int, input().split()))
bank = list(map(int, input().split()))

G = {}
G['S'] = {}
G['T'] = {}
sum_pr = 0

def plus_edge(u, v, I):
    if u not in G:
        G[u] = {}
    if v not in G:
        G[v] = {}
    G[u][v] = I
    G[v][u] = 0

for i in range(len(pr)):
  sum_pr += pr[i]

for i in range(n):
    plus_edge('S', f'P{i}', pr[i])

for j in range(n):
    plus_edge(f'B{j}', 'T', bank[j])

for i in range(n):
    for j in range(n):
        plus_edge(f'P{i}', f'B{j}', float('inf'))

if edmonds_karp(G, 'S', 'T') == sum_pr:
    print("YES")
else:
    print("NO")