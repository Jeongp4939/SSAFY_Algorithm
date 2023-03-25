# https://www.acmicpc.net/problem/9205

# T <= 50, 0<=n<=100, -32768 <= x,y <= 32767
# 맨해튼거리(x값+y값 으로 거리를 계산)

from collections import deque
def bfs(st, ed):
    q = deque()
    q.append(st)
    visited[st]=1
    while q:
        st = q.popleft()
        for i in range(1,n+2):
            if visited[i]:continue
            if abs(A[i][0]-A[st][0])+abs(A[i][1]-A[st][1]) <=1000:
                visited[i] = 1
                q.append(i)
                if i==ed:
                    return 'happy'
    return 'sad'

# 테스트 케이스의 수
T = int(input())
for _ in range(T):
    # 맥주의 개수/ 50미터에 1개 -> 20개 1000미터
    n = int(input())
    # 좌표값 n+2개 저장 / 0번 인덱스는 집 n+1번 인덱스는 페스티벌
    A = [list(map(int,input().split())) for _ in range(n+2)]
    visited = [0]*(n+2)

    result = bfs(0,n+1)
    print(result)

