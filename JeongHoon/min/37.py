"""
# 1 바이러스 2군데 투여
from collections import deque

dy,dx = [-1,1,0,0],[0,0,-1,1]
def bfs():
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<N and 0<=nx<N:
                if not arr[ny][nx]:
                    arr[ny][nx] = arr[y][x]+1
                    q.append((ny,nx))

N = int(input())
arr = [[0]*N for _ in range(N)]
lst = list(map(int,input().split()))
q = deque()

for i in range(2):
    y,x = lst[i*2:i*2+2]
    arr[y][x] = 1
    q.append(lst[i*2:i*2+2])

bfs()
for i in range(N):
    for j in range(N):
        print(arr[i][j], end='')
    print()
"""
"""
# 2 BBQ 장작
from collections import deque

dy,dx = [-1,1,0,0],[0,0,-1,1]
def bfs(st):
    q = deque()
    q.append(st)
    Max=0
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=ny<N and 0<=nx<M:
                if arr[ny][nx]==0:
                    q.append((ny,nx))
                    arr[ny][nx] = arr[y][x]+1
                    Max = max(arr[ny][nx],Max)
    return Max

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
y,x = map(int,input().split())

print(bfs((y,x)))
"""

# 3 폭죽놀이
