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
# lol = 'sp\xc4m'
# print(lol)

# lol = b'a\x01c'
# print(lol)

# lol = u'sp\u00c4m'
# print(lol)

# print('spam')
# print('spam'.encode('utf8'))
# print('spam'.encode('utf16'))

# lol = '\u00A3', '\u00A3'.encode('latin1'), b'\xA3'.decode('latin1')
# print(lol)


# lol = u'x'.encode() + b'y'
# lol = u'x' + b'y'.decode()
# # lol = u'x' + b'y' //ошибка
# print(lol)
#--------------------------------------------------

# import re
# math = re.match('Hello[\t]*(.*)world', 'Hello Python world')
# print(math.group(1))

# math = re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home/:lumberjack')
# print(math.group())
# print(re.split('[/:]', '/usr/home/lumberjack'))

#---------------------------------------------------

# L = [123, 'spam', 1.23]
# print(len(L))

# # print(L[0])
# # print(L[:-1])
# # print(L + [4, 5, 6])
# # print(L * 2)
# # print(L)
# # L += [4, 5, 6]
# # print(L)

# L.append('NT')
# print(L)
# print(L.pop(2))
# print(L)

# M = ['bb', 'aa', 'cc']
# M.sort()
# print(M)

# M.reverse()
# print(M)

#-------------------------------------------------------
M = [[1,2,3], [4,5,6], [7,8,9]]
# print(M)
# print(M[1])
# print(M[1][2])

# col2 = [row[1] for row in M]
# print(col2)
# print(M[1])
# print(M)
# col2 = [row[1] + 2 for row in M]
# print(col2)
# col2 = [row[1]  for row in M if row[1] % 2 == 0]
# print(col2)

# diag = [M[i][i] for i in [0,1,2]]
# print(diag)

# doubles = [c * 2 for c in 'spam']
# print(doubles)

# print(list(range(4)))
# print(list(range(-6, 7, 2)))
# print([[x ** 2, x ** 3] for x in range(4)])
# print([[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0])

# G = (sum(row) for row in M)
# print(next(G))
# print(next(G))
# print(next(G))

# print(list(map(sum, M)))

# print({sum(row) for row in M})
# print({i : sum(M[i]) for i in range(3)})

# print([ord(x) for x in 'spaam'])
# print({ord(x) for x in 'spaam'})
# print({x : ord(x) for x in 'spaam'})
# print((ord(x) for x in 'spaam'))


# print(type([x for x in 'abc']))
# print(type({x for x in 'abc'}))
# print(type({x: ord(x) for x in 'abc'}))
# print(type((x for x in 'abc')))

#--------------------------------------------------
# D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
# print(D['food'])
# D['quantity'] += 1
# print(D)

# D = {}
# D['name'] = 'Bob'
# D['job'] = 'dev'
# D['age'] = 40
# print(D)
# print(D['name'])


# bob1 = dict(name = 'Bob', job = 'dev', age = 40, aname1 = 'Bob1', ajob2 = 'dev2', age3 = 403)
# print(bob1)

# bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
# print(bob2)

#так как у меня версия новая, у меня добавляется по порядку добавления элементов

# rec = {'name': {'first': 'Bob', 'last': 'Smith'},
#         'jobs': ['dev', 'mgr'],
#         'age': 40.5}
# print(rec['name'])
# print(rec['name']['last'])
# print(rec['jobs'])
# print(rec['jobs'][-1])
# rec['jobs'].append('janitor')
# print(rec)

#--------------------------------------------------------------------
# D = {'a' : 1, 'c' : 2, 'b' : 3}
# print(D)

# D['e'] = 99
# print(D)

# #D['f'] - ошибка

# print('f' in D)

# if not 'f' in D:
#     print('missing')

# if 'f' in D:
#     print('missing')
#     print('no, really ...') 
# print('hehe')


# value = D.get('x', 0)
# print(value)
# D['x'] = 100
# value = D['x'] if 'x' in D else 0
# print(value)

# Ks = list(D.keys())
# print(Ks)

# Ks.sort()
# print(Ks)

# for key in Ks:
#     print(key, '=>' , D[key])

