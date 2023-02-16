# https://www.acmicpc.net/problem/10986

# 수 N개 A1, A2, ..., AN이 주어진다.
# 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의
# 개수를 구하는 프로그램을 작성하시오.
# 즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는
# (i, j) 쌍의 개수를 구해야 한다.

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
A = list(map(int,input().split()))
S=[0] * n
C=[0] * m
S[0]=A[0]

# mod 연산을 이용
# mod(a+b) = mod(mod(a)+mod(b))
# 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수
cnt = 0
for i in range(1,n):
    S[i] = S[i-1]+A[i]  # 합배열
for i in range(n):
    rem = S[i]%m
    if rem==0:
        cnt+=1
    C[rem]+=1

for i in C:
    cnt += (i*(i-1))//2

print(cnt)

