# n <= 10^5 (N), k <= min(10^9, n^2) (N)
# 배열에 들어있는 수 A[i][j] = i×j 이다
# O(n^2) 하면 터짐 -> 100억 -> 10초 이상
# 인덱스는 1부터 -> 1~N+1
# 해당 인덱스에 해당하는 숫자

n = int(input())
k = int(input())

head = 1
tail = n*n
result = 0

if n*n == k:
    print(k)
else:
    while head < tail:
        mid = (head+tail)//2 # B[k]?
        cnt = 0

        for i in range(1,n+1):
            cnt += min(mid//i, n)

        if cnt>=k:
            tail = mid
            result = mid
        else:
            head = mid+1

    print(result)

