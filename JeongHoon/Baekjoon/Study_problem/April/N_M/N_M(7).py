def dfs(depth,ans=[]):
    if depth == M:
        print(*ans)
        return
    for i in range(N):
        dfs(depth+1,ans+[lst[i]])

N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
dfs(0)