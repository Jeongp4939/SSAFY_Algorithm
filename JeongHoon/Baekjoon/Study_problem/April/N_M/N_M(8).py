def dfs(depth,idx=0,ans=[]):
    if depth == M:
        print(*ans)
        return
    for i in range(idx,N):
        dfs(depth+1,i,ans+[lst[i]])

N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
dfs(0)