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
