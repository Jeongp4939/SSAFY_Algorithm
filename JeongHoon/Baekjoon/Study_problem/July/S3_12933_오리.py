quack = {0:"q", 1:"u", 2:"a", 3:"c", 4:"k"}

s = input()
length = len(s)
check = [0]*length

i = 0
answer = 0
if length%5!=0 or s[-1]!='k':
    print(-1)
else:
    while i<length:
        # q에 해당하는 문자 탐색
        if s[i]=="q" and not check[i]:
            flag= 0

            j = i
            # 현재 문자 q를 나타냄
            word=0
            # q를 시작점으로 하면서 이후의 문자들을 전부 조사
            while j < length:
                if 5-word%5 > length-j:
                    break
                for k in range(j,length):
                    if s[k] == quack[word % 5] and not check[k]:
                        if word%5==4:
                            if not flag:
                                answer+=1
                                flag=1
                        check[k]=1
                        j = k
                        word += 1
                        break
                j+=1
        i += 1

    if 0 in check:
        print(-1)
    else:
        print(answer if answer else -1)