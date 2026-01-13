import json
import os

# путь к папке, где лежит этот файл
folder = os.path.dirname(__file__)

students_path = os.path.join(folder, "students.json")
output_path = os.path.join(folder, "students_updated.json")

# читаем json
with open(students_path, "r", encoding="utf-8") as file:
    students = json.load(file)

# считаем средний балл
for student in students:
    grades = student["grades"]
    student["average"] = sum(grades) / len(grades)

# записываем в новый файл
with open(output_path, "w", encoding="utf-8") as file:
    json.dump(students, file, indent=4)

print("Done. File students_updated.json created.")
