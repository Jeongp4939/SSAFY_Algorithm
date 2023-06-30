from itertools import combinations

N = int(input())

result = []
for i in range(1, 11):
    # 조합(중복x)
    # 작동 방식 -> 하나의 수가 나오면 다음의 숫자는 자동적으로 보다 큰 수가 오게 됨
    # 순서를 고려하지 않으며 중복을 허용하지 않기 때문데
    # 0 01 02 ... 09 012 013 ...
    # 위처럼 앞에 있는 숫자(이 경우 작은수)가 먼저 조합의 리스트에 있기 때문에
    # 앞뒤가 바뀌어 큰수 뒤에 작은 수가 오는 경우가 있을 수 없음
    for j in combinations(range(10), i):
        num = ''.join(list(map(str, reversed(list(j)))))  # 0 ~ 9876543210 까지 문자열 생성
        result.append(int(num))  # 인트형으로 result에 저장

result.sort() # 오름차순으로 정렬
if N >= len(result):
    print(-1)
else:
    print(result[N])

