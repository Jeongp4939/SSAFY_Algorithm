# https://www.acmicpc.net/problem/1697

from collections import deque
D = [0]*100001

def bfs(n):
    q = deque()
    q.append(n)
    D[n]=1
    while q:
        n = q.popleft()
        dd = [1, -1, n]
        for i in range(3):
            nn = n+dd[i]
            if 0<=nn<100001:
                if not D[nn]:
                    D[nn] = D[n]+1
                    q.append(nn)
                if nn==k:
                    return D[nn]-1

n,k = map(int,input().split())
print(bfs(n))