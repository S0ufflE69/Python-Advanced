a = input("String 1: ")  
b = input("String 2: ")  


count_a = {}
for c in a:
    if c in count_a:
        count_a[c] += 1
    else:
        count_a[c] = 1

count_b = {}
for c in b:
    if c in count_b:
        count_b[c] += 1
    else:
        count_b[c] = 1


if count_a == count_b:
    print("YES")  
else:
    print("NO")   
