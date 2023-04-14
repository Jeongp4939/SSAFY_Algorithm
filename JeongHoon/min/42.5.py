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

bird = {0:[0,1,2],1:[3,4,5],2:[1,2,3,4]}
food = list(map(int,input().split()))
visited=[0]*6
Max=0
n = int(input())
result = 0

for i in range(n):
    dfs()

