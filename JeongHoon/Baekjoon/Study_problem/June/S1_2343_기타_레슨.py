# 강의 순서가 바뀌면 안된다 -> 정렬이 된 상태로 취급
# 이진 탐색
# 블루레이 개수와 크기를 최소로 하려함

n,m = map(int,input().split()) # 강의 수와 블루레이 개수
times = list(map(int,input().split())) # 강의 길이 리스트

Min = max(times)
Max = sum(times)

while Min <= Max:
    mid = (Min+Max)//2  # 블루레이의 총 길이의 최대값
    cnt = 1

    blueRayLength = 0

    for i in range(n):
        if blueRayLength + times[i] > mid:
            blueRayLength = times[i]
            cnt += 1
        else:
            blueRayLength += times[i]

    if cnt > m: # cnt가 블루레이 개수를 넘어가면 안됨, 넘어간다면 mid의 크기 증가
        Min = mid + 1
    else:
        Max = mid - 1

print(Min)