def calc(left,right,i):
    if i == 0:
        return left+right
    elif i == 1:
        return left-right
    elif i == 2:
        return left*right
    else:
        return int(left/right)


def dfs(now, rlt):
    global MAX, MIN
    if now > n-2:
        MAX = max(MAX,rlt)
        MIN = min(MIN,rlt)
        return

    for i in range(4):
        if i==3 and lst[now+1]==0:
            continue
        if op[i]:
            tmp = rlt
            op[i]-=1
            rlt = calc(rlt,lst[now+1], i)
            dfs(now+1, rlt)
            op[i]+=1
            rlt = tmp

n = int(input())
lst = list(map(int,input().split()))
op = list(map(int,input().split()))

MIN = 1e9
MAX = -1e9

dfs(0,lst[0])


print(int(MAX))
print(int(MIN))