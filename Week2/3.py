s = input()
a,op,b,c = s[0],s[1],s[2],s[4]


if a != 'x': a = int(a)
if b != 'x': b = int(b)
c = int(c)

if a == 'x':
    x = c - b if op=='+' else c + b
else:
    x = c - a if op=='+' else a - c
print(x)