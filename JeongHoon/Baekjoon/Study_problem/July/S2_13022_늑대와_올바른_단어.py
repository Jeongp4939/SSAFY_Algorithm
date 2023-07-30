s = list(input())
n = len(s)

def check():
    for i in range(3):
        for j in range(i+1,4):
            if cnt[i]<cnt[j] or cnt[i]>cnt[j]+1:
                return 0
    return 1


# 길이가 4의배수가 아니거나 마지막이 f가 아니라면 잘못된 단어
if len(s)%4!=0 or s[-1]!='f':
    print(0)
# 길이가 4의 배수가 맞고 f로 끝나면 전체 검사
else:
    flag=1
    cnts=[]
    cnt = 0
    tmp_cnt=1
    tmp='w'
    i = 0
    while i<n:
        if s[i] == tmp:
            cnt+=1
        else:
            tmp = s[i]
            if tmp_cnt==cnt:
                flag=0
                break
            tmp_cnt=cnt
            cnt=0
        i+=1
    print(flag)