# for key in sorted(D):
#     print(key, '=>', D[key])

#-------------------------------------------------------
# for c in 'spam':
#     print(c.upper())

# x = 5
# while x > 0:
#     print('spam!' * x)
#     x -= 1

# squares = [x **  2 for x in [1, 2, 3, 4, 5]]
# print(squares)

# squares = []
# for x in [1,2,3,4,5]:
#     squares.append(x ** 2)
# print(squares)

#-----------------------------------------------------

# T = (1, 2, 3, 4)
# print(len(T))
# print(T + (5, 6))
# print(T[0])
# print(T.index(4))
# print(T.count(4))

# #T[0] = 2 //ошибка кортежи нельзя менять
# T = (2,) + T[1:]
# print(T)

# T = 'spam', 3.0, [11, 22, 33]
# print(T[1])
# print(T[2][1])

# #T.append(4) //ошибка нет атрибута и по сути это изменение 

#---------------------------------------------------------------
# f = open('data.txt', 'w')
# f.write('hello\n')
# f.write('world\n')
# f.close()

# f = open('data.txt')
# text = f.read()
# print(text)
# print(text.split())
# f.close()

# for line in open('data.txt'): print(line)

# print(dir(f))

# import struct
# packed = struct.pack('i4sh', 7, b'spam', 8)
# print(packed)

# file = open('data.bin', 'wb')
# print(file.write(packed))
# file.close()

# data = open('data.bin', 'rb').read()
# print(data)
# print(data[4 : 8])
# print(list(data))
# print(struct.unpack('>i4sh', data))

#-------------------------------------------------
# S = 'sp\xc4m'
# print(S)
# print(S[2])

# file = open('unidata.txt', 'w', encoding='utf-8')
# print(file.write(S))
# file.close()
# text = open('unidata.txt', encoding='utf-8').read()
# print(text)
# print(len(text))

# raw = open('unidata.txt', 'rb').read()
# print(raw)
# print(len(raw))

# print(text.encode('utf-8'))
# print(text.encode('utf-16'))
# print(len(text.encode('latin-1')), len(text.encode('utf-16')))
# print(b'\xff\xfes\x00p\x00\xc4\x00m\x00'.decode('utf-16'))
# file.close()

# import codecs
# print(codecs.open('unidata.txt', encoding='utf8').read())
# print(open('unidata.txt', 'rb').read())
# print(open('unidata.txt').read())

#--------------------------

# X = set('spam')
# Y = {'h', 'a', 'm'}

# print(X, Y)
# print(X & Y)
# print(X | Y)
# print(X - Y)
# print(X > Y)
# print([n ** 2 for n in [1, 2, 3, 4]])
# print({n ** 2 for n in [1, 2, 3, 4]})

# print(list(set([1,2,1,3,1])))
# print(set('spam') - set('ham'))
# print(set('spam') == set('asmp'))

# print('p' in set('spam'), 'p' in 'spam', 'ham' in['eggs', 'spam', 'ham'])

# print(1/3)
# print((2/3) + (1/2))
# import decimal
# d = decimal.Decimal('3.141')
# print(d+1)
# decimal.getcontext().prec = 2
# print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))
# from fractions import Fraction
# f = Fraction(2, 3)
# print(f + 1)
# print(f + Fraction(1, 2))
# print(1>2, 1<2)
# print(bool('spam'))
# X = None
# print(X)
# L = [None] * 100
# print(L)

#---------------------------------------------------------------
# L = [None] * 100
# print(type(L))
# print(type(type(L)))

# if type(L) == type([]):
#         print('yes')
# else:
#         print('no')
# if type(L) == list:
#     print('yes')

#-------------------------------------------------------------

# class Worker:
#         def __init__(self, name, pay):            #инициализировать при создании
#             self.name = name                    #новый обхект 
#             self.pay = pay
#         def lastName(self):
#                 return self.name.split()[-1]       #разбить строку по проблеам
#         def giveRaise(self, percent):
#                self.pay *= (1.0 + percent)          #обновить pay на месте

# bob = Worker('Bob Smith', 50000)
# sue = Worker('Sue Jones', 60000)

