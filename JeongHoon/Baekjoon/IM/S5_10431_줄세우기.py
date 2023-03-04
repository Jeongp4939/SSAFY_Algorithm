# https://www.acmicpc.net/problem/10431

# 자기 앞에 자기보다 키가 큰 학생이 없다면 그냥 그 자리에 서고 차례가 끝난다.
# 자기 앞에 자기보다 키가 큰 학생이 한 명 이상 있다면 그중 가장 앞에 있는 학생(A)의 바로 앞에 선다.
# 이때, A부터 그 뒤의 모든 학생들은 공간을 만들기 위해 한 발씩 뒤로 물러서게 된다.
# 첫 줄에 테스트 케이스의 수 P (1 ≤ P ≤ 1000) 가 주어진다.
# 각 테스트 케이스는 테스트 케이스 번호 T와 20개의 양의 정수가 공백으로 구분되어 주어진다.

p = int(input())
for t in range(p):
    tc, *lst = map(int,input().split())
    cnt = 0
    for i in range(1,20):
        for j in range(i):
            if lst[i]<lst[j]:
                cnt+=1

    print(f'{tc} {cnt}')

