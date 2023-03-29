def solution(n, computers):
    def dfs(node):
        visited[node]=1
        for i in range(n):
            if computers[node][i] and not visited[i]:
                dfs(i)
    visited = [0]*(n+1)
    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer+=1
    return answer

print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))