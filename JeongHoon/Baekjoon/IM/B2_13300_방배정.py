# https://www.acmicpc.net/problem/13300
# N(1 ≤ N ≤ 1,000),K(1 < K ≤ 1,000)
# 성별 S(0,1)와 학년 Y(1 ≤ Y ≤ 6)

import math

n,k = map(int,input().split())
d = {1:{},2:{},3:{},4:{},5:{},6:{}}
for _ in range(n):
    s,y = map(int,input().split())
    if s not in d[y]:
        d[y][s]=1
    else:
        d[y][s]+=1
cnt = 0
for i in d.values():
    for j in i.values():
        cnt+=math.ceil(j/k)
print(cnt)