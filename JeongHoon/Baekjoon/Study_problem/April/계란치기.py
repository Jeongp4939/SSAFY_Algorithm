def egg_break(idx=0,cnt=0):
    global Max
    if idx == N:
        Max = max(Max,cnt)
        return



N = int(input())
eggs = []
broken = [0]*N
Max=0

for _ in range(N):
    eggs.append(list(map(int,input().split())))

egg_break()

print(Max)