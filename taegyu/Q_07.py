n = int(input())
s = str(n) # len(s) : even number

l, r = 0, 0
for i in range(len(s)):
    if i < len(s)//2:
        l += int(s[i])
else:
    r += int(s[i])

if l == r:
    print('LUCKY')
else:
    print('READY')