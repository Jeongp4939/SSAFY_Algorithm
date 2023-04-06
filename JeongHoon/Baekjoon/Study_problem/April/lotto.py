def dfs(lv=0, nums=[]):
    if lv==6:
        if tuple(sorted(nums)) not in n_set:
            n_set.add(tuple(sorted(nums)))
            print(*nums)
        return

    for i in range(n):
        if not used[i]:
            used[i]=1
            dfs(lv+1,nums+[lst[i]])
            used[i]=0


while 1:
    n,*lst = map(int,input().split())
    if n==0:
        break
    used=[0]*n
    n_set=set()
    dfs()
    print()