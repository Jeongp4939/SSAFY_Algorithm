import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    a = int(input())
    if not a:
        if heap: print(-heapq.heappop(heap))
        else: print(0)
    else:
        heapq.heappush(heap,-a)