# print(bob.lastName())
# print(sue.lastName())

# print(sue.giveRaise(.10))
# print(sue.pay)
# print(sue.name)

#--------------------------------------------------------------
#Chapter 5
# y = 10
# x = 10.0
# print(y <= x)

a = 3   #имя создается не объявляется заранее
b = 4

# print(a + 1, a - 1)
# print(b * 3, b / 2)
# print(a % 2, b ** 2)
# print(2 + 4.0, 2.0 ** b)
# print(b / 2 + a)
# print(b / (2.0 + a))

# print(1 / 2.0)
# num = 1 / 3.0
# print(num)
# print('%e' % num)
# print('%4.2f' % num)
# print('{0:4.2f}'.format(num))

# repr('spam')
# print('spam')

#---------------------------------------------------------

# print(1 < 2)
# print(2.0 >= 1)
# print(2.0 == 2.0)
# print(2.0 != 2.0)

# X = 2
# Y = 4
# Z = 6

# print(X < Y < Z)
# print(X < Y and Y < Z)
# print(X < Y > Z)
# print(X < Y and Y > Z)
# print(1 < 2 < 3.0 < 4)
# print(1 > 2 > 3.0 > 4)

# print(1 == 2 < 3) #то же что и 1 == 2 and 2 < 3
# print(1.1 + 2.2 == 3.3)
# print(1.1 + 2.2)
# print((int)(1.1 + 2.2) == (int)(3.3))

# X = Y // Z
# print(X)
# X = Y / float(Z)
# print(X)

# from__future__iport division #Делает доступным поведение / из Python З.Х
# import math
# print(math.floor(2.5))
# print(math.floor(-2.5))
# print(math.trunc(2.5))
# print(math.trunc(-2.5))

# print(5 / 2, 5 / -2)
# print(5 // 2, 5 // -2)
# print(5 / 2.0, 5 / -2.0)
# print(5 // 2.0 , 5 // -2.0)


# import math
# print(5 / -2)
# print(5 // -2)
# print(math.trunc(5 / -2))


# print((5 / 2), (5 / 2.0), (5 / -2.0), (5 / -2))
# print((5 // 2), (5 // 2.0), (5 // -2.0), (5 // -2))
# print((9 / 3), (9 / 3.0), (9 // 3), (9 // 3.0))

#-------------------------------------------------------------


# print(0o1, 0o20, 0o377)
# print(0x01, 0x10, 0xFF)
# print(0b1, 0b10000, 0b11111111)

# print(0xFF, (15 * (16 ** 1)) + 15 * (16 ** 0))
# print(0x2F, (2 * (16 ** 1)) + (15 * (16 ** 0)))
# print(0xF, 0b1111, (1 * (2 ** 3) + 1 * (2 ** 2) + 1 * (2 ** 1) + 1 * (2 ** 0)))

# print(oct(64), hex(64), bin(64))

# print(64, 0o100, 0x40, 0b1000000)
# print(int('64'), int('100', 8), int('40', 16), int('1000000', 2))
# print(int('0x40', 16), int('0b1000000', 2))
# print(int('100', 10))

# print('{0:o}, {1:x}, {2:b}'.format(64, 64, 64))
# print('%o, %x, %x, %X,' % (64, 64, 255, 255))
# print(0o1, 0o20, 0o377)

# x = 1
# print(x << 2)
# print(x | 2)
# print(x & 1)

# X = 0b0001
# print(X << 2)
# print(bin(X << 2))
# print(bin(X | 0b010))
# print(bin(X & 0b1))

# X = 0xFF
# print(bin(X))
# print(X ^ 0b10101010)
# print(bin(X ^ 0b10101010))
# print(int('01010101', 2))
# print(hex(85))

# X = 99
# print(bin(X), X.bit_length(), len(bin(X)) - 2)
# print(bin(256), (256).bit_length(), len(bin(256)) - 2)

