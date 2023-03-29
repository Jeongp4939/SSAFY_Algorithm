# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

def solution(maps):
    from collections import deque
    n = len(maps)
    m = len(maps[0])

    visited = [[0] * m for _ in range(n)]
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

    def bfs(y,x):
        q=deque()
        q.append((y,x))
        visited[y][x]=1
        if y == n - 1 and x == m - 1:
            return
        while q:
            y,x = q.popleft()
            for i in range(4):
                ny = y+dy[i]
                nx = x+dx[i]
                if 0<=ny<n and 0<=nx<m:
                    if maps[ny][nx] and not visited[ny][nx]:
                        visited[ny][nx]=visited[y][x]+1
                        q.append((ny,nx))
                    if ny==n-1 and nx==m-1:
                        return
    bfs(0,0)
    answer = visited[n-1][m-1]

    if answer:
        return answer
    else:
        return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))