# from collections import deque
#
# dy,dx = (-1,1,0,0),(0,0,-1,1)
# def bfs(time,ty,tx):
#     cnt = 0
#     while q and time>cnt:
#         y,x = q.popleft()
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if 0<=ny<N and 0<=nx<N:
#                 if arr[ny][nx]==0:
#                     arr[ny][nx]=arr[y][x]
#                     q.append((ny,nx))
#         if  arr[y][x] == K and arr[q[0][0]][q[0][1]]==1:
#             cnt+=1
#
#     return arr[ty][tx]
#
#
# N,K = map(int,input().split())
# arr = [list(map(int,input().split())) for _ in range(N)]
# S, Y, X = map(int,input().split())
# q = deque()
#
# for i in range(1,K+1):
#     for j in range(N):
#         for k in range(N):
#             if arr[j][k] == i:
#                 q.append((j,k))
# print(bfs(S,Y-1,X-1))


from collections import deque

dy,dx = (-1,1,0,0),(0,0,-1,1)
def bfs(time,ty,tx):
    cnt = 0
    while q and time>cnt:
        _, y,x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<N:
                if arr[ny][nx]==0:
                    arr[ny][nx]=arr[y][x]
                    q.append((_,ny,nx))
        if arr[y][x] == K and arr[q[0][1]][q[0][2]]==1:
            cnt+=1
    return arr[ty][tx]


N,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
S, Y, X = map(int,input().split())
q = []

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            q.append((arr[i][j],i,j))
q.sort()
q = deque(q)

print(bfs(S,Y-1,X-1))