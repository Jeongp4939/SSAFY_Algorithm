from itertools import combinations

N = int(input())

result = []
for i in range(1, 11):
    for j in combinations(range(10), i):  # 조합(중복x)
        num = ''.join(list(map(str, reversed(list(j)))))  # 0 ~ 9876543210 까지 문자열 생성
        result.append(int(num)) # 인트형으로 result에 저장

result.sort() # 오름차순으로 정렬
if N >= len(result):
    print(-1)
else:
    print(result[N])

