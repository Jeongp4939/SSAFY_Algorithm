def dfs(depth,ans=[]):
    if depth == M:
        print(*ans)
        return
    for i in range(1,N+1):
        dfs(depth+1,ans+[i])

N,M = map(int,input().split())
dfs(0)