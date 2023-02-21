# https://www.acmicpc.net/problem/2564

# 첫째 줄에 블록의 가로의 길이와 세로의 길이가 차례로 주어진다.
# 둘째 줄에 상점의 개수가 주어진다. 블록의 가로의 길이와 세로의 길이,
# 상점의 개수는 모두 100이하의 자연수이다.이어 한 줄에 하나씩 상점의 위치가 주어진다.
# 상점의 위치는 두 개의 자연수로 표시된다. 첫째 수는 상점이 위치한 방향을 나타내는데,
# 1은 블록의 북쪽, 2는 블록의 남쪽, 3은 블록의 서쪽, 4는 블록의 동쪽에 상점이 있음을 의미한다.
# 둘째 수는 상점이 블록의 북쪽 또는 남쪽에 위치한 경우 블록의 왼쪽 경계로부터의 거리를 나타내고,
# 상점이 블록의 동쪽 또는 서쪽에 위치한 경우 블록의 위쪽 경계로부터의 거리를 나타낸다.
# 마지막 줄에는 동근이의 위치가 상점의 위치와 같은 방식으로 주어진다.
# 상점의 위치나 동근이의 위치는 블록의 꼭짓점이 될 수 없다.

def directions(dir,dist):   # 경로를 일직선으로 생각하여 각 방향에 있는 거리 계산
    if dir == 1:
        return dist
    elif dir == 2:
        return 2*w+h-dist
    elif dir == 3:
        return 2*w+2*h-dist
    else:
        return w+dist


w,h = map(int,input().split())

n = int(input())
d=[]
for i in range(n+1):
    dir, dist = map(int,input().split())
    d.append(directions(dir,dist))
rlt = 0
for i in range(n):
    In = abs(d[i]-d[n])
    Out = 2*w+2*h - In
    rlt+=(min(In,Out))
print(rlt)

