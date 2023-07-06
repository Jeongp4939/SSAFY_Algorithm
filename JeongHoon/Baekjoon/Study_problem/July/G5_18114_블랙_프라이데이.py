def weight_binary_search(left, right, target):
    while left<=right:
        mid = (left + right) // 2
        if weights[mid] == target:
            return 1
        elif weights[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0


n, c = map(int,input().split())
weights = list(map(int,input().split()))

weights.sort()
flag = 0

left = 0
right = n-1

if weight_binary_search(0,n-1,c):
    flag = 1
else:
    while left<right:
        tmp = weights[left]+weights[right]
        if tmp > c:
            right-=1
        elif tmp < c:
            remain = c-tmp
            if weight_binary_search(left,right,remain) and remain!=weights[left] and remain!=weights[right]:
                flag = 1
                break
            left+=1
        else:
            flag = 1
            break

print(flag)