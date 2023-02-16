# https://www.acmicpc.net/problem/2018
# 어떤 자연수 N(1 ≤ N ≤ 10,000,000)에 대해서,
# 이 N을 몇 개의 연속된 자연수의 합으로 나타내는 가지수

# 연속된 자연수의 합 -> 구간 합 or 투포인터


N = int(input())
sum=1
cnt=1
st=ed=1

while ed!=N:
    if sum<N:
        ed+=1
        sum+=ed
    elif sum==N:
        ed+=1
        sum+=ed
        cnt+=1
    else:
        sum-=st
        st+=1
print(cnt)



