# 마일리지 최대치 36

n, m = map(int,input().split())
needs =[0]*n

for i in range(n*2):
    if i%2==0:
        # p = 신청자, l=수강인원
        p,l = map(int,input().split())
    else:
        # 마일리지 투입 수를 내림차순으로 정렬
        mileage = sorted([*map(int,input().split())], reverse=True)
        # 신청한 인원이 수강인원보다 적다면 1의 마일리지만 넣으면 됨
        if len(mileage) < l:
            needs[i//2] = 1
        # 신청한 인원이 수강인원보다 크거나 같으면 가장 말석에 있는 사람의 마일리지와 동일한 마일리지 투입
        # 마일리지가 같다면 우선순위가 성준이에게 있다라는 조건
        else:
            needs[i//2] = mileage[l-1]

needs.sort()
result = 0
Sum = 0
for j in needs:
    if Sum + j <= m:
        Sum+=j
        result+=1

print(result)
