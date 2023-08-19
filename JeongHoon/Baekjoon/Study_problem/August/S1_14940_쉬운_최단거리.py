from collections import deque

dy,dx=(1,-1,0,0),(0,0,-1,1)

def bfs():
    while q:
        y,x = q.popleft()

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if 0<=ny<n and 0<=nx<m:
                if arr[ny][nx]==1 and not visited[ny][nx]:
                    visited[ny][nx] = visited[y][x]+1
                    q.append((ny,nx))


n,m = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
q = deque()

flag=False;
for i in range(n):
    if flag:
        break
    for j in range(m):
        if arr[i][j]==2:
            q.append((i,j))
            flag=True
            break
bfs()

for i in range(n):
    for j in range(m):
        if arr[i][j]==1 and not visited[i][j]:
            visited[i][j] = -1

for i in range(n):
    print(*visited[i])