def dfs(depth,idx=0,ans=[]):
    if depth == M:
        print(*ans)
        return
    for i in range(idx,N):
        if not used[i]:
            used[i]=1
            dfs(depth+1,i+1,ans+[lst[i]])
            used[i]=0

N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
used = [0]*N
dfs(0)