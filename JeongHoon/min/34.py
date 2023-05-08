"""
# 1 Binary Search

arr = [4,4,5,7,8,10,20,22,23,24]

st = 0
ed = len(arr)-1
target = int(input())
result = 'X'
while True:
    mid= (st+ed)//2
    if st > ed:
        result = 'X'
        break
    if arr[mid] == target:
        result = 'O'
        break
    if arr[mid] < target:
        st = mid+1
    else:
        ed = mid-1

print(result)
"""
"""
# 2 자동차 기름 채우기

def binarySearch():
    st = 0
    ed = 9

    while 1:
        mid = (st+ed)//2
        if st>ed:
            return '10%'
        if arr[mid] == '#' and arr[mid+1]=='_':
            return f'{(mid+1)*10}%'
        if arr[mid]=='_' and arr[mid+1]=='_':
            ed = mid - 1
        if arr[mid]=='#' and arr[mid+1]=='#':
            st = mid + 1

arr = input()+'_'
print(binarySearch())
"""

# 3 민코 북카페
