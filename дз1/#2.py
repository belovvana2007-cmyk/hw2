#2
import heapq

def johnson(G):
    nodes = list(G.keys())
    h = bellman_ford(G, nodes[0])  
    G_new = {}
    for v in nodes:
        G_new[v] = {}
    for v in nodes:
        for u in G[v]:
            G_new[v][u] = G[v][u] + h[v] - h[u]
    
    res = {}
    for start in nodes:
        dist = dijkstra(G_new, start)
        dist_new = {u: dist[u] - h[start] + h[u] for u in nodes}
        res[start] = dist_new
    
    return res

def bellman_ford(G, start):
    d = {i: float("inf") for i in G}
    d[start] = 0
    for i in range(len(G)-1):
        for node1 in d:  
                for node2 in G[node1]:
                    if d[node2] > d[node1] + G[node1][node2]:
                        d[node2] = d[node1] + G[node1][node2]
    return d

def dijkstra(G, start):
    distances = {i: float('inf') for i in G}  
    distances[start] = 0
    h = [(0, start)]
    visited = set()
    while h:
        cur_dist, cur_node = heapq.heappop(h)
        if cur_node in visited:
            continue
        visited.add(cur_node)
        if cur_node not in G:
            continue
        for neighbor in G[cur_node]:
            distance = cur_dist + G[cur_node][neighbor]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(h, (distance, neighbor))
    return distances
