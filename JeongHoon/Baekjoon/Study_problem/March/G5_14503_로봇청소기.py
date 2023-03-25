# https://www.acmicpc.net/problem/14503

# 원래 지문
# https://web.archive.org/web/20210124122312/https://www.acmicpc.net/problem/14503

# 북, 동, 남, 서
direct = [(-1,0),(0,1),(1,0),(0,-1)]

def clean(y,x,d,cnt=0):
    # 청소 안된 칸이면 청소
    if not arr[y][x] and not visited[y][x]:
        visited[y][x] = 1
        cnt+=1
    for _ in range(4):
        d = (d-1)%4
        ny = y + direct[d][0]
        nx = x + direct[d][1]
        if 0<=ny<N and 0<=nx<M:
            if not arr[ny][nx] and not visited[ny][nx]:
                # 방문한 곳이 아니면 청소 진행
                return clean(ny,nx,d,cnt)
    if not arr[y+direct[(d+2)%4][0]][x+direct[(d+2)%4][1]]:
        return clean(y+direct[(d+2)%4][0],x+direct[(d+2)%4][1],d,cnt)
    else:
        return cnt

N,M = map(int,input().split())
y,x,d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
rlt = clean(y,x,d)
print(rlt)