#-------------------------------------------------------------
# import math
# print(math.pi, math.e)
# print(math.sin(2 * math.pi / 180))
# print(math.sqrt(144), math.sqrt(2))
# print(pow(2, 4), 2 ** 4, 2.0 ** 4.0)
# print(abs(-42.0), sum((1, 2, 3, 4)))
# print(min(3, 1, 2, 4), max(3, 1, 2 ,4))
# print(math.floor(2.567), math.floor(-2.567))
# print(math.trunc(2.567), math.trunc(-2.567))
# print(int(2.257), int(-2.567))
# print(round(2.567), round(2.467), round(2.567, 2))
# print('%.1f' %2.567, '{0:.2f}'.format(2.567))

# print((1 / 3.0), round(1 / 3.0, 3), ('%.2f' % (1 / 3.0)))

# import math
# print(math.sqrt(144))
# print(144 ** .5)
# print(pow(144, .5))
# print(math.sqrt(1234567890))
# print(1234567890 ** 0.5)
# print(pow(1234567890, .5))

# import random
# # print(random.random())
# # print(random.random())

# # print(random.randint(1, 10))
# # print(random.randint(1, 10))

# print(random.choice(['Life of Brian', 'Holy Grail', 'Meaning of life']))
# print(random.choice(['Life of Brian', 'Holy Grail', 'Meaning of life']))

# suits = ['hearts', 'clubs', 'diamonds', 'spades']
# random.shuffle(suits)
# print(suits)
# random.shuffle(suits)
# print(suits)

#------------------------------
# print(0.1 + 0.1 + 0.1 - 0.3)

# from decimal import Decimal
# print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))

# import decimal
# print(decimal.Decimal(1) / decimal.Decimal(7))
# decimal.getcontext().prec = 4
# print(decimal.Decimal(1) / decimal.Decimal(7))
# print(decimal.Decimal(0.1) + decimal.Decimal(0.1) + decimal.Decimal(0.1) - decimal.Decimal(0.3))

# print(1999 + 1.33)
# decimal.getcontext().prec = 2
# pay = decimal.Decimal(str(1999 + 1.33))
# print(pay)

# import decimal
# print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

# with decimal.localcontext() as ctx:
#     ctx.prec = 2
#     print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))
# print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

# from fractions import Fraction
# x = Fraction(1, 3)
# y = Fraction(4, 6)

# print(x)
# print(y)

# print(x + y)
# print(x - y)
# print(x * y)

# print(Fraction('.25'))
# print(Fraction('1.25'))
# print(Fraction('.25') + Fraction('1.25'))

# a = 1 / 3.0
# b = 4 / 6.0
# print(a)
# print(b)
# print(a + b)
# print(a - b)
# print(a * b)

# print(0.1 + 0.1 + 0.1 - 0.3)
# from fractions import Fraction
# print(Fraction(1, 10) + Fraction(1, 10) + Fraction(1 , 10) - Fraction(3, 10))

# from decimal import Decimal
# # print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))

# # print(1 / 3)
# # print(Fraction(1, 3))

# # import decimal
# # decimal.getcontext().prec = 2
# # print(Decimal(1) / Decimal(3))

# # print((1 / 3) + (6 / 12))
# # print(Fraction(6, 12))
# # print(Fraction(1, 3) + Fraction(6, 12))

# # decimal.Decimal(str(1/3)) + decimal.Decimal(str(6/12))

# # print(1000.0 / 1234567890)
# # print(Fraction(1000, 1234567890))

# x = Fraction(1, 3)
# print(2.5.as_integer_ratio())
# f = 2.5
# z = Fraction(*f.as_integer_ratio())
# print(z)
# print(x)
# print(x + z)
# print(float(x))
# print(float(z))
# print(float(x+z))
# print(17 / 6)
# print(Fraction.from_float(1.75))
# print(Fraction(*(1.75).as_integer_ratio()))

# print(x)
# print(x + 2)
# print(x + 2.0)
# print(x + (1./3))
# print(x + (4./3))
# print(x + Fraction(4, 3))

# print(4.0 / 3)
# print((4.0 / 3).as_integer_ratio())
# print(x)
# a = x + Fraction(*(4.0 / 3).as_integer_ratio())
# print(a)
# print(22517998136852479 / 13510798882111488.) 
# print(a.limit_denominator(10))

