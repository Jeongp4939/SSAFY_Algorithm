s = input()

a, d = [], []
for i in range(len(s)):
    if s[i].isalpha():
        a.append(s[i])
    else: # s[i].isdigit()
        d.append(s[i])

a.sort() # 문자 정렬(오름차순)

sum = 0 # 숫자 덧셈
for i in range(len(d)):
    sum += int(d[i])

a.append(str(sum)) # 1. 문자 변환 2. list 추가

for i in range(len(a)):
    print(a[i], end='')
print()