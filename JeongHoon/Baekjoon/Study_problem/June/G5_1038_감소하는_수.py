def dfs(depth, num=[]):

    if depth==10:
        return
    if ''.join(sorted(num, reverse=True)) not in S:
        S.add(''.join(sorted(num, reverse=True)))

    for i in range(10):
        if not used[i]:
            used[i]=1
            dfs(depth,num+[str(i)])
            used[i]=0

N = int(input())
used = [0]*10
S = set()
dfs(0)
result = sorted(list(S))
print(result(N))