#-----------------------------------------------

# x = set('abcde')
# y = set('bdxyz')

# print(x)
# print(x - y)
# print(x | y)
# print(x & y)
# print(x ^ y)
# print(x > y, x < y)

# print('e' in x)
# print('e' in 'Camelot', 22 in [11,22,33])

# z = x.intersection(y)
# print(z)
# z.update(set(['X', 'Y']))
# print(z)
# z.remove('b')
# print(z)

# for item in set('abc') : print(item * 3)

# S = set([1, 2, 3])
# # print(S | set([3, 4]))
# print(S.union([3, 4]))
# print(S.intersection((1, 3, 5)))
# print(S.issubset(range(-5, 5)))

#-----------------------------------

# set([1, 2, 3, 4])       #вызов во всей версии
# {1, 2, 3, 4}            #вызов в новых версиях с 2.7 и т.д

# print(set([1, 2, 3, 4]))
# print(set('spam'))
# print({1, 2, 3, 4})
# S = {'s', 'p', 'a', 'm'}
# print(S)
# S.add('alot')
# print(S)

# S1 = {1, 2, 3, 4}
# print(S1 & {1, 3})
# print({1, 5, 3, 6} | S1)
# print(S1 - {1, 3, 4})
# print(S1 > {1, 3}) 

# print(S1 - {1, 2, 3, 4})
# print(type({}))
# S = set()
# S.add(1.23)
# print(S)

# print({1, 2, 3}.union([3, 4]))
# print({1, 2, 3}.union({3, 4}))
# print({1, 2, 3}.union(set([3, 4])))
# print({1, 2, 3}.intersection((1, 3, 5)))
# print({1, 2, 3}.issubset(range(-5, 5)))

# print(S)
# #print(S.add([1, 2, 3]))     #ошибка нелья, во множество работают только неизменяемые объекты
# #print(S.add({'a' : 1}))     #ошиька таже, тип нехешируемый
# print(S.add((1, 2, 3)))     # норм так как эт кортеж
# print(S)
# print(S | {(4, 5, 6), (1, 2, 3)})
# print((1, 2, 3) in S)
# print((1, 4, 3) in S)

# print({x ** 2 for x in [1, 2, 3, 4]})
# print({x for x in 'spam'})
# print({c * 4 for c in 'spam'})
# print({c * 4 for c in 'spamham'})
# S = {c * 4 for c in 'spam'}
# print(S)
# print(S | {'mmmm', 'xxxx'})
# print(S & {'mmmm', 'xxxx'})

# L = [1, 2, 1, 3, 2, 4, 5]
# print(set(L))
# L = list(set(L))
# print(L)
# print(list(set(['yy', 'cc', 'aa', 'xx', 'dd', 'aa'])))

# print(set([1, 3, 5, 7]) - set([1, 2, 4, 5, 6]))
# print(set('abcdefg') - set('abdghij'))
# print(set('spam') - set(['h', 'a', 'm']))
# print(set('spam') - set('ham'))

# print(set(dir(bytes)) - set(dir(bytearray)))
# print(set(dir(bytearray)) - set(dir(bytes)))

# L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
# print(L1 == L2)

# print(set(L1) == set(L2))
# print(sorted(L1) == sorted(L2))

# print('spam' == 'asmp', set('spam') == set('asmp'), sorted('spam') == sorted('asmp'))

# enginers = {'bob', 'sue', 'ann', 'vic'}
# managers = {'tom', 'sue'}
# print('bob' in enginers)
# print(enginers & managers)
# print(enginers | managers)
# print(enginers - managers)
# print(managers - enginers)
# print(managers > enginers)
# print({'bob', 'sue'} < enginers)
# print(managers | enginers > managers)
# print(managers ^ enginers)
# print((managers | enginers) - (managers ^ enginers))

#-------------------------------------------------------------
# print(type(True))
# print(isinstance(True, int))
# print(True == 1)
# print(True == -1)
# print(True == 2)
# print(True is 1)
# print(True or False)
# print(True + 4)

#---------------------------------------------------------------------------

