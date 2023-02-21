# https://www.acmicpc.net/problem/14696

# 만약 두 딱지의 별의 개수가 다르다면, 별이 많은 쪽의 딱지가 이긴다.
# 별의 개수가 같고 동그라미의 개수가 다르다면, 동그라미가 많은 쪽의 딱지가 이긴다.
# 별, 동그라미의 개수가 각각 같고 네모의 개수가 다르다면, 네모가 많은 쪽의 딱지가 이긴다.
# 별, 동그라미, 네모의 개수가 각각 같고 세모의 개수가 다르다면, 세모가 많은 쪽의 딱지가 이긴다.
# 별, 동그라미, 네모, 세모의 개수가 각각 모두 같다면 무승부이다.
# 별, 동그라미, 네모, 세모를 각각 숫자 4, 3, 2, 1로 표현
# A가 승자라면 A, B가 승자라면 B, 무승부라면 D

n = int(input())

for _ in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    da = {4:0,3:0,2:0,1:0}
    db = {4:0,3:0,2:0,1:0}

    for i in a[1:]:
        da[i]+=1
    for i in b[1:]:
        db[i]+=1

    cnt = 0
    flag = False
    for key in da.keys():
        if da[key]>db[key]:
            print('A')
            flag=True
            break
        elif da[key]<db[key]:
            print('B')
            flag = True
            break
        else:
            cnt+=1
    if not flag and cnt==4:
        print('D')


