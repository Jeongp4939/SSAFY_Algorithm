import sys
input = sys.stdin.readline

n = int(input())
A = []
for i in range(n):
    A.append((int(input()),i))

Max = 0
sorted_A = sorted(A)

for i in range(n):
    Max=max(Max,sorted_A[i][1]-i)
print(Max + 1)