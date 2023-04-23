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

# 2 Graph 순회
def preorder():
    return

def postorder():
    return

N,M = map(int,input().split())
graph = [[]*(N+1)]
st_node = int(input())
for _ in range(M):
    st,ed = map(int,input().split())
    graph[st].append(ed)
    graph[ed].append(st)


    