# import sys
# import math
# print(sys.platform)
# print(2 ** 100)
# x = 'Spam!'
# print(x * 8)
# print("HAHAHAH")
# name = math.sqrt(85)
# print(name)
# input()

# -------------------------------------
# S = 'Spam'
# print(len(S))

# print(S[0])

# print(S[1])

# print(S[-1])
# print(S[-2])
# print(S[-3])
# print(S[-4])
# # print(S[-5])      //ошибка 
# print(S[0 : 3])

# print(S[1:])
# print(S[:3])
# print(S[-1:])
# print(S[:])

# print(S + 'xyz')
# print(S)    #не изменно 
# print(S * 5)

# S[0] = 'z'      #ошибка
# print(S)       

# S = 'z' + S[1:]
# print(S)

#------------------------------------------------
# S = 'shrubbery'
# L = list(S)         #развернуть в список: [...]
# print(L)

# L[1] = 'c'          #изменить на месте
# print(L)
# result = ''.join(L)          #объекдигить с пустым разделителем
# print(result)            

# B = bytearray(b'spam')  #гибрид байтов/списка
# B.extend(b'eggs')       #b необходимо в пайтон 3.Х
# print(B)
# print(B.decode())       #преобразовать в обычную строку

#------------------------------------------------------------
# S = 'Spam'
# print(S.find('pa'))        #найти смещение подстроки
# print(S)
# print(S.replace('pa', 'XYZ'))   #Заменить вхождения подстроки в S другой подстрокой
# print(S)
# S = S.replace('pa', 'XYZ')
# print(S)

#------------------------------------------------------------
# line = 'aaa,bbb,cccc,dd'
# print(line)
# print(line.split(','))

# S = 'spam'
# print(S.upper())
# print(S.isalpha())

# line = 'aaa,bbb,ccccc,dd\n'
# print(line)                        
# print(line.rstrip())                #удалить пробельные символы с правой стороны
# print(line.rstrip().split(','))     #скомбинировать

#------------------------------------------------------------
# print('%s, eggs, and %s' % ('spam', 'SPAM'))
# print('{0}, eggs and {1}'.format('spam', 'SPAM'))
# print('{}, eggs and {}'.format('spam', 'SPAM'))

# print('{:,.2f}'.format(296999.2567))
# print('%.2f | %+05d' % (3.14159, -42))

# ----------------------------------------------------------
# S = 'spam'
# print(dir(S))
# print(S + 'NI!')
# print(S.__add__('NI!'))
# print(help(S.replace))
#-----------------------------------------------------------

# S = 'A\nB\tC'       # \n - конец строки, \t - табуляция
# print(len(S))       # Как \n, так и \t является только одним символом
# ord('\n')           # \n - один символ, кодируемый как десятичное значение 10
# S = 'A\0B\0C'       # \0, байт с двоичными нулями, не завершает строку
# print(len(S))
# print(S)

# msg = """
# aaaaaaaaaaaaaaaa
# bbbbbbb'''bbbbbbbbb""bbbbbbbbbbbbb'bbbbb
# cccccccccccccccccc
# dddddddd
# """
# print(msg)

#---------------------------------------------------------
lol = 'sp\xc4m'
print(lol)













