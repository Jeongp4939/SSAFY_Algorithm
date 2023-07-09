from collections import deque

direct = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

def bfs():
    q = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j]:
                q.append((i, j))

    while q:
        y,x = q.popleft()
        for d in direct:
            ny = y+d[0]
            nx = x+d[1]
            if 0<=ny<n and 0<=nx<m:
                if arr[ny][nx] == 0:
                    q.append((ny,nx))
                    arr[ny][nx] = arr[y][x] + 1


n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
result = 0

bfs()
for i in range(n):
    for j in range(m):
        result = max(arr[i][j],result)
print(result-1)