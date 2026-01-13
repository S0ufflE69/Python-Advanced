import string
import os

# путь к папке, где лежит этот файл .py
folder = os.path.dirname(__file__)

# полный путь к text.txt
text_path = os.path.join(folder, "text.txt")
analysis_path = os.path.join(folder, "analysis.txt")

# если text.txt нет — создаём его
if not os.path.exists(text_path):
    with open(text_path, "w", encoding="utf-8") as f:
        f.write("Hello world\nPython is easy\nHello Python")

with open(text_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

total_lines = len(lines)
total_words = 0
word_count = {}

for line in lines:
    line = line.lower()
    line = line.translate(str.maketrans("", "", string.punctuation))
    words = line.split()

    total_words += len(words)

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

with open(analysis_path, "w", encoding="utf-8") as file:
    file.write("Lines: " + str(total_lines) + "\n")
    file.write("Words: " + str(total_words) + "\n")
    file.write("Word frequency:\n")

    for word in word_count:
        file.write(word + ": " + str(word_count[word]) + "\n")

print("Done. Check analysis.txt")
