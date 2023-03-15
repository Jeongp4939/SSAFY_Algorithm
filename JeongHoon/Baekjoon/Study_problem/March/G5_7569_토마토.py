# https://www.acmicpc.net/problem/7569

# 각 지점에서 BFS flood fill 을 이용해서 채우기
# 새롭게 익은 토마토 중 숫자가 2 이상인 경우
# 다른 지점에서 시작된 익는데 필요한 기간을 비교하여
# 더 작은 숫자로 교체

# from collections import deque
#
# dy,dx =[-1,1,0,0,0],[0,0,-1,1,0]
# dh=[1,-1]
#
# def bfs(h,y,x):
#     q = deque([(y,x)])
#     rlt = -1
#     if arr[h][y][x]==0 and visited[h][y][x]==0:
#         return
#     while q:
#         y,x = q.popleft()
#         # 익은 토마토라면 실행
#         for i in range(H):
#             # 같은 층의 토마토가 익는 것
#             for i in range(5):
#                 ny = y + dy[i]
#                 nx = x + dx[i]
#                 if i==4:
#                     # 위 아래 확인
#                     for hh in range(2):
#                         nh = h+dh[hh]
#                         if 0<=nh<H:
#                             if arr[nh][y][x] == 1 or visited[nh][y][x]: continue
#                             if arr[nh][y][x] == -1: continue
#                             if arr[nh][y][x] == 0:
#                                 if visited[nh][y][x]==0:
#                                     visited[nh][y][x]= visited[h][y][x]+1
#                                 else:
#                                     visited[nh][y][x] = min(visited[nh][y][x],visited[h][y][x] + 1)
#                                 q.append((ny,nx))
#                                 rlt = max(visited[h][ny][nx], rlt)
#                 elif 0<=ny<n and 0<=nx<m:
#                     if arr[h][ny][nx] == 1 or visited[h][ny][nx]: continue
#                     if arr[h][ny][nx] == -1: continue
#                     if arr[h][ny][nx] == 0:
#                         if visited[h][ny][nx] == 0:
#                             visited[h][ny][nx] = visited[h][y][x] + 1
#                         else:
#                             visited[h][ny][nx] = min(visited[h][ny][nx], visited[h][y][x] + 1)
#                         rlt = max(visited[h][ny][nx],rlt)
#                         q.append((ny, nx))
#     return rlt
#
# m,n,H = map(int,input().split())
# arr = [[list(map(int,input().split())) for _ in range(n)] for _ in range(H)]
# visited = [[[0]*m for _ in range(n)] for _ in range(H)]
# rlt = int(28e8)
# cnt0=cnt1=cnt_minus=0
#
# for h in range(H):
#     for i in range(n):
#         for j in range(m):
#             if arr[h][i][j]==1:
#                 cnt1+=1
#                 visited[h][i][j]=1
#                 temp=bfs(h,i,j)
#                 if temp != -1:
#                     rlt = min(rlt,temp)
#             elif arr[h][i][j]==-1:
#                 cnt_minus+=1
#             else:
#                 cnt0+=1
# if cnt1+cnt_minus == H*n*m:
#     print(0)
# else:
#     flag=1
#     for h in range(H):
#         for i in range(n):
#             for j in range(m):
#                 if visited[h][i][j]==0:
#                     flag=0
#     if flag:
#         print(rlt)
#     else:
#         print(-1)


from collections import deque

dy,dx,dh =[-1,1,0,0,0,0],[0,0,-1,1,0,0],[0,0,0,0,1,-1]

def bfs(h,y,x):
    q=deque([[h,y,x]])
    visited = [[[0]*m for _ in range(n)] for _ in range(H)]
    while q:
        h,y,x = q.popleft()
        visited[h][y][x]=1
        for i in range(6):
            ny = y + dy[i]
            nx = x + dx[i]
            nh = h + dh[i]
        if 0<=ny<n and 0<=nx<m and 0<=nh<H:
            # 토마토가 존재하지 않으면 패스
            if arr[nh][ny][nx]==-1: continue
            # 시간이 지나면서 익은 토마토면 확인하기
            if not arr[nh][ny][nx] and not visited[nh][ny][nx]:
                visited[nh][ny][nx] = min(visited[nh][ny][nx],visited[h][y][x]+1)
                q.append(nh,ny,nx)
            # 익은 토마토일 때 -> visited는 0이라 생각하면 될듯
            elif arr[nh][ny][nx] and visited[nh][ny][nx]:
                pass



m, n, H = map(int, input().split())
arr = [[list(map(int,input().split())) for _ in range(n)] for _ in range(H)]
visited = [[[0]*m for _ in range(n)] for _ in range(H)]
rlt = int(28e8)
flag = 0
for h in range(H):
    if flag: break
    for i in range(n):
        if flag: break
        for j in range(m):
            if arr[h][i][j]==1:
                hh,y,x = h,i,j
                flag = 1
                break
bfs(h,y,x)



