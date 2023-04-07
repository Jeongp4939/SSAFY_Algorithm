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

bird = {0:[0,1,2],1:[3,4,5],2:[1,2,3,4]}
food = list(map(int,input().split()))
visited=[0]*6
Max=0
n = int(input())
result = 0
if n == 1:
    for i in range(3):
        idx = food.index(max(food))
        result += food[idx]
        food[idx]=0
elif n == 2:
    for i in range(3):
        idx = food.index(max(food))
        result += food[idx]
        food[idx] = 0
    result= result*2 + sum(food)
else:
    cnt=0
    # 가장 작은 값들을 처음에 추가(0도 상관 없음)
    for i in range(3):
        idx = food.index(min(food))
        result += food[idx]
        if food[idx]!=0:
            cnt+=1
        food[idx] = 0
    # 먹이 두배로 증가
    food = [x*2 for x in food]
    if cnt==2:
        Min = 1000000
        idx = 0
        for i in range(6):
            if food[i] != 0 and food[i]<Min:
                idx = i
                Min = food[i]
        result += food[idx]
        food[idx]=0
    food = [x * 2 for x in food]
    result+=sum(food)

print(result)
