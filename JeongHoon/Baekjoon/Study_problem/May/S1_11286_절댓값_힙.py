from queue import PriorityQueue
import sys
print = sys.stdout.write
input = sys.stdin.readline

n = int(input())
q = PriorityQueue()
for _ in range(n):
    request = int(input())
    if not request:
        if q.empty():
            print('0\n')
        else:
            temp = q.get()
            print(str(temp[1])+'\n')
    else:
        q.put((abs(request),request))