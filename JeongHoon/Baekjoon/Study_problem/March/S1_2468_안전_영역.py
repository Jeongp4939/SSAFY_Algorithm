# from collections import deque
#
# dy,dx = [-1,1,0,0],[0,0,-1,1]
# n = int(input())
# arr = [list(map(int,input().split())) for _ in range(n)]
# rlt = 0
#
# for h in range(101):
#     visited = [[0] * n for _ in range(n)]
#     cnt=0
#     for i in range(n):
#         for j in range(n):
#             # 방문한 적 없고, 물의 높이보다 높은 곳 찾기
#             if arr[i][j]>h and not visited[i][j]:
#                 cnt+=1
#                 # bfs 실행
#                 q = deque([[i,j]])
#                 while q:
#                     y,x = q.popleft()
#                     for d in range(4):
#                         ny = y + dy[d]
#                         nx = x + dx[d]
#                         if 0<=ny<n and 0<=nx<n:
#                             # 상하좌우로 피신 가능한 지점 탐색
#                             # 높은 곳만 1 표시
#                             if not visited[ny][nx]:
#                                 if arr[ny][nx]>h:
#                                     visited[ny][nx] = 1
#                                     q.append([ny,nx])
#     # 피신 가능한 지점들에서만 bfs 실행하며 체크했으므로
#     # cnt는 가능한 지점(덩어리)의 수
#     # 덩어리가 rlt보다 클 경우에만 갱신
#     rlt=max(cnt,rlt)
# print(rlt)

# 물의 높이 0일때를 고려 안했다가 틀림
# 처음 for문의 range를 1~101으로 했었는데 0부터로 바꾸고 해결


from collections import deque

dy,dx = [-1,1,0,0],[0,0,-1,1]
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
rlt = 0

def bfs(y,x):
    q = deque([[y, x]])
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < n and 0 <= nx < n:
                # 상하좌우로 피신 가능한 지점 탐색
                # 높은 곳만 1 표시
                if not visited[ny][nx]:
                    if arr[ny][nx] > h:
                        visited[ny][nx] = 1
                        q.append([ny, nx])
    return cnt

for h in range(101):
    visited = [[0] * n for _ in range(n)]
    cnt=0
    for i in range(n):
        for j in range(n):
            # 방문한 적 없고, 물의 높이보다 높은 곳 찾기
            if arr[i][j]>h and not visited[i][j]:
                cnt+=1
                # bfs 실행
                bfs(i,j)
    # 피신 가능한 지점들에서만 bfs 실행하며 체크했으므로
    # cnt는 가능한 지점(덩어리)의 수
    # 덩어리가 rlt보다 클 경우에만 갱신
    rlt=max(cnt,rlt)
print(rlt)

# 함수로 따로 제작해서 실행 시 실행시간 많이 줄어듦