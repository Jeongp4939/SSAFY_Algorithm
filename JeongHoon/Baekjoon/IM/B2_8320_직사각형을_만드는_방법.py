D =[0]*10001
for i in range(1,10001):
    for j in range(1,int(i**(1/2))+1):
        if i%j==0:
            D[i]+=1
for i in range(1,10001):
    D[i]+=D[i-1]

n = int(input())
print(D[n])

