from collections import deque
import sys
input = sys.stdin.readline

dy,dx = (-1,1,0,0),(0,0,-1,1)

def bfs(tup):
    q = deque()
    q.append(tup)
    visited = [[0] * m for _ in range(n)]
    visited[tup[0]][tup[1]] = 1
    while q:
        y,x = q.popleft()
        for i,j in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            ny = y + i
            nx = x + j
            if 0<=ny<n and 0<=nx<m and arr[ny][nx]=='L':
                if visited[ny][nx] == 0:
                    visited[ny][nx] = visited[y][x]+1
                    q.append((ny,nx))
    return visited[y][x]-1

n,m = map(int,input().split())
arr = [list(input()) for _ in range(n)]
MAX = 0

for i in range(n):
    for j in range(m):

        # backtracking(검색 찬스)
        if 0 < i < n - 1 and arr[i - 1][j] == 'L' and arr[i + 1][j] == 'L':
            continue
        if 0 < j < m - 1 and arr[i][j - 1] == 'L' and arr[i][j + 1] == 'L':
            continue

        if arr[i][j] == 'L':
            MAX = max(MAX,bfs((i,j)))

print(MAX)