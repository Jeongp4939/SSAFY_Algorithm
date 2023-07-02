import heapq
import sys

input = sys.stdin.readline

INF = 1e9

def dijkstra(st):
    distances = [INF] * (n + 1)
    distances[st] = 0
    q = []
    heapq.heappush(q, [distances[st], st])

    while q:
        dist, node = heapq.heappop(q)

        if distances[node] < dist:
            continue

        for new_node, new_dist in graph[node]:
            distance = dist + new_dist
            if distance < distances[new_node]:
                distances[new_node] = distance
                heapq.heappush(q, (distance, new_node))
    return distances

for tc in range(int(input())):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    cross_dist = 0
    graph = [[] for _ in range(n+1)]
    result = []

    for i in range(m):
        a,b,d = map(int,input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))

    dist_s = dijkstra(s)
    dist_g = dijkstra(g)
    dist_h = dijkstra(h)

    for j in range(t):
        x = int(input())
        res1 = dist_s[g]+dist_g[h]+dist_h[x]
        res2 = dist_s[h]+dist_h[g]+dist_g[x]
        if dist_s[x] == res1 or dist_s[x] == res2:
            result.append(x)

    result.sort()
    print(*result)