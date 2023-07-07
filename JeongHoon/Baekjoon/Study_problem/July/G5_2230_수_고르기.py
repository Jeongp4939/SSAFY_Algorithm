import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = []
for i in range(n):
    a =int(input())
    lst.append(a)

lst.sort()

left = right = 0
result = 2e9

while left<=right and right < n:
    gap = lst[right] - lst[left]
    if gap < m:
        right +=1
    else:
        result = min(gap,result)
        left +=1

print(result) #.