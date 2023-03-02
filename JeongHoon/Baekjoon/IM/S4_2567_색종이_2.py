n = int(input())

arr = [[0]*102 for _ in range(102)]

for _ in range(n):
    x,y = map(int,input().split())
    for i in range(y,y+10):
        for j in range(x,x+10):
            arr[i][j]=1
cnt = 0

for i in range(1,102):
    for j in range(1,102):
        # 사각형을 만나는 경우와 나가는 경우 카운트
        if arr[i][j]!=arr[i][j-1]:
            cnt+=1
        if arr[j][i]!=arr[j-1][i]:
            cnt+=1
print(cnt)
