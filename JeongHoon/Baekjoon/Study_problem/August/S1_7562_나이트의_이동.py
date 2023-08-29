from collections import deque

dy = (-2,-2,2,2,-1,-1,1,1)
dx = (-1,1,-1,1,-2,2,-2,2)

tc = int(input())

for t in range(tc):
    # 판의 크기
    n = int(input())
    # 시작 지점
    visited = [[0]*n for _ in range(n)]

    def bfs_knight(st,tg):
        q = deque()
        q.append(st)

        while q:
            y, x = q.popleft()

            for i in range(8):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <=ny<n and 0<=nx<n:
                    if visited[ny][nx] == 0:
                        visited[ny][nx]=visited[y][x]+1
                        if ny==tg[0] and nx==tg[1]:
                            return visited[ny][nx]
                        q.append((ny,nx))

    start = tuple(map(int,input().split()))
    # 도착하기 위한 지점
    target = tuple(map(int, input().split()))

    if start==target:
        print(0)
    else:
        print(bfs_knight(start,target))
