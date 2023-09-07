def dfs(s,e,cost=0):
    global MIN
    if s==e:
        MIN = min(MIN,cost)
        return
    for ne,nc in graph[s]:
        if not visited[ne]:
            visited[ne]=1
            dfs(e,ne,cost+nc)
            visited[ne] = 0

n,m = map(int,input().split())
graph = [[]for _ in range(n+1)]
visited = [0]*(n+1)
visited[1] = 1
MIN = 2e10

for _ in range(m):
    s,e,c = map(int,input().split())
    graph[s].append((e,c))
    graph[e].append((s,c))

dfs(1,n)

print(MIN)