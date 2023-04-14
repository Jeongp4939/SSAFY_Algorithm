"""
# 폭탄 투하 장소 선정
def dfs(bomb=0,cnt=0,target=[]):
    global Max, result
    if bomb==n:
        if cnt>Max:
            Max=cnt
            result = target[:]
        return
    for i in range(4):
        for j in range(4):
            if arr[i][j] != '_' and not visited[i][j]:
                tcnt = 0
                temp =[]
                for d in range(5):
                    ny = i + dy[d]
                    nx = j + dx[d]
                    if 0<=ny<4 and 0<=nx<4:
                        if arr[ny][nx] != '_' and not visited[ny][nx]:
                            visited[ny][nx]=1
                            tcnt+=1
                            temp.append((ny,nx))
                dfs(bomb+1, cnt+tcnt, target+[arr[i][j]])
                for t in temp:
                    visited[t[0]][t[1]]=0


arr = [input() for _ in range(4)]
visited = [[0]*4 for _ in range(4)]
dy,dx = [-1,1,0,0,0],[0,0,-1,1,0]
n = int(input())
Max = 0
result = []
dfs()
print(*sorted(result))
"""
"""
# 독수리 3형제
#
# visited 가 0이면 sum에 food[i]*2**depth를 더해주고
# visited 가 1이면 sum에 0을 더함

def dfs(depth,Sum=0):
    # 3마리 독수리가 먹이를 먹었다면 return
    if depth ==3:
        return

    # 6칸의 먹이
    for j in range(6):
       pass

def dfs(depth=0, bd=0, Sum=0):
    global Max
    # 독수리 3마리 -> 총 n*2번 먹이를 먹음
    if depth == n*3:
        Max = max(Max,Sum)
        return
    for i in bird[bd]:
        if not visited[i]:
            visited[i]=1
            # 독수리 인덱스를 다음으로 넘겨주면서 진행
            # 먹이는 현재 음식의 값 * 2**(먹이를 먹은 사이클의 수)
            dfs(depth+1, (bd+1)%3,Sum+food[i]*(2**(depth//3)))
            visited[i]=0
        else:
            # 먹이를 먹었던 곳이면 0이므로 +0
            dfs(depth+1, (bd+1)%3, Sum+0)


bird = {0:[0,1,2],1:[3,4,5],2:[1,2,3,4]}
food = list(map(int,input().split()))
visited=[0]*6
Max=0
n = int(input())
dfs()
print(Max)
"""
# 디자이너의 손길
#
# def score_calc(s:str)->int:
#     ln = len(s)
#     score = 0
#     for i in range(1,ln):
#         if s[i-1]==s[i]:
#             score-=50
#         elif abs(ord(s[i-1])-ord(s[i]))<=5:
#             score+=3
#         elif abs(ord(s[i-1])-ord(s[i]))>=20:
#             score+=10
#     return score
#
# def swap_str(depth:int, strlen:int, S:str):
#     global Max
#     if depth==n:
#         Max = max(Max,score_calc(S))
#         return
#     for i in range(strlen):
#         for j in range(i+1,strlen):
#             swap_str(depth+1, strlen, S[:i]+S[j]+S[i+1:j]+S[i]+S[j+1:])
#
# st= input()
# st_len = len(st)
# n = int(input())
# Max = 0
# swap_str(0,st_len,st)
#
# print(Max)
