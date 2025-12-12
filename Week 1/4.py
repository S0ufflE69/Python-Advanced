N = int(input())
k=0

if N>= 1:
    for i in range(1, N+1):
        k += i
else:
    for i in range(1, N-1, -1):
        k += i

print(k)
