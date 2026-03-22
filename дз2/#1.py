from collections import deque

M = int(input())
G = {}

for i in range(M):
    v1, v2, w = input().split()
    w = int(w)
    if v1 in G:
        G[v1][v2] = w
    else:
        G[v1] = {v2: w}
    if v2 in G:
        G[v2][v1] = 0
    else:
        G[v2] = {v1: 0}

def bfs(G,start,finish,visited,f_min):
    sl = {}
    queue = deque()
    queue.append(start)
    visited.add(start)
    while queue:
        current = queue.popleft()
        for i in G[current]:
            if i not in visited and G[current][i] > 0:
                visited.add(i)
                sl[i] = current
                queue.append(i)

    if finish not in visited:
        return 0
    flow = f_min
    V = []
    i = finish
    while i != start:
        u = sl[i]
        V.append((u, i))
        flow = min(flow, G[u][i])
        i = u
    for u, i in V:
        G[u][i] -= flow
        G[i][u] += flow
    return flow

def edmonds_karp(G, start, finish):
    res = 0
    visited = set()
    while (flow := bfs(G,start,finish,visited,float('inf'))) != 0:
        res += flow
        visited = set()
    return res