# https://www.acmicpc.net/problem/5014
# 스타트링크

from collections import deque

def bfs(n):
    q = deque()
    q.append(n)
    visited=[0]*(F+2)
    visited[n]=1
    while q:
        n = q.popleft()
        for i in range(2):
            nn = n + select[i]
            if 1<=nn<F+1:
                # 방문을 안한 곳이면 visited[n]+1을 체크하고 q에 append
                if not visited[nn]:
                    visited[nn]=visited[n]+1
                    q.append(nn)

    if visited[G]:
        return visited[G]-1
    else:
        return "use the stairs"


F,S,G,U,D = map(int,input().split())
select = [U,-D]
rlt = bfs(S)
print(rlt)

