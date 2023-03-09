# 틀림 1 : bfs는 queue 구조인데 pop(0) 안해서 틀림
# 틀림 2 : dfs의 출력을 리턴 조건 후에 넣어서 틀림

def dfs(a):
    print(a,end=' ')
    visited[a]=1
    if not graph[a]:
        return
    for i in graph[a]:
        if not visited[i]:
            dfs(i)

def bfs(a):
    new_visited=[0]*(n+1)
    q = [a]
    print(a, end=' ')
    new_visited[a]=1
    while q:
        a = q.pop(0)
        for i in graph[a]:
            if not new_visited[i]:
                print(i,end=' ')
                new_visited[i]=1
                q.append(i)

n,e,v = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    st,ed = map(int,input().split())
    graph[st].append(ed)
    graph[ed].append(st)
for i in range(n + 1):
    graph[i] = sorted(graph[i])

visited=[0]*(n+1)
dfs(v)
print()
bfs(v)