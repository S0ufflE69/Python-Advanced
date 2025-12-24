lst = input().split()  # читаем список строк через пробел
max_len = max(len(s) for s in lst)  # находим длину самой длинной строки
res = [s + "_"*(max_len - len(s)) for s in lst]  # дополняем короткие строки
print(res)
