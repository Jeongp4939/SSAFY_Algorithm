def is_prime(n):
    if n==1 or n==0:
        return 0
    if n==2:
        return 1
    else:
        for i in range(2,int(n**(1/2))+1):
            if n%i==0:
                return 0
    return 1

def dfs(depth, numbers, li_len, num_set, used, num="0"):
    if int(num) not in num_set:
        if is_prime(int(num)):
            num_set.add(int(num))
    if depth==li_len:
        return
    for i in range(li_len):
        if not used[i]:
            used[i]=1
            dfs(depth+1, numbers, li_len, num_set, used, num+numbers[i])
            used[i]=0


def solution(numbers):
    used=[0]*len(numbers)
    num_set = set()
    dfs(0,numbers,len(numbers),num_set,used)
    answer = len(num_set)
    return answer


print(solution("17"))