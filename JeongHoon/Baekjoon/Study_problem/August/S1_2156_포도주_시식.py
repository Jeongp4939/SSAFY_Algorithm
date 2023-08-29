# 포도주 잔을 선택하면 다 마시고, 제 자리에 놓음
# 연속으로 3잔을 마실 수 없음

# 마시는 경우
# 0-> 첫 한잔
# d[1] -> 0,1번 째 잔
# d[2] -> 0,1 또는 1,2 또는 0,2 중 가장 큰 값
# d[2] = max(d[1], wine[1]+wine[2], d[0]+wine[2])
# d[i] = max(d[i-1], d[i-3]+wine[i-1]+wine[i] ,d[i-2]+wine[i])

n = int(input())
wine = []

for i in range(n):
    wine.append(int(input()))

d = [0]*n

d[0] = wine[0]
if n>1:
    d[1] = wine[0]+wine[1]
if n>2:
    d[2] = max(wine[2]+wine[1], wine[2]+wine[0], d[1])

for i in range(3,n):
    d[i] = max(d[i-1], d[i-3]+wine[i-1]+wine[i], d[i-2]+wine[i])

print(d[n-1])



