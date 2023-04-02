# 시작은 ICN
result=[]
def solution(tickets):
    global result
    # 시작은 항상 ICN이라 했으므로 ICN을 미리 path에 넣고 시작
    def dfs(city,cnt=1,path = ["ICN"]):
        global result
        # 방문한 도시의 수가 n이 되면 종료
        if cnt == n:
            result.append(path)
            return
        # cities 딕셔너리에 city가 key로 존재 할때 아니면 0으로 해서 반복문을 시행하지 않고 종료
        for i in range(len(cities.get(city)) if cities.get(city) else 0):
            if cities[city][i]!=0:
                temp = cities.get(city)[i]
                cities.get(city)[i]=0
                dfs(temp,cnt+1,path+[temp])
                cities.get(city)[i]=temp

    n = len(tickets)+1
    cities =dict()

    # cites를 딕셔너리로 생성
    for i in tickets:
        if i[0] not in cities:
            cities[i[0]] = [i[1]]
        else:
            cities[i[0]].append(i[1])

    # cites의 각 키에 해당하는 값(해당 도시에서 가는 경로)를 알파벳 순으로 정렬
    for i in cities.keys():
        cities[i].sort()
    dfs("ICN")
    # 결과 값의 가장 앞에 오는 결과가 알파벳 순으로 가장 앞에 위치함
    answer = result[0]
    return answer

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))