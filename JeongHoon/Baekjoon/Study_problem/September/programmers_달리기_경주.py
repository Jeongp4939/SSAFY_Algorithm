def solution(players, callings):
    answer = []
    player = dict()
    # dictionary에 선수와 등 수 정보 입력
    for i in range(len(players)):
        player[i + 1] = players[i]
        player[players[i]] = i + 1

    for p in callings:
        rank = player[p]
        front = player[rank - 1]

        player[rank], player[rank - 1] = player[rank - 1], player[rank]
        player[p], player[front] = player[front], player[p]

    for i in range(1, len(players) + 1):
        answer.append(player[i])

    return answer