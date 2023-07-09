import heapq
import sys

input = sys.stdin.readline

INF = 1e10

def find_target(n,k):
    times = [INF] * 100001
    times[n] = 0
    q = [(0,n)]

    while q:
        time, x = heapq.heappop(q)
        if time > times[x]:
            continue

        for next_x, cur_time in [(x-1,1),(x+1,1),(2*x,0)]:
            next_time = time + cur_time

            if 0 <= next_x < 100001 and time < times[next_x]:
                times[next_x] = next_time
                heapq.heappush(q,(next_time, next_x))
    return times[k]

n,k = map(int,input().split())

print(find_target(n,k))
