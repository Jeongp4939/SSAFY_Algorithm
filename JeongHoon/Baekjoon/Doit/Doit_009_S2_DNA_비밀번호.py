# https://www.acmicpc.net/problem/12891

d = {'A':0,'C':1,'G':2,'T':3}

s, p = map(int,input().split())
st = input()
check = list(map(int,input().split()))
S=[0]*4
rlt = 0
cnt = 0

for i in st[:p]:    # S 초기값
    S[d[i]]+=1

for j in range(4):
    if S[j] >= check[j]:
        cnt+=1
if cnt==4:
    rlt+=1

for i in range(1,s-p+1):
    cnt = 0
    S[d[st[i-1]]]-=1
    S[d[st[i+p-1]]]+=1
    for j in range(4):
        if S[j] >= check[j]:
            cnt+=1
    if cnt==4:
        rlt+=1
print(rlt)

