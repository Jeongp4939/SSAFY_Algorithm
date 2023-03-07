# https://www.acmicpc.net/problem/1874

# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
# 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자
# 첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 둘째 줄부터 n개의 줄에는
# 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다.
# 물론 같은 정수가 두 번 나오는 일은 없다.
# 입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다.
# push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.

from collections import deque
import sys
input = sys.stdin.readline

def push(a):
    global top ,rlt
    while lst and lst[0]<=a:
        if lst:
            stack.append(lst.popleft())
            top+=1
            rlt+='+\n'

def s_pop(a):
    global top, flag,rlt
    if top !=-1 and stack[top]==a:
        stack.pop()
        rlt+='-\n'
        top-=1
    elif a<stack[top]:
        flag=1
        return


n = int(input())
lst = deque(i for i in range(1,1+n))
stack=[]
rlt = ''
flag = False
top=-1

for _ in range(n):
    a = int(input())
    if top==-1 or a>stack[top]:
        push(a)
        s_pop(a)
    elif a<=stack[top]:
        s_pop(a)

if flag:
    print('NO')
else:
    print(rlt)
