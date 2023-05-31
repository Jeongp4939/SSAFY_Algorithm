# 1 알뜰 기차여행
#
# from heapq import heappush,heappop
# INF = 1e11
# def dijkstra(st):
#     q=[]
#     heappush(q,(0,st))
#     distance[st]=0
#
#     while q:
#         dist,node = heappop(q)
#         if distance[node] < dist:
#             continue
#         for next in graph[node]:
#             cost = distance[node] + next[1]
#             if cost < distance[next[0]]:
#                 distance[next[0]] = cost
#                 heappush(q, (cost,next[0]))
#     return distance[n-1] if distance[n-1]<INF else 'impossible'
#
#
# n,v = map(int,input().split())
# graph = [[] for _ in range(n)]
# for _ in range(v):
#     a,b,c = map(int,input().split())
#     graph[a].append((b,c))
# distance = [INF]*n
#
# print(dijkstra(0))


# 2 통행료

from heapq import heappush,heappop
INF = 1e11

def dijkstra(st,ed):
    q=[]
    heappush(q,(0,st))
    distance = [INF] * (n + 1)
    distance[st]=0

    while q:
        dist,node = heappop(q)
        if distance[node] < dist:
            continue
        for next_node, cost in graph[node]:
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heappush(q, (new_cost,next_node))
    return distance[ed]


n,m,k = map(int,input().split())
a,b = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    f,t,c = map(int,input().split())
    graph[f].append([t,c])

print(dijkstra(a, b))

for _ in range(k):

    p = int(input())
    for i in graph:
        if i:
            for j in i:
                j[1] += p
    print(dijkstra(a,b))



