# 1. Написание базовых циклов. В данном упражнении предлагается поэксперименти
# ровать с циклами for.
# а) Напишите цикл for, который выводит код ASCII каждого символа в строке по 
# имени S. Для преобразования символа в целочисленный код ASCII используй
# те встроенную функцию ord (символ). Формально функция ord в Python З.Х 
# возвращает кодовую точку Unicode, но если вы ограничите содержимое стро
# ки символами ASCII, то будете получать обратно коды ASCII (Опробуйте ее 
# интерактивно, чтобы посмотреть, как она работает.)
# б) Далее измените цикл для вычисления суммы кодов ASCII всех символов в строке.
# в) Наконец снова модифицируйте код, чтобы возвращать новый список, ко
# торый содержит коды ASCII всех символов в строке. Дает ли выражение 
# map (ord, S) похожий результат? Как насчет [ord (с) for с in S]? Почему? 
# (Подсказка: см. главу 14.)

print("Input new object for translate on ASCII number or send 'stop'") 
S = input()
L = list()
while True:
    sum_simvol = 0
    if S == "stop" : 
        break
    for x in S:
        print("%s = ASCII: %d" %  (x, ord(x)))
        sum_simvol += ord(x)
        L.append(ord(x))
    print("sum simvol ASCII:", sum_simvol)
    print("Input new object for translate on ASCII number or send 'stop'") 
    S = input()
print("list: ", L)
print("end work")




#проблема, я думал у него меняется изнчальное представление, 
#однако что первым фор сохранил то и будет, из за чего цикл 
#продолжится пока не пройдет по первому символу
# print("Input new object for translate on ASCII number or send 'stop'")           
# S = input()                                                                                 
# for x in S:       
#     if S == "stop" : 
#         break
#     for x in S:
#         print("%s = ASCII: %d" %  (x, ord(x)))
#     print("Input new object for translate on ASCII number or send 'stop'") 
#     S = input()
# print("end work")


