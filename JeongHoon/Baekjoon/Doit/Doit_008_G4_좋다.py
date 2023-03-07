# https://www.acmicpc.net/problem/1253

# 첫째 줄에는 수의 개수 N(1 ≤ N ≤ 2,000),
# 두 번째 줄에는 i번째 수를 나타내는 Ai가 N개 주어진다.
# (|Ai| ≤ 1,000,000,000, Ai는 정수) -> 음수도 포함되어 있을 수 있다

N = int(input())
A = list(map(int,input().split()))
A.sort()        # 투포인터를 사용하기 위해 정렬

cnt = 0

for n in range(N):
    f = A[n]
    i = 0
    j = N-1

    while i<j:
        if A[i]+A[j] == f:   # 두 포인터의 합이 일치할 때
            if i != n and j != n:
                cnt += 1
                break       # 좋은수라면 while문 탈출
            elif i == n:
                i += 1      # 본인을 제외해야 하므로 이동
            elif j == n:
                j -= 1      # 본인을 제외해야 하므로 이동
        elif A[i]+A[j] < f:
            i+=1
        else:
            j-=1

print(cnt)