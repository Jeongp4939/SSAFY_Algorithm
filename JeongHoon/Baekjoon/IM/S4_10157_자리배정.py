# 출력 좌표 x,y -> 조심
# 1,1 에서 시작하여 시계방향으로 회전
# 생성된 행렬에서는 아래로 뒤집어서 생각하면 될 거라 판단
# 방향은 아래 오른쪽 위 왼쪽(반시계)
# 방향 고정한 채로 쭉 진행, 채워진 좌석을 만나거나 밖을 향하면 방향변수 +1

def make_map(arr):
    y = x = 0
    num = 1
    d = 0
    while num<=(len(arr)*len(arr[0])+1):
        arr[y][x] = num

        if num==(len(arr)*len(arr[0])):
            return

        y+=dy[d]
        x+=dx[d]
        if 0<=y<len(arr) and 0<=x<len(arr[0]) and not arr[y][x]:
            num+=1
        else:
            y-=dy[d]
            x-=dx[d]
            d=(d+1)%4


c,r = map(int,input().split())
k = int(input())
y=x=0
arr = [[0]*c for _ in range(r)]

dy = [1,0,-1,0]
dx = [0,1,0,-1]

make_map(arr)

for i in range(r):
    for j in range(c):
        if arr[i][j]==k:
            y=i
            x=j
if k > r*c:
    print(0)
else:
    print(x+1,y+1)
