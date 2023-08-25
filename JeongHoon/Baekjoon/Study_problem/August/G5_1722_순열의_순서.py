# 다시 풀자
# 수학, 구현, 조합론
# 최대 n=20/ k값 20! DFS로 하면 시간초과

n = int(input())
seq = [i for i in range(1,n+1)]
digit = 0
case, *numbers = list(map(int,input().split()))

# factorial의 집합을 생성
factorials = [i for i in range(21)]
for i in range(2,21):
    factorials[i] *= factorials[i-1]

# 변화가 시작된 자리수 확인
for i in range(20):
    if factorials[i]<=n<factorials[i+1]:
        digit = n-i
        break

# case에 따른 분리
if case==1:
    pass
else:
    pass





# def dfs(depth=0):
#     global seq, cnt
#     if case==1 and numbers[0]<cnt:
#         return
#     if depth==n:
#         if tuple(seq) in seqs:
#             return
#         seqs.append(tuple(seq))
#         cnt+=1
#         return
#     for i in range(1,n+1):
#         if not visited[i]:
#             visited[i]=1
#             seq.append(i)
#             dfs(depth+1)
#             seq.pop()
#             visited[i]=0
#
# dfs()
#
# if case==1:
#     print(*seqs[numbers[0]-1])
# else:
#     print(seqs.index(tuple(numbers))+1)

