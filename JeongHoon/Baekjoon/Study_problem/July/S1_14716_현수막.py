from collections import deque

dy,dx = (1,-1,0,0,1,1,-1,-1),(0,0,-1,1,1,-1,1,-1)

def bfs(start):
    q = deque([start])

    while q:
        y,x = q.popleft()
        for i in range(8):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=ny<n and 0<=nx<m:
                if arr[ny][nx]:
                    arr[ny][nx]=0
                    q.append((ny,nx))

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if arr[i][j]:
            cnt+=1
            bfs((i,j))

print(cnt)