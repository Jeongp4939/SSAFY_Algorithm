# moo 0
# s = 'moomooomoo' # 0 3 7 / 3 4
# s = 'moomooomoomoooomoomooomoo' # 0 3 7 10 15 18 22 / 3 4 3 5 3 4
# s = 'moomooomoomoooomoomooomoomooooomoomooomoomoooomoomooomoo' # 0 3 7 10 15 18 22 25 31 34 38 41 46 49 53 / 3 4 3 5 3 4 3 6 3 4 3 5 3 4
s = 'moomooomoomoooomoomooomoomooooomoomooomoomoooomoomooomoomoooooomoomooomoomoooomoomooomoomooooomoomooomoomoooomoomooomoo'
# 0 3 7 10 15 18 22 25 31 34 38 41 46 49 53 56 63 66 70 73 78 81 85 88 94 97 101 104 109 112 116

import time

st = time.time()
for i in range(len(s)):
    if s[i]=='m':
        print(i//3, i%3)

ed = time.time()
print('\ntime : ',ed-st)
