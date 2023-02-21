n = int(input())

lst = list(map(int,input().split()))
i=1
cnt = 1
Max = 0
flag = 0
while i<n:
    if lst[i-1]<=lst[i]:
        cnt+=1
        i+=1
        if cnt>Max:
            Max=cnt
    else:
        cnt = 1
        i+=1
i=1
cnt=1
while i<n:
    if lst[i-1] >= lst[i]:
        cnt += 1
        i += 1
        if cnt > Max:
            Max = cnt
    else:
        cnt = 1
        i+=1
if len(lst)==1:
    print(1)
else:
    if Max==1:
        print(2)
    else:
        print(Max)