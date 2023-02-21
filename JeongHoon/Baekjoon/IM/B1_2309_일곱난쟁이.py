# https://www.acmicpc.net/problem/2309

# 아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다.
# 주어지는 키는 100을 넘지 않는 자연수이며,
# 아홉 난쟁이의 키는 모두 다르며,
# 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다.

lst = [int(input()) for _ in range(9)]

lst.sort()

over = sum(lst) - 100   # 100보다 얼마나 커졌는지 확인
i = 0
j = 8

while i<j:  # 투포인터를 사용하여 두 수의 합이 over와 같은 수 찾기
    if lst[i]+lst[j] <over:
        i+=1
    elif lst[i]+lst[j]>over:
        j-=1
    else:
        a,b = lst[i],lst[j]
        lst.remove(a)
        lst.remove(b)
        break
for i in lst:
    print(i)



