# https://www.acmicpc.net/problem/2606
# 한 노드에서 갈 수 있는 노드들의 숫자를 파악하는 문제
# 방문하지 않은 노드를 방문 했을 때 visited의 해당 노드 숫자 1
# 1에서 갈 수 있는 노드들만 출력이므로 1은 제외
# 양방향인걸 고려 안해서 틀림, 양방향으로 수정후 정답

def dfs(a):
    if not nodes[a]:
        return
    # 해당 node의 원소(다음 이동 경로) 탐색
    for i in nodes[a]:
        # 방문하지 않은 노드일 경우 탐색하고 cnt+=1
        if not visited[i]:
            visited[i]=1
            dfs(i)


# 노드의 개수
n = int(input())
# 간선의 개수
e = int(input())
# 노드 간의 경로를 표현하기 위한 인접리스트 생성
nodes = [[] for _ in range(n+1)]
# 방문 체크를 위한 visited 배열
visited=[0]*(n+1)

for i in range(e):
    s,e = map(int,input().split())
    nodes[s].append(e)
    nodes[e].append(s)
# 1번 노드에서 갈 수 있는 노드의 숫자 파악
dfs(1)
# 1을 제외해야하므로 -1
print(sum(visited)-1)
