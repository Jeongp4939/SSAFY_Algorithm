# 단어 중에서 한 알파벳만 다른 단어들을 찾기
# 그 단어들로 경로를 만들어서 진행
flag = 0
Min = int(28e8)
def solution(begin, target, words):
    global flag, Min
    flag = 0
    Min = int(28e8)
    if target not in words:
        return 0
    def check(a, b):
        cnt = 0
        for i in range(n):
            if a[i] == b[i]:
                cnt += 1
        if cnt == n - 1:
            return 1
        return 0

    def dfs(bg, tg,cnt=0):
        global flag, Min
        if bg == tg:
            flag = 1
            Min = min(Min,cnt)
            return
        for i in range(n_words):
            if not visited[i]:
                if check(bg, words[i]):
                    visited[i] = 1
                    dfs(words[i], tg, cnt+1)
                    visited[i] = 0

    n = len(begin)
    n_words = len(words)
    visited = [0] * n_words

    dfs(begin,target)

    if flag:
        return Min
    else:
        return 0

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"]))
