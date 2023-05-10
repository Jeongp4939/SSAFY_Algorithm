from collections import deque

N = int(input())
A = [[] for _ in range(N+1)]

for _ in range(N):
    data = list(map(int,input().split()))
    idx = 0
    s = data[idx]
    idx+=1
    while True:
        e = data[idx]
        if e==-1:
            break
        v = data[idx+1]
        A[s].append((e,v))
        idx += 2
dist = [0]*(N+1)
visited = [0]*(N+1)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        now = q.popleft()
        for i in A[now]:
            if not visited[i[0]]:
                visited[i[0]]=1
                q.append(i[0])
                dist[i[0]] = dist[now]+i[1]

bfs(1)
MAX = 1

for i in range(2,N+1):
    if dist[MAX] < dist[i]:
        MAX = i

dist = [0]*(N+1)
visited = [0]*(N+1)
bfs(MAX)
dist.sort()
print(dist[N])
