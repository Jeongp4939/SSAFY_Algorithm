def bfs(y,x,t):
    q = [(y,x)]
    visited[y][x]=1
    cnt=1
    while q:
        ny,nx = q.pop(0)
        for i,j in ((1,0),(-1,0),(0,1),(0,-1)):
            dy = ny+i
            dx = nx+j
            if 0<=dy<n and 0<=dx<m:
                if not visited[dy][dx] and arr[dy][dx]==t:
                    visited[dy][dx] = 1
                    cnt+=1
                    q.append((dy,dx))
    return cnt

m,n = map(int,input().split())

arr = [input() for _ in range(n)]
visited = [[0]*m for _ in range(n)]
tw=[]
tb=[]

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if arr[i][j]=='W':
                tw.append(bfs(i,j,'W')**2)
            else:
                tb.append(bfs(i,j,'B')**2)

print(sum(tw),sum(tb))