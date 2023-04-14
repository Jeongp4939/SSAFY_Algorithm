

dy,dx = [-1,1,0,0],[0,0,1,-1]

def dfs(start:tuple, path:list, S:str, cnt=1,):
    global ans

    # Y의 수가 많아지면 종료
    if S.count('Y')>=4:
        return
    # 경로 set에 해당 경로가 존재하면 리턴
    # 없으면 경로에 추가
    if tuple(path) in path_set:
        return
    else:
        path_set.add(tuple(path))

    # 7개의 지점을 방문했을 때 개수를 세고
    # 조건에 부합하면 ans+=1
    if cnt==7:
        if S.count('S') >= S.count('Y'):
            ans+=1
        return

    # path 내부에 있는 지점들에서 새로운 탐색 시작
    for i in path:
        y,x = i
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0<=ny<5 and 0<=nx<5:
                if visited[ny][nx]==0:
                    visited[ny][nx]=1
                    dfs((ny,nx),sorted(path+[(ny,nx)]), S+arr[ny][nx], cnt+1)
                    visited[ny][nx]=0

arr = [input() for _ in range(5)]
path_set = set()
ans = 0

for i in range(5):
    for j in range(5):
        visited=[[0]*5 for _ in range(5)]
        path = [(i,j)]
        visited[i][j]=1
        dfs((i,j), path, arr[i][j])

print(ans)