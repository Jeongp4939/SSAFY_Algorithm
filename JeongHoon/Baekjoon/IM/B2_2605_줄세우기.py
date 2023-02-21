# https://www.acmicpc.net/problem/2605

# 첫 번째 학생이 번호를 뽑은 후 : 1
# 두 번째 학생이 번호를 뽑은 후 : 2 1
# 세 번째 학생이 번호를 뽑은 후 : 2 3 1
# 네 번째 학생이 번호를 뽑은 후 : 4 2 3 1
# 다섯 번째 학생이 번호를 뽑은 후 : 4 2 5 3 1

n = int(input())
lst=[]
a = list(map(int,input().split()))
for i in range(1,n+1):

    if not lst:
        lst.append(i)
    else:
        lst.insert(len(lst)-a[i-1],i)
print(*lst)

