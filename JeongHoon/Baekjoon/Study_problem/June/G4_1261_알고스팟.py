import sys
sys.setrecursionlimit(100000)

dy,dx = (1,0,-1,0),(0,1,0,-1)
def dfs(y,x,cnt=0,depth=0):
    global Min
    if cnt>=Min or depth>=m*n:
        return
    if y==n-1 and x==m-1:
        Min = min(Min,cnt)
        return
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=ny<n and 0<=nx<m:
            if visited[ny][nx]==0:
                visited[ny][nx] = 1
                if arr[ny][nx]==0:
                    dfs(ny,nx,cnt,depth+1)
                else:
                    dfs(ny,nx,cnt+1,depth+1)
                visited[ny][nx]=0

m,n = map(int,input().split())
arr = [list(map(int,list(input()))) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
visited[0][0]=1
Min = 10e10
dfs(0,0)
print(Min)
