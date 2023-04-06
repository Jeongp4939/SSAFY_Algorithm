N = int(input())
cnt = 0
DAT = [0]*N
LDRU=[0]*(N*2)
LURD=[0]*(N*2)

def nqueen(row):
    global cnt
    if row == N:
        cnt+=1
        return
    for i in range(N):
        # i열이 사용중이면 X
        if DAT[i]:
            continue
        # 오른쪽 위로 향하는 대각선에 Queen이 있으면 불가능
        if LURD[i+row]:
            continue
        # 오른쪽 아래로 향하는 대각선에 Queen이 있으면 불가능
        if LDRU[i-row+N]:
            continue

        DAT[i] = 1
        LDRU[i+row]=1
        LURD[i-row+N]=1
        nqueen(row+1)
        DAT[i] = 0
        LDRU[i+row]= 0
        LURD[i-row+N]=0

nqueen(0)
print(cnt)