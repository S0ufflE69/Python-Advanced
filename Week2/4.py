n, m = map(int, input().split())
text = input()
words = set()
for i in range(n - m + 1):
    words.add(text[i:i+m])

print(len(words))
