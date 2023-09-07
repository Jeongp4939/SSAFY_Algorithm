n,m = map(int,input().split())

node = [[] for _ in range(n+1)]

def dfs(s,e,dist=0):
    global Min
    if dist>=Min:
        return
    if s==e:
        Min = min(Min,dist)
        return
    for ne,nd in node[s]:
        if not visited[ne]:
            visited[ne]=1
            dfs(ne,e,dist+nd)

for _ in range(n-1):
    s,e,d = map(int,input().split())
    node[s].append((e,d))
    node[e].append((s,d))

for _ in range(m):
    Min = 10e9
    visited = [0] * (n + 1)
    s,e = map(int,input().split())
    visited[s]=1
    dfs(s,e)
    print(Min)