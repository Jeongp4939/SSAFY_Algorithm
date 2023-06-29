import sys
from collections import deque

input = sys.stdin.readline

dy,dx = (1,0,-1,0),(0,1,0,-1)
def bfs(y,x):
    visited = [[-1] * m for _ in range(n)]
    visited[0][0] = 0

    q = deque()
    q.append((y,x))

    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<n and 0<=nx<m and visited[ny][nx]==-1:
                if arr[ny][nx] == 0:
                    visited[ny][nx]=visited[y][x]
                    q.appendleft((ny,nx))
                else:
                    visited[ny][nx] = visited[y][x]+1
                    q.append((ny,nx))
    return visited[n-1][m-1]


m,n = map(int,input().split())
arr = [list(map(int,input().rstrip())) for _ in range(n)]

print(bfs(0,0))

