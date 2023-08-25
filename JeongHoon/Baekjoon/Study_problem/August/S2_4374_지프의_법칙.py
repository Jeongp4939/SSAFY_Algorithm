low_alphabet = set(chr(i) for i in range(97,123))
while True:
    try:
        n = int(input())
        words_dic = {}

        st = ""
        while True:
            new_st = input().lower()
            if new_st=="endoftext":
                break
            for i in new_st:
                if i not in low_alphabet:
                    new_st = new_st.replace(i,' ')

            st=st+ " " + new_st


        words = [i for i in st.split() if len(i)!=1]
        words_set = set(words)
        for i in words_set:
            words_dic[i]=words.count(i)
        answer = [i for i in words_dic.keys() if words_dic[i]==n]
        answer.sort()

        if answer:
            for i in answer:
                print(i)
        else:
            print('There is no such word.')
        print()
    except:
        break
