# 출발 노드와 도착 노드를 입력 받아 두 노드 사이의 거리를 구하는 문제

def dfs(s,e,level=0):
    global rlt, flag
    # 시작 노드가 도착 노드와 같아지면 flag를 세우고 return
    if s == e:
        rlt=min(rlt,level)
        flag=1
        return
    # 도착한 노드가 비어있는 노드라면 return
    if not nodes[s]:
        return
    # 시작 노드의 원소(경로) 중 이동한 적 없는 방향으로 이동
    for i in nodes[s]:
        if not visited[i]:
            visited[i]=1
            dfs(i,e,level+1)

n = int(input())
st,ed = map(int,input().split())
nodes = [[] for _ in range(n+1)]
visited=[[] for _ in range(n+1)]
m = int(input())
# 관계가 쌍방향이므로 양쪽 노드에 모두 경로를 추가 해줌
for _ in range(m):
    s,e = map(int,input().split())
    nodes[s].append(e)
    nodes[e].append(s)
rlt = 28e8
flag=0
dfs(st,ed)
if flag:
    print(rlt)
else:
    print(-1)
