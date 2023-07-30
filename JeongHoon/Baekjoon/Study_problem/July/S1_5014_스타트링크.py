from collections import deque

F,S,G,U,D = map(int,input().split())

def bfs(n):
    q = deque()
    q.append(n)
    visited=[0]*(F+1)
    visited[n]=1
    select = [U,-D]
    while q:
        n = q.popleft()
        for i in range(2):
            nn = n + select[i]
            if 1<=nn<F+1 and not visited[nn]:
                    visited[nn]=visited[n]+1
                    q.append(nn)

    if visited[G]:
        return visited[G]-1
    else:
        return "use the stairs"


print(bfs(S))