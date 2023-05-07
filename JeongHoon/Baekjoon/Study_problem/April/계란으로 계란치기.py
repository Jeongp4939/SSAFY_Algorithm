# 계란의 순서에 따른 배열을 만들고
# 조건을 만족하는 계란을 찾아보기

def make_egg_set(depth=0, arr=[]):
    if depth == N:
        if tuple(arr) in egg_set:
            return
        else:
            egg_set.add(tuple(arr))
    for i in range(N):
        if not used[i]:
            used[i] = 1
            make_egg_set(depth+1, arr+[eggs[i]])
            used[i] = 0

N = int(input())
used = [0]*N
eggs = []
egg_set = set()

for _ in range(N):
    egg, weight = map(int,input().split())
    eggs.append((egg,weight))

make_egg_set()
egg_set = list(egg_set)
Max = 0
for eggs in egg_set:
    cnt = 0
    temp = 0
    for i in range(1,N):
        if eggs[i][0] < eggs[i-1][1]:
            pass
print(egg_set)

