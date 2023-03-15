# https://www.acmicpc.net/problem/2667
# 교수님이 수업시간에 내주었던 섬 문제와 비슷한 문제
# visited 행렬을 만들고, 이를 이용해 각 단지의 수를 파악
# BFS로 해결

from collections import deque
dy,dx = [-1,1,0,0],[0,0,-1,1]

def bfs(y,x):
    cnt=1
    q=deque()
    q.append([y,x])
    visited[y][x]=1
    while q:
        y,x = q.popleft()
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if 0<=ny<n and 0<=nx<n:
                if arr[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx]=1
                    cnt+=1
                    q.append([ny,nx])
    return cnt

def dfs(y,x,cnt=1):
    stack = [(y,x)]
    visited[y][x] = 1
    while stack:
        y,x = stack.pop()
        for i in range(4):
            ny,nx = y+dy[i],x+dx[i]
            if 0<=ny<n and 0<=nx<n:
                if arr[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx]=1
                    cnt+=1
                    stack.append([ny,nx])
    return cnt


n = int(input())
arr = [list(map(int,list(input()))) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
cnts=[]
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] and not visited[i][j]:
#             cnts.append(bfs(i,j))

for i in range(n):
    for j in range(n):
        if arr[i][j] and not visited[i][j]:
            cnts.append(dfs(i,j))

cnts.sort()
print(len(cnts))
for i in cnts:
    print(i)

