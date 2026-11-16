# 3. Для s = " Hello, World! " получи:
# строку без пробелов по краям
# всё в верхнем регистре
# всё в нижнем регистре
# замену "World" на "Python"
# список слов, разделённых пробелом/запятой (подсказка: split)

s = " Hello, World! "
print(s)
s = s[1: len(s) - 1]
print(s)
print(s.upper())
print(s.lower())

s = s[0:s.find("World")] + "Python" 
print(s)

s = s.split()
print(s)