# https://www.acmicpc.net/problem/2527
# 직사각형(S1)
# 왼쪽 아래의 좌표 (x,y)와 오른쪽 위의 좌표 (p,q) 가 주어진다 (x<p, y<q)
# 4개의 입력이 주어지고, 각 줄에 2개의 사각형이 주어진다.
# 이 때 두 직사각형의 겹치는 부분이 직사각형일 경우 a, 선분일 경우 b, 점일 경우 c, 겹치는 부분이 없을 때 d를 출력한다

def rect_overlap(x1, y1, p1, q1, x2, y2, p2, q2):
    # 1. 안만나는 경우
    if (x2>p1) or (x1>p2) or (y1>q2) or (y2>q1):
        print('d')
        return
    # 2. 한 점에서 만나는 경우
    if (x1==p2 and (y1==q2 or q1==y2)) or (p1==x2 and (y1==q2 or q1==y2)):
        print('c')
        return
    # 3. 선분이 만나는 경우
    if x1==p2 or x2==p1 or y1==q2 or y2==q1:
        print('b')
        return
    # 4. 나머지 겹치는 경우
    print('a')
    return


# 총 4번의 테스트 케이스
for _ in range(1,5):

    x1,y1,p1,q1,x2,y2,p2,q2 = map(int,input().split())     # 직사각형의 좌표값 입력

    rect_overlap(x1, y1, p1, q1, x2, y2, p2, q2)
