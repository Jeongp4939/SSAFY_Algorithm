import heapq
import sys

input = sys.stdin.readline

INF = 10e10

def dijkstra(n,st):
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
                heapq.heappush(q, [distance, new_node])
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
        if a==g and b==h or a==h and b==g:
            cross_dist = d

    dist_s = dijkstra(n,s)
    dist_g = dijkstra(n,g)
    dist_h = dijkstra(n,h)

    for j in range(t):
        x = int(input())
        if dist_s[x] == dist_s[g]+dist_g[h]+dist_h[x] or dist_s[x] == dist_s[h]+dist_h[g]+dist_g[x]:
            result.append(x)

    result.sort()
    print(*result)