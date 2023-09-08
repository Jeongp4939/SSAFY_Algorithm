import heapq
INF = int(2e10)
def dijkstra(s):
    q = []
    heapq.heappush(q,(0,s))
    distances[s] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]

            if cost<distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
distances = [INF]*(n+1)
MIN = 2e10

for _ in range(m):
    s,e,c = map(int,input().split())
    graph[s].append((e,c))
    graph[e].append((s,c))

dijkstra(1)

print(distances[n])