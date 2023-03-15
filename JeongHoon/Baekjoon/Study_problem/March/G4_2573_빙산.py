# https://www.acmicpc.net/problem/2573
from collections import deque
import copy

def bfs(y,x):
    q = deque([[y, x]])
    visited[y][x] = 1
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < n and 0 <= nx < m:
                if arr[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    q.append([ny, nx])
    return

def melting(y,x):
    q = deque([[y, x]])
    new_visited = [[0] * m for _ in range(n)]
    new_visited[y][x] = 1
    while q:
        y, x = q.popleft()
        cnt=0
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < n and 0 <= nx < m:
                if not arr[ny][nx] and not new_visited[ny][nx]:
                    cnt+=1
                elif arr[ny][nx] and not new_visited[ny][nx]:
                    new_visited[ny][nx]=1
                    q.append([ny, nx])
        arr[y][x] = max(0,arr[y][x]-cnt)
    return arr

dy,dx = [-1,1,0,0],[0,0,-1,1]
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
rlt = 0

for t in range(500):
    visited = [[0] * m for _ in range(n)]
    cnt=0
    for i in range(n):
        for j in range(m):
            if arr[i][j] and not visited[i][j]:
                cnt+=1
                # bfs 실행
                bfs(i,j)
                arr=copy.deepcopy(melting(i, j))
    if cnt >=2:
        rlt=t
        break
    for i in arr:
        if sum(i):
            continue
    rlt=0

print(rlt)