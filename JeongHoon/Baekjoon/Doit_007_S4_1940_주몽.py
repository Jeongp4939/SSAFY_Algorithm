# https://www.acmicpc.net/problem/1940
# 두 재료의 고유한 번호를 합쳐서 M(1 ≤ M ≤ 10,000,000)이 되면
# 갑옷이 만들어 지게 된다.
#  N(1 ≤ N ≤ 15,000) 개의 재료와 M이 주어졌을 때
#  몇 개의 갑옷을 만들 수 있는지를 구하는 프로그램을 작성하시오

# 시간 제한 2초 -> O(nlogn)
# 두개의 재료로 하나의 수 -> 투포인터
# 첫 줄에 N(재료의 개수), 둘 째 줄에 M(갑옷에 필요한 수), 셋 째줄에 재료들
import sys
input=sys.stdin.readline

N = int(input())
M = int(input())
N_L = list(map(int,input().split()))
# 효율적인 계산을 위해 N_L 리스트를 정렬
N_L.sort()
st=0
ed=N-1
cnt=0

# st가 ed와 같아지면 종료

while st<ed:
    # 두 재료를 합한 값이 M보다 작으면 작은수 인덱스++(합 커짐)
    if N_L[st]+N_L[ed]<M:
        st+=1
    # 두 재료를 합한 값이 M이면, cnt++, 양쪽 인덱스 앞뒤로 한칸씩 조정
    elif N_L[st]+N_L[ed]==M:
        cnt+=1
        st+=1
        ed-=1
    # 두 재료를 합한 값이 M보다 크면 큰수 인덱스--(합 작아짐)
    else:
        ed -= 1

print(cnt)
