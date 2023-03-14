from collections import deque

dy,dx =[-1,1,0,0],[0,0,-1,1]
dh=[1,-1]

def bfs(y,x,h):
    q = deque([[y,x]])
    rlt = -1
    while q:
        y,x = q.popleft()
        for i in range(h):
            # 같은 층의 토마토가 익는 것
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

    return rlt


n,m,h = map(int,input().split())
arr = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[0]*m for _ in range(n)] for _ in range(h)]

rlt = bfs(f,i,j)
print(rlt)



