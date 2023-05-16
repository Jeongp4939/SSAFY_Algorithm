# 1 알뜰 기차여행

from heapq import heappush,heappop
INF = 1e11
def dijkstra(st):
    q=[]
    heappush(q,(0,st))
    distance[st]=0

    while q:
        dist,node = heappop(q)
        if distance[node] < dist:
            continue
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heappush(q, (cost,next[0]))
    return distance[n-1] if distance[n-1]<INF else 'impossible'


n,v = map(int,input().split())
graph = [[] for _ in range(n)]
for _ in range(v):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
distance = [INF]*n

print(dijkstra(0))
