#1
import copy

N, M = map(int, input().split())

graph = {i: set() for i in range(N)}

for i in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].add(v2) 
    graph[v2].add(v1) 

degrees = {i: len(graph[i]) for i in graph}

order = []
a1 = 0
a2 = 0
components_res = {}

for d in degrees:
  if degrees[d] % 2 != 0:
      a1 += 1

def dfs(G, start, visited, order):
    visited.add(start)
    for i in G[start]:
        if i not in visited:
            dfs(G, i, visited, order)
    order.add(start)

sv = 0
visited = set()

for i in graph:
  if i not in visited:
    sv += 1
    components = set()
    dfs(graph,i,visited, components)
    r = 0
    for c in components:
      r += len(graph[c])
    r = r // 2
    components_res[sv] = r

for i in components_res:
  if components_res[i] != 0:
    a2 += 1

start = None
for i in range(N):
    if degrees[i] % 2 == 1:
        start = i
    elif start is None:  
        start = i

graph_1 = copy.deepcopy(graph)

def path(graph_1, start):

    g = []

    def Euler(a):
        while graph_1[a]: 
            u = graph_1[a].pop()  
            graph_1[u].discard(a) 
            Euler(u)
        g.append(a)
    Euler(start)
    return g[::-1]  

if (a1 == 2 or a1 == 0) and a2 <= 1:
    print("Yes")
    print(' '.join(map(str, path(graph_1, start))))
else:
    print("No")