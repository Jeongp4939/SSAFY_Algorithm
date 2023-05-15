n,m = map(int,input().split())
lst = list(map(int,input().split()))
st = 0
ed = 0

for i in lst:
    if st < i:
        start = i
    ed+=1


