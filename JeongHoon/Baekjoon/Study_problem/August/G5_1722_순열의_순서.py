# 다시 풀자

n = int(input())
visited = [0]*(n+1)
seqs=[]
seq=[]
cnt = 0
case, *numbers = list(map(int,input().split()))

def dfs(depth=0):
    global seq, cnt
    if case==1 and numbers[0]>=cnt:
        return
    if depth==n:
        if tuple(seq) in seqs:
            return
        seqs.append(tuple(seq))
        cnt+=1
        return
    for i in range(1,n+1):
        if not visited[i]:
            visited[i]=1
            seq.append(i)
            dfs(depth+1)
            seq.pop()
            visited[i]=0

dfs()

if case==1:
    print(*seqs[numbers[0]-1])
else:
    print(seqs.index(tuple(numbers))+1)