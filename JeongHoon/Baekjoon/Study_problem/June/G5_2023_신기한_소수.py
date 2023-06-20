def is_prime(n):
    for i in range(2,n//2):
        if not n%i:
            return 0
    return 1

def dfs(lvl=0, num=0):
    if lvl==n:
        return print(num)
    # 짝수가 뒤에 오면 소수가 아님
    for i in range(1,10):
        if lvl==0:
            if i in {2,3,5,7}:
                dfs(lvl+1,num+i)
        else:
            if i%2 and is_prime(num*10+i):
                dfs(lvl+1,num*10+i)
            else:
                continue

n = int(input())
dfs()