# https://www.acmicpc.net/problem/11003
# N개의 수 A1, A2, ..., AN과 L이 주어진다.
# Di = Ai-L+1 ~ Ai 중의 최솟값이라고 할 때,
# D에 저장된 수를 출력하는 프로그램을 작성하시오.
# 이때, i ≤ 0 인 Ai는 무시하고 D를 구해야 한다.
from collections import deque

n,l = map(int,input().split())
A = list(map(int,input().split()))
q = deque()

for i in range(n):
    # 덱에 새로운 값이 들어올 때 들어오는 수보다 큰 수를 덱에서 제거
    while q and q[-1][0] > A[i]:
        q.pop()
    q.append((A[i], i))
    # 범위에서 벗어난 값은 제거(슬라이딩 윈도우)
    if q[0][1] <= i-l:
        q.popleft()
    print(q[0][0], end=' ')
