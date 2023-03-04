# https://www.acmicpc.net/problem/10709
# 입력은 1 + H 행으로 주어진다.
# 첫 번째 행에는 정수 H, W (1 ≦ H ≦ 100, 1 ≦ W ≦ 100) 가 공백을 사이에 주고 주어진다.
# 이것은 JOI시가 H × W 개의 작은 구역으로 나뉘어 있다는 것을 의미한다.
# 이어진 H 개의 행의 i번째 행 (1 ≦ i ≦ H) 에는 W문자의 문자열이 주어진다.
# W 개의 문자 중 j번째 문자 (1 ≦ j ≦ W) 는, 구역 (i, j) 에 지금 구름이 떠 있는지 아닌지를 나타낸다.
# 구름이 있는 경우에는 영어 소문자 'c' 가, 구름이 없는 경우에는 문자 '.' 가 주어진다.

n,m = map(int,input().split())
arr = [input() for _ in range(n)]
answer = [[0]*m for _ in range(n)]

for i in range(n):
    cnt = -1
    flag=0
    for j in range(m):
        if arr[i][j]=='c':
            flag=1
            cnt=0
        elif flag:
            if arr[i][j]=='.':
                cnt+=1
        else:
            cnt=-1
        answer[i][j]=cnt

for line in answer:
    print(*line)


