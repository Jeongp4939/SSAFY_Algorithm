"""
# 1 네트워크 바이러스
def dfs(st):
    global cnt
    for i in nodes[st]:
        if not visited[i]:
            visited[i]=1
            cnt += 1
            dfs(i)


N = int(input())
nodes = [[]for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 0
M = int(input())
for _ in range(M):
    st,ed = map(int,input().split())
    nodes[st].append(ed)
    nodes[ed].append(st)
visited[1]=1
dfs(1)
print(cnt)
"""
"""
# 2 Graph 순회
def preorder(depth,st):
    if depth==N:
        return

    for i in graph[st]:
        if not visited[i]:
            visited[i]=1
            print(i, end=' ')
            preorder(depth+1, i)


def postorder(depth,st):
    if depth == N:
        return

    for i in graph[st]:
        if not visited[i]:
            visited[i] = 1
            postorder(depth + 1, i)
            print(i,end=' ')


N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
st_node = int(input())
for _ in range(M):
    st,ed = map(int,input().split())
    graph[st].append(ed)

for nodes in graph:
    nodes.sort(reverse=True)

visited = [0]*(N+1)
visited[st_node]=1
print(st_node, end=' ')
preorder(0,st_node)
print()
visited = [0]*(N+1)
visited[st_node]=1
postorder(0,st_node)
print(st_node)
"""
"""
# 크리스마스 트리

# 1 번 inorder
# 2 번 preorder
# 3 번 postorder
# 주어진 그래프는 이진 그래프이므로 코드 짜기 편함

def inorder(st):
    if graph[st][0]!=-1:
        inorder(graph[st][0])
    print(st, end = ' ')
    if graph[st][1]!=-1:
        inorder(graph[st][1])

def preorder(st):
    print(st, end = ' ')
    if graph[st][0]!=-1:
        preorder(graph[st][0])
    if graph[st][1]!=-1:
        preorder(graph[st][1])

def postorder(st):
    if graph[st][0]!=-1:
        postorder(graph[st][0])
    if graph[st][1]!=-1:
        postorder(graph[st][1])
    print(st, end=' ')

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(1,N+1):
    i, *lst = map(int,input().split())
    graph[i] = lst[:]

visited=[0]*(N+1)
inorder(1)
print()

visited=[0]*(N+1)
preorder(1)
print()

visited=[0]*(N+1)
postorder(1)
"""
"""
# 4. 럭셔리 여행
def dfs(st,ed, sum=0):
    global Max,Min
    if st == ed:
        Min = min(Min,sum)
        Max = max(Max,sum)
        return
    for i in range(N):
        if not visited[i] and arr[st][i]:
            visited[i] = 1
            dfs(i,ed, sum+arr[st][i])
            visited[i] =0

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
st, ed = map(int,input().split())
visited =[0]*N
Max = 0
Min = 28e8
visited[st]=1
dfs(st,ed)
print(Min)
print(Max)
"""
"""
# 5. 헤밀턴 회로
def dfs(now, depth=0, sum=0):
    global Min
    # N개의 노드를 방문 했을 때만 수를 확인
    if sum>=Min:
        return
    if depth==N:
        if now == 0:
            Min = min(Min,sum)
        return
    if depth < N-1:
        for i in range(1,N):
            if not visited[i] and arr[now][i]:
                visited[i] = 1
                dfs(i,depth+1, sum+arr[now][i])
                visited[i] =0
    else:
        if arr[now][0] and not visited[0]:
            dfs(0,depth+1,sum+arr[now][0])

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
visited =[0]*N
Min = 28e8
# 시작점으로 다시 돌아와야하므로 시작점의 visited를 0으로 놔둠
dfs(0)
print(Min)
"""

# 7 등수 찾기
def dfs(st,ed, depth=0):
    if st==ed or not arr[st]:
        return depth
    dfs(arr[st][0],depth+1)

n,m,x = map(int(input))
u=v=0
depth=0
arr = [[] for _ in range(n)]
for i in range(m):
    st,ed = map(int,input().split())
    arr[st].append(ed)

