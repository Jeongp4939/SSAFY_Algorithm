numbers = list(map(int, input().split()))
target = int(input())
def dfs(depth, target,idx=0, sum=0):
    global cnt
    if depth == len(numbers):
        if sum == target:
            cnt += 1
            return
        else:
            return
    for j in D:
        dfs(depth + 1, target,idx+1, sum + numbers[idx] * j)

visited = [0] * len(numbers)
cnt = 0
D = [-1, 1]

dfs(0,target)
print(cnt)

