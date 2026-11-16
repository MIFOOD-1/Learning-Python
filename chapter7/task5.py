# 5. Дан name = "Вася", age = 25. 
# Выведи "Вася, 25 лет" тремя способами: %-форматирование, format(), f-строка.

name = "Вася"
age = 25

print("%s, %d лет" % (name, age)) 
print("{}, {} лет" .format(name, age)) 
print(f"{name}, {age} лет")