n,k = map(int,input().split())
li = []
answer=0
for _ in range(n):
    new_s = set(list(input()))
    for i in ('a','c','i','n','t'):
        if i in new_s:
            new_s.remove(i)
        new_len = len(new_s)
    li.append(new_len)

for i in li:
    if i<=k-5:
        answer+=1

print(answer)