# L1 = [2, 3, 4]
# L2 = L1
# L1[0] = 24
# print(L1) #[24, 3, 4]
# print(L2) #[24, 3, 4]

# L1 = [2, 3, 4]
# L2 = L1[:]
# L1[0] = 24
# print(L1) #[24, 3, 4]
# print(L2) #[2, 3, 4]


# import сору
# X = copy.copy(Y)          #Создать "поверхностную" копию верхнего уровня
                            # любого объекта Y
# X = сору.deepcopy(Y)      # Создать глубокую копию любого объек

# L = [1, 2, 3]
# M = L                   #М и L ссылаются на один и тот же объект
# print(L == M)           #Одинаковые значения
# print(L is M)           #Одинаковые объекты


# L = [1, 2, 3]
# M = [1, 2, 3]           #М и L ссылаются на один и тот же объект
# print(L == M)           #Одинаковые значения
# print(L is M)           #Разные бъекты        

# X = 42
# Y = 42
# print(X == Y)
# print(X is Y)

# import sys
# print(sys.getrefcount (1))


#-------------------------------------------------------------------------------------------------

# print("shrubbery", 'shrubbery')

# print('knights"s', "knight's")
# print('knights\'s', "knight\"s")

# title = "Meaning " 'of' " Life"     #неявно 
# print(title)

# title = "Meaning", 'of'," Life"     #явно 
# print(title)

# print("Meaning", 'of',"Life")

# s = 'a\nb\tc'
# print(s)
# print(len(s))

# s = 'a\0b\0c'
# print(s)
# print(len(s))

# s = '\001\002\x03'
# print(s)
# print(len(s))

# S = "s\tp\na\x00m"
# print(S)
# print(len(S))

# x = "C:\py\code"
# x
# print(len)


# myfile = open('C:\new\text.dat', 'w') #проблема из форматирования \ используется для символом избежание этого ниже
# myfile = open(r'C:\new\text.dat', 'w') #проблема решена так r, убирает форматирования, из за чего \ так и читается
# myfile = open('C:\\new\\text.dat', 'w') # альтенатива ставить \\, так будет читаться как одна \

# mantra = """Always look
# on the bright
# side of life.
# """
# print(mantra)

# mantra = "lol\n" \
# "lel\n" \
# " hjahahh"
# print(mantra)

# menu = """span      #комментраии здесь добалвяются к строке
# eggs                #тоже самое
# """
# print(menu)

# menu = (
#     "spam\n"           #коммент ыигнорируется 
#     "eggs\n"            #но символы новой строки не являются автоматическими, покажется как есть в интерактивном запуске, а так нет
# )
# print(menu)

# X = 1
# """
# import os
# print(os.getcws())
# """
# Y = 2

# print(len('abc'))
# print('abc' + 'def')
# print('Ni!' * 4)

# myjob = "hacker"
# for c in myjob: print(c, end=' ')

# print("k" in myjob)
# print("z" in myjob)
# print('spam' in 'abcspamdef')

# S = 'spam'
# print(S[0], S[-2])
# print(S[1:3], S[1:], S[:-1] )
# print(S[0: ])

# S = 'abcdefghijklmnop'
# print(S[1:10:2])
# print(S[::2])
# S = 'hello'
# print(S[::-1])
# S = 'abcedfg'
# print(S[5:1:-1])

# print('spam'[1:3])
# print('spam'[slice(1,3)])
# print('spam'[::-1])
# print('spam'[slice(None,None, -1)])

# S = "42"
# I = 1
# print(S + str(I))
# print(int(S) + I)
# print(str(3.1415), float("1.5"))

# print(ord('s'))
# print(chr(115))

# S = '5'
# S = chr(ord(S) + 1)
# print(S)
# S = chr(ord(S) + 1)
# print(S)

# S = 'spam'
# S = S + 'SPAM!'
# print(S)
# S = S[:4] + 'Burger' + S[-1]
# print(S)

# S = 'splot'
# S = S.replace('pl', 'pamal')
# print(S)

print('That is %d %s bird!' % (1, 'dead'))
print('That is {0}{1} bird!'.format(1, 'dead'))