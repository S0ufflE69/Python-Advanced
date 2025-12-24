a,b = input(), input()
c = b + b
count = 0
for i in range(len(a) - len(b) + 1):
    if a[i:i+len(b)] in c:
        count += 1
print(count)
