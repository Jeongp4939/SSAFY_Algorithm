# https://www.acmicpc.net/problem/10163
# pypy 실행시 100점 통과

import sys
input = sys.stdin.readline


arr = [[0]*1001 for _ in range(1001)]

N = int(input())
Mi = 0
Mj = 0

for n in range(1,N+1):
    y,x, yi,xj = map(int,input().split())

    if y+yi > Mi:
        Mi = y+yi
    if x+xj > Mj:
        Mj = x+xj

    for i in range(y,y+yi):
        for j in range(x,x+xj):
            arr[i][j]=n

D={}
for i in range(N+1):
    D[i]=0

for i in range(Mi):
    for j in range(Mj):
        D[arr[i][j]]+=1

for i in range(1,N+1):
    print(D.get(i))

