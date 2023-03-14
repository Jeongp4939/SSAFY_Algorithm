# https://www.acmicpc.net/problem/1987

# 세로 R칸, 가로 C칸으로 된 표 모양의 보드가 존재
# 1행 1열에 말이 놓여 있다.
# 시간초과 심하게 남
# in을 썼을 때 시간 복잡도가 증가하는거 같음
# pypy3로 제출 했을 때 통과는 했지만, 5000ms 걸림
# 재귀가 문제일 가능성

dy,dx = [-1,1,0,0],[0,0,-1,1]
# 처음 말이 놓여진 위치도 카운트 해야하므로 1로 시작
def dfs(y,x,cnt=1):
    global Max
    # dfs가 진행되며 cnt가 Max보다 높아지면 Max에 cnt를 저장
    Max=max(Max,cnt)
    if Max==26:
        return
    # ASCII 번호를 이용해서 visited의 방문 체크
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=ny<n and 0<=nx<m:
            if visited[ord(arr[ny][nx])-ord('A')]:continue
            visited[ord(arr[ny][nx])-ord('A')]=1
            dfs(ny,nx,cnt+1)
            visited[ord(arr[ny][nx])-ord('A')]=0


n,m = map(int,input().split())
arr=[list(input()) for _ in range(n)]
# 알파벳의 수만큼 visited 리스트 생성
visited=[0]*(26)
#시작점은 체크하고 시작
visited[ord(arr[0][0])-ord('A')] = 1
Max=0
dfs(0,0)
print(Max)

# import sys
# input = sys.stdin.readline
#
# dy,dx = [-1,1,0,0],[0,0,-1,1]
# # 처음 말이 놓여진 위치도 카운트 해야하므로 1로 시작
# def dfs(y,x,cnt=1):
#     global Max
#     # dfs가 진행되며 cnt가 Max보다 높아지면 Max에 cnt를 저장
#     Max=max(Max,cnt)
#     # ASCII 번호를 이용해서 visited의 방문 체크
#     for i in range(4):
#         ny=y+dy[i]
#         nx=x+dx[i]
#         if 0<=ny<n and 0<=nx<m:
#             if arr[ny][nx] in visited:continue
#             visited.add(arr[ny][nx])
#             dfs(ny,nx,cnt+1)
#             visited.remove(arr[ny][nx])
#
#
# n,m = map(int,input().split())
# arr=[list(input()) for _ in range(n)]
# # visited set 생성
# visited = set()
# visited.add(arr[0][0])
# Max=0
# dfs(0,0)
# print(Max)

