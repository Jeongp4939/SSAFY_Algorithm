def dfs(depth,idx,ans=[]):
    if depth == M:
        if tuple(ans) not in ans_set:
            ans_set.add(tuple(ans))
            print(*ans)
        return
    for i in range(idx,N):
        dfs(depth+1,i+1,ans+[lst[i]])

N,M = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
ans_set = set()
dfs(0,0)