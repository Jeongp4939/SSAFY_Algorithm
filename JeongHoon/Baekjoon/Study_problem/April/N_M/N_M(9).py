def dfs(depth,ans=[]):
    if depth == M:
        if tuple(ans) not in ans_set:
            ans_set.add(tuple(ans))
            print(*ans)
        return
    for i in range(N):
        if not used[i]:
            used[i]=1
            dfs(depth+1,ans+[lst[i]])
            used[i]=0


N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
used=[0]*N
ans_set = set()
dfs(0)