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
"""
# 3 폭죽놀이
from collections import deque
dy = [-1,1,0,0,1,-1,1,-1]
dx = [0,0,-1,1,1,1,-1,-1]

arr = [list(map(int,input().split())) for _ in range(4)]
q = deque()
for i in range(4):
    for j in range(5):
        if arr[i][j]==1:
            q.append((i,j))
result = 0
while q:
    y,x = q.popleft()
    for i in range(8):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=ny<4 and 0<=nx<5:
            if not arr[ny][nx]:
                arr[ny][nx] = arr[y][x]+1
                result = max(result, arr[ny][nx])
                q.append((ny,nx))

print(result-1)
"""
"""
# 4 무인도의 크기
from collections import deque
dy = [-1,1,0,0]
dx = [0,0,-1,1]

arr = [list(map(int,input().split())) for _ in range(4)]
q = deque()
q.append((0,0))
result = 0
while q:
    y,x = q.popleft()
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=ny<4 and 0<=nx<4:
            if arr[ny][nx]:
                arr[ny][nx] = 0
                result += 1
                q.append((ny,nx))
print(result)
"""
"""
# 5 BFS로 미로찾기

from collections import deque

dy = [-1,1,0,0]
dx = [0,0,-1,1]
arr = [[0,0,0,0],
       [1,1,0,1],
       [0,0,0,0],
       [1,0,1,0]]

q = deque()
sy,sx = map(int,input().split())
ey,ex = map(int,input().split())

q.append((sy,sx))

while q:
    y,x = q.popleft()
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<4 and 0<=nx<4:
            if not arr[ny][nx]:
                arr[ny][nx] = arr[y][x]+1
                if ny==ey and nx==ex:
                    break
                q.append((ny,nx))
print('%d회'%arr[ey][ex])
"""
"""
# 6 고기가 좋아
from collections import deque
dy = [-1,1,0,0]
dx = [0,0,-1,1]

arr = [list(map(int,input().split())) for _ in range(4)]
q = deque()
q.append((0,0))
result = 0
while q:
    y,x = q.popleft()
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=ny<4 and 0<=nx<6:
            if arr[ny][nx] != 1:
                if arr[ny][nx]==2:
                    result +=1
                arr[ny][nx] = 1
                q.append((ny,nx))
print(result)
"""
"""
# 친구 만나러 가는 길
from collections import deque
dy,dx = [-1,1,0,0],[0,0,-1,1]

def bfs(sty,stx, edy,edx):
    q = deque()
    q.append((sty,stx))
    visited=[[0]*c for _ in range(r)]
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<r and 0<=nx<c:
                if arr[ny][nx]!='x' and not visited[ny][nx]:
                    visited[ny][nx] = visited[y][x]+1
                    if ny==edy and nx==edx:
                        return visited[ny][nx]
                    q.append((ny,nx))


r,c = map(int,input().split())
arr=[list(input().split()) for _ in range(r)]

path = [0]*3
result = 0
for i in range(r):
    for j in range(c):
        if arr[i][j]=='S':
            path[0]=(i,j)
        if arr[i][j]=='C':
            path[1]=(i,j)
        if arr[i][j]=='D':
            path[2]=(i,j)

for i in range(2):
    arr[path[i][0]][path[i][1]]=0
    result+=bfs(path[i][0],path[i][1],path[i+1][0],path[i+1][1])

print(result)
"""
"""
# 8 섬찾아 삼만리

from collections import deque
dy,dx = [-1,1,0,0],[0,0,-1,1]

def bfs(y,x):
    q = deque()
    q.append((y,x))
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<r and 0<=nx<c:
                if arr[ny][nx]==1:
                    arr[ny][nx]=0
                    q.append((ny,nx))
    return 1


r,c = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(r)]
result = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] == 1:
            arr[i][j] = 0
            bfs(i,j)
            result+=1
print(result)
"""