def countCorrectAnswer(idx,answers):
    cnt = 0
    if idx==0:
        answer=[1,2,3,4,5]
        for i in range(len(answers)):
            if answers[i]==answer[i%5]:
                cnt+=1
    elif idx==1:
        answer=[2,1,2,3,2,4,2,5]
        for i in range(len(answers)):
            if answers[i]==answer[i%8]:
                cnt+=1
    else:
        answer=[3,3,1,1,2,2,4,4,5,5]
        for i in range(len(answers)):
            if answers[i]==answer[i%10]:
                cnt+=1
    return cnt


def solution(answers):
    answer = []
    temp = []
    for i in range(3):
        temp.append(countCorrectAnswer(i,answers))
    Max = max(temp)
    for i in range(3):
        if temp[i]==Max:
            answer.append(i+1)
    answer.sort()

    return answer