def dfs(depth,idx=1,ans=[]):
    if depth == M:
        print(*ans)
        return
    for i in range(idx,N+1):
        dfs(depth+1,i+1,ans+[i])

N,M = map(int,input().split())
dfs(0)

