"""
# 1 Heap 정렬 구현하기

from heapq import heappop, heappush

S = list(input())
heap = []

for i in S:
    heappush(heap,(-ord(i),i))
while len(heap)>=1:
    print(heappop(heap)[1], end='')
print()
"""
"""
# 2 부르주아 여행사

from heapq import heappop, heappush
alpha = [chr(i+ord('A')) for i in range(26)]

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
heap = []
for i in range(n):
    for j in range(n):
        # 최대값으로
        heappush(heap, (-arr[i][j], alpha[i], alpha[j]))
# print(heap)
for _ in range(3):
    path = heappop(heap)
    print(f'{path[1]}-{path[2]} {-path[0]}')
"""
"""
# 3 연쇄폭탄

from heapq import heappop, heappush

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
visited=[0]*(n*n+1)

heap = []

for i in range(n):
    for j in range(n):
        heappush(heap,(arr[i][j],i,j))

cnt=0
time = 0
while heap:
    bomb = heappop(heap)
    if not visited[bomb[0]]:
        visited[bomb[0]]=1
        cnt+=1
        time=bomb[0]
        for i in ((1,0),(-1,0),(0,-1),(0,1)):
            ny = bomb[1]+i[0]
            nx = bomb[2]+i[1]
            if 0<=ny<n and 0<=nx<n:
                if not visited[arr[ny][nx]]:
                    visited[arr[ny][nx]] = 1
                    cnt += 1
    if cnt==n*n:
        break
print(f'{time}초')
"""
"""
# 4 통행료 몰래 올리기

from heapq import heappop, heappush

n = int(input())
arr= [list(map(int,input().split())) for _ in range(n)]
heap=[]

for i in range(n):
    for j in range(n):
        if i!=j and arr[i][j]!=-1:
            heappush(heap, [arr[i][j],i,j])
for _ in range(10):
    price = heappop(heap)
    price[0] *= 2
    heappush(heap,price)
print(f'{price[0] * 2}만원')
"""
"""
# 5 Ugly Number

from heapq import heappop as hpop, heappush as hpush

N = int(input())
K = list(map(int,input().split()))

ugly = []

heap = [1]
hpush(heap, 2)
hpush(heap, 3)
hpush(heap, 5)

while len(ugly) < 1501:
    n = hpop(heap)
    if n not in ugly:
        ugly.append(n)
        hpush(heap, n*2)
        hpush(heap, n*3)
        hpush(heap, n*5)
for i in K:
    print(ugly[i-1], end=' ')
print()
"""

# 6 정중앙 대학교
#
# import sys
# from heapq import heappush, heappop
#
# input = sys.stdin.readline
#
# n = int(input())
# heap = [500]
#
# cnt = 1
#
# for _ in range(n):
#     answer = []
#     a,b = map(int,input().split())
#     heappush(heap, a)
#     heappush(heap, b)
#     while heap:
#         answer.append(heappop(heap))
#     heap = answer[:]
#     cnt+=2

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
maxheap = [-500]
minheap = []

for _ in range(n):
    input_lst = list(map(int,input().split()))
    for i in input_lst:
        if i < -maxheap[0]:
            heappush(maxheap, -i)
        else:
            heappush(minheap, i)

        if len(maxheap)>len(minheap):
            heappush(minheap,-heappop(maxheap))
        if len(maxheap)<len(minheap):
            heappush(maxheap, -heappop(minheap))

    print(-maxheap[0])

