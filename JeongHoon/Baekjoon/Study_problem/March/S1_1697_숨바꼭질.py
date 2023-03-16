D=[0]*100000

n,k = map(int,(input().split()))

for i in range(1,10000//n):
    D[i*n]=i
    for j in range(1,n-1):
        D[i*n+j]=D[i*n]+j
    for j in range(1,n-1):
        D[(i+1)*n-j] = min(D[i*n]+j,D[(i+1)*n-j])
Min = int(28e8)

print(D[k])

