s = input()
i = 0

numbers = []
# 숫자와 연산자 나누기
while len(s)>i:
    if s[i]=='+' or s[i]=='-':
        numbers.append(int(s[:i]))
        s = s[i:]
        i=0
    if i==len(s)-1:
        numbers.append(int(s))
    i+=1

answer = 0
flag_minus=0

for i in numbers:
    if i<0:
        answer+=i
        flag_minus=1
    elif i>0 and flag_minus:
        answer-=i
    elif i>0 and not flag_minus:
        answer+=i

print(answer)