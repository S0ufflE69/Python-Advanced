it = input("Enter items: ").split()  
freq = {}  
for i in it:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

# purchase frequency
print("Purchase frequency:")
for k in freq:  
    print(k, ":", freq[k])

# most popular 
most = ""
max_count = 0
for k in freq:
    if freq[k] > max_count:
        max_count = freq[k]
        most = k
print("Most popular:", most)

# once
once = []
for k in freq:
    if freq[k] == 1:
        once.append(k)
print("Purchased once:", ' '.join(once))

# sorted 
sorted_items = list(freq.items())
for i in range(len(sorted_items)):
    for j in range(i+1, len(sorted_items)):
        if sorted_items[j][1] > sorted_items[i][1]:
            sorted_items[i], sorted_items[j] = sorted_items[j], sorted_items[i]

print("Sorted by frequency:")
for k, v in sorted_items:
    print(k, v)
