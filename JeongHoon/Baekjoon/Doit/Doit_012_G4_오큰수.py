# https://www.acmicpc.net/problem/17298
# 크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다.
# Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.
# 예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다.
# A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.

# import sys
# input = sys.stdin.readline

# def NGE(i):
#     # for문이 2중으로 사용되어 시간초과가 나옴
#     for a in A[i:]:
#         if A[i]<a:
#             rlt.append(a)
#             return
#     rlt.append(-1)
#     return
#
# n = int(input())
# A = list(map(int,input().split()))
# rlt = []
#
# for i in range(n):
#     NGE(i)
#
# print(*rlt)

n = int(input())
A = list(map(int,input().split()))
# -1로 이루어진 배열 선언
answer = [-1]*n
# 인덱스값을 저장할 stack 선언
stack = []

# 처음에 해당하는 0 stack에 추가
stack.append(0)
for i in range(n):
    while stack and A[stack[-1]]<A[i]:
        answer[stack.pop()]=A[i]
    # stack에 다음 인덱스 추가 stack=[0,0]일 때 A[1]이 더 크므로
    # answer[0]에 A[1]이 저장되고 while문 조건이 만족되어있으므로 0이 제거 됨
    # 다음 인덱스로 넘어 갔을 시 i+1이 구해지면 i또한 구해지므로 끝까지 반복 하면 정답 출력
    stack.append(i)

print(*answer)
