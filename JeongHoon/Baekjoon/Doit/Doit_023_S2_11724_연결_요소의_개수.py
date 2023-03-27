# https://www.acmicpc.net/problem/11724
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,m  = map(int,input().split())
def dfs(n):
    visited[n] = 1
    for i in graph[n]:
        if not visited[i]:
            dfs(i)

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
cnt=0
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,n+1):
    if not visited[i]:
        cnt+=1
        dfs(i)

print(cnt)