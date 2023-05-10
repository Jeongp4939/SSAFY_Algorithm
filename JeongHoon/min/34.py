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
"""
# 3 민코 북카페

def binarySearch(book):
    cnt = 1
    idx = lst.index(book)
    st = 0
    ed = n-1
    while 1:
        mid = (st+ed)//2
        if st>ed:
            return cnt
        if mid == idx:
            return cnt
        if mid < idx:
            st = mid + 1
            cnt+=1
        else:
            ed = mid - 1
            cnt+=1

n = int(input())
lst = input().split()
lst.sort(key=lambda x:x[0])
m = int(input())
for i in range(m):
    book,searchCnt = input().split()
    if book in lst:
        rlt = binarySearch(book)
    else:
        rlt = 10**8
    if rlt <= int(searchCnt):
        print('pass')
    else:
        print('fail')
"""
"""
# 4 클라우드 데이터 백업

def binarySearchArray():
    st,ed = 0,N-1
    while 1:
        mid = (st+ed)//2
        if st > ed:
            return mid
        if arr[mid] != '#'*N and arr[mid] != '0'*N:
            return mid
        if arr[mid] == '#'*N:
            if mid<N-1 and arr[mid+1][0] == '#':
                st = mid+1
            else:
                return mid
        if arr[mid] == '0'*N:
            ed = mid-1

def binarySearch(idx):
    st, ed = 0, N - 1
    while 1:
        mid = (st+ed)//2
        if st>ed:
            return mid
        if mid<N-1 and arr[idx][mid] == '#' and arr[idx][mid+1] == '0':
            return mid
        elif mid==N-1:
            return mid
        if arr[idx][mid] == '#' and arr[idx][mid+1] == '#':
            st = mid+1
        if arr[idx][mid] == '0' and arr[idx][mid+1] == '0':
            ed = mid-1

N = int(input())

arr = [input() for _ in range(N)]
print(binarySearchArray(),binarySearch(binarySearchArray()))
"""

# 5 root 계산기