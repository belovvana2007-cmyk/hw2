#2
n = int(input())
graph = {i: {} for i in range(n)}

for i in range(n):
    graph_line = list(map(float, input().split()))
    u = int(graph_line[0])
    v = int(graph_line[1])
    k = graph_line[2]  
    graph[u][v] = k

def bellman_ford(G, start):
    d = {i: 0.0 for i in G}  
    d[start] = 1.0  
    for i in range(len(G)-1):
        for node1 in list(graph.keys()):
            if d.get(node1, 0) == 0:
                continue
            for node2 in G[node1]:
                new_d = d[node1] * G[node1][node2]
                if new_d > d[node2]: 
                    d[node2] = new_d
    return d

def check(G):
    for start in range(n):
        d = bellman_ford(G, start)
        for node1 in G:
            for node2 in G[node1]:
                if d.get(node1, float("inf")) != float("inf"):
                    if d[node2] > d[node1] + G[node1][node2]:
                        return True
    return False

if check(graph):
    print("YES")
else:
    print("NO")
