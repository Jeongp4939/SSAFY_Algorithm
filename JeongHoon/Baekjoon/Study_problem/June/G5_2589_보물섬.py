from collections import deque

dy,dx = [-1,1,0,0],[0,0,-1,1]

def bfs(tup):
    global MAX
    q = deque()
    q.append(tup)
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<m and arr[ny][nx]=='L':
                if visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x]+1
                    MAX = max(MAX,visited[ny][nx])
                    q.append((ny,nx))


n,m = map(int,input().split())
arr = [list(input()) for _ in range(n)]
MAX = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            visited = [[0]*m for _ in range(n)]
            visited[i][j] = 1
            bfs((i,j))

print(MAX-1)