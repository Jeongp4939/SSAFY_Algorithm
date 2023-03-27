# https://www.acmicpc.net/problem/13023

def dfs(node,depth=1):
    global flag

    if depth==5:
        flag=1
        return
    visited[node] = 1
    for i in A[node]:
        if not visited[i]:
            dfs(i,depth+1)
    visited[node]=0


n,m = map(int,input().split())
A = [[] for _ in range(n+1)]
visited = [0]*(n+1)
flag=0
for _ in range(m):
    s,e = map(int,input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(n):
    dfs(i)
    if flag:
        break
if flag:
    print(1)
else:
    print(0)