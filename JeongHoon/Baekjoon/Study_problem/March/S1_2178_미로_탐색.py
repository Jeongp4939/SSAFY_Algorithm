# https://www.acmicpc.net/problem/2178
# flood fill algorithm을 이용해 풀면 쉽게 해결 가능

from collections import deque

n,m = map(int,input().split())
arr = [list(map(int,list(input()))) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

dy,dx = [-1,1,0,0],[0,0,-1,1]

y=x=0
flag = 0
visited[0][0]=1
q = deque()
q.append([y,x])
while q:
    y,x = q.popleft()
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        # 방향별로 갈 수 있는 방향을 확인
        if 0<=ny<n and 0<=nx<m:
            if not visited[ny][nx] and arr[ny][nx]:
                # 간 적 없으면서, 갈 수 있는 길이면 왔던 길의 숫자 + 1
                visited[ny][nx]=visited[y][x]+1
                q.append([ny,nx])
            if ny==n-1 and nx==m-1:
                flag=1
    if flag:
        break

print(visited[n-1][m-1])
