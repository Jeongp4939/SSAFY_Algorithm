N, K = map(int,input().split())
lst = list(map(int, input().split()))
result = [0]*(N-K+1)

for i in range(N-K+1):
    if i == 0:
        result[i] = sum(lst[i:i+K])
    else:
        result[i] = result[i-1]-lst[i-1]+lst[i+K-1]
print(max(result))