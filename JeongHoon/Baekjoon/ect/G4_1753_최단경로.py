from heapq import heappush, heappop
import sys

input = sys.stdin.readline

INF = int(1e14)
start = 1

def dijkstra(start):
    q=[]
    heappush(q,(0,start))   # 시작노드 정보 큐에 삽입
    distance[start] = 0     # 시작노드-> 시작노드 거리 0
    while q:
        dist, node = heappop(q)
        # 큐에서 뽑은 거리가 이미 갱신된 거리보다 클 때 무시
        if distance[node] < dist:
            continue
        # 큐에서 뽑은 노드와 연결된 인접 노드 탐색
        for next in graph[node]:
            # 시작 -> node 거리 + node->node 인접노드 거리
            cost = distance[node] + next[1]
            # cost < 시작 -> node 인접노드 거리
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heappush(q,(cost,next[0]))

v,e = map(int,input().split())
st = int(input())

graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)
for _ in range(e):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))

dijkstra(st)

for i in range(1,v+1):
    if distance[i]==INF:
        print('INF')
    else:
        print(distance[i])