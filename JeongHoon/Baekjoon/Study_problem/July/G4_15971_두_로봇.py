""" dijkstra (23점)
# a,b 가 통신할 때, a,b는 같은 노드에 있는 것이 아니라 이어진 두 노드에 각각 존재

import sys
import heapq
input = sys.stdin.readline

def dijkstra(st):
    distances = [[INF,[]] for _ in range(n + 1)]
    distances[st][0] = 0
    distances[st][1] += [0]
    q = [(0,st)]

    while q:
        dist, x = heapq.heappop(q)
        if dist > distances[x][0]:
            continue
        for next_x, new_dist in graph[x]:
            next_dist = dist+new_dist

            if dist < distances[next_x][0]:
                distances[next_x][0] = next_dist
                distances[next_x][1] = distances[x][1] + [new_dist]
                heapq.heappush(q,(next_dist,next_x))
    return distances


n, a, b = map(int,input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)

for _ in range(n-1):
    i, j, cost = map(int,input().split())
    graph[i].append((j, cost))
    graph[j].append((i, cost))

distances = dijkstra(a)

print(distances[b][0]-max(distances[b][1]))
"""

