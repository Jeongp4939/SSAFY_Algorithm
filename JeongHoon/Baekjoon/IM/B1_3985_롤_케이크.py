# https://www.acmicpc.net/problem/3985
# 첫째 줄에 롤 케이크의 길이 L (1 ≤ L ≤ 1000)이 주어진다. 둘째 줄에는 방청객의 수 N (1 ≤ N ≤ 1000)이 주어진다.
# 다음 N개 줄에는 각 방청객 i가 종이에 적어낸 수 Pi와 Ki가 주어진다. (1 ≤ Pi ≤ Ki ≤ L, i = 1..N)
# 첫째 줄에 가장 많은 조각을 받을 것으로 기대하고 있던 방청객의 번호를 출력한다.
# 둘째 줄에 실제로 가장 많은 조각을 받은 방청객의 번호를 출력한다.
# 가장 많은 조각을 받도록 예상되는 방청객이 여러 명인 경우에는 번호가 작은 사람을 출력한다.

l = int(input())
n = int(input())

# 받을 조각의 수를 저장할 배열
cnt_lst = [0]*(n+1)
ex_lst = [0]*(n+1)
l_lst = [0]*(l+1)

for i in range(n):
    a,b = map(int,input().split())
    for j in range(a,b+1):
        ex_lst[i]+=1
        if not l_lst[j]:
            l_lst[j]=1
            cnt_lst[i]+=1

print(ex_lst.index(max(ex_lst))+1)
print(cnt_lst.index(max(cnt_lst))+1)



