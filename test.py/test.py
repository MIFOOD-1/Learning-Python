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
# M = [[1,2,3], [4,5,6], [7,8,9]]
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

# print('That is %d %s bird!' % (1, 'dead'))
# print('That is {0}{1} bird!'.format(1, 'dead'))

# S = 'spam'
# result = S.find('pa')
# print(result)

# S = 'spammy'
# S = S[:3] + 'xx' + S[5:]
# print(S)

# S = 'spammy'
# S = S.replace('mm', 'xx')
# print(S)

# S = 'spammymm'
# S = S.replace('mm', 'xx')
# print(S)

# S = 'xxxxSPAMxxxxSPAMxxxx'
# where = S.find('SPAM')
# print(where)
# S = S[:where] + 'EGGS' + S[(where+4):]
# print(S)

# S = 'spammy'
# L = list(S)
# print(L)

# L[3] = 'x'
# L[4] = 'x'
# print(L)

# S = ''.join(L)
# print(S)

# line = 'aaa bbb ccc'
# col1 = line[0:3]
# col3 = line[8:]
# print(col1)
# print(col3)

# cols = line.split()
# print(cols)

# line = 'bob,hacker,40'
# print(line.split(','))

# line = "i'mSPAMaSPAMlumberjack"
# print(line.split("SPAM"))
# line = ' '.join(line.split("SPAM"))
# print(line)

# line = "The knights who say Ni!\n"
# print(line.rstrip())
# print(line.upper())
# print(line.isalpha())
# print(line.endswith('Ni!\n'))
# print(line.startswith('The'))

# print(line.find('Ni') != -1)
# print('Ni' in line)
# sub = 'Ni!\n'
# print(line.endswith(sub))
# print(line[-len(sub):] == sub)

# exclamation = 'Ni'
# print('The knights who say %s!' % exclamation)
# print('%d %s %g you' % (1, 'spam', 4.0))
# print('%s -- %s -- %s' % (42, 3.14159, [1, 2, 3]))
# print('%(qty)d more %(food)s' % {'qty' : 1, 'food': 'spam'})

# reply = """
# Greetings...
# Hello %(name)s
# Your age is %(age)s
# """

# values = {'name': 'Bob', 'age': 40}
# print(reply % values)

# food = 'spam'
# qty = 10
# print(vars())

# template = '{0}, {1} and {2}'
# print(template.format('spam', 'ham', 'eggs'))

# template = '{motto}, {pork} and {food}'
# print(template.format(motto='spam', pork='ham', food='eggs'))

# template = '{motto}, {0} and {food}'
# print(template.format('ham', motto = 'spam', food = 'eggs'))

# template = '{}, {} and {}'
# print(template.format('spam', 'ham', 'eggs'))

# template = '%s, %s and %s'
# print(template % ('spam', 'ham', 'eggs'))

# template = '%(motto)s, %(pork)s and %(food)s'
# print(template % dict(motto='spam', pork = 'ham', food = 'eggs'))

# X = '{motto}, {0} and {food}'.format(42, motto= 3.14, food= [1, 2])
# print(X)

# print(X.split(' and' ))
# Y = X.replace('and', 'but under no circumstances')
# print(Y)

# import sys
# print('My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'}))
# print('My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'laptop'}))

# somelist = list('SPAM')
# print(somelist)
# print('first={0[0]}, third={0[2]}'.format(somelist))
# print('first={0}, last={1}'.format(somelist[0], somelist[-1]))
# print('first={0}, last={1}'.format(somelist, somelist[-1]))
# parts = somelist[0], somelist[-1], somelist[1:3]
# print(parts)
# print('first={0}, last={1}, middle={2}'.format(*parts))

# print('{0:10} = {1:10}'.format('spam', 123.4567))
# print('{0:>10} = {1:<10}'.format('spam', 123.4567))
# print('{.platform:>10} = {[kind]:<10}'.format(sys,dict(kind='laptop')))

# print('{0:e}, {1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159))
# print('{0:f}, {1:.2f}, {2:06.2f}'.format(3.14159, 3.14159, 3.14159))
# print('{0:X}, {1:b}, {2:o}'.format(3,5, 1))
# print('{0:X}, {1:o}, {2:b}'.format(255, 255, 255))

# print(bin(255), int('11111111', 2), 0b11111111)
# print(hex(255), int('FF', 16), 0xFF)
# print(oct(255), int('377', 8), 0o377)

# print('{0:.2f}'.format(1 / 3.0))
# print('%.2f' % (1 /30))

# print('{0:.{1}f}'.format(1 / 3.0, 4))
# print('%.*f' % (4, 1 / 3.0))

# print('{0:.2f}'.format(1.2345))
# print(format(1.2345, '.2f'))
# print('%.2f' % 1.2345)

# print("%s, %s and %s" % (3.14, 42, [1, 2]))
# print('My %(kind)s runs %(platform)s' % {'kind' : 'laptop', 'platform': sys.platform})
# print('My %(kind)s runs %(platform)s' % dict(kind='laptop', platform=sys.platform))
# somelist = list('SPAM')
# parts = somelist[0], somelist[-1], somelist[1:3]
# print('first=%s, last=%s, middle=%s' % parts)

# data = dict(platform= sys.platform, kind='laptop')
# print('My {kind:<8} runs {platform:>8}'.format(**data))
# print('My %(kind)-8s runs %(platform)8s' % data)

# print('{0:b}'.format((2 ** 16) - 1))
# # print('%b' % ((2 ** 16) - 1))       #error
# print(bin((2 ** 16 - 1)))
# print('%s' % bin((2 ** 16) - 1))
# print('{}'.format(bin((2 ** 16) - 1)))
# print('%s' % bin((2 ** 16) - 1)[2:])

# D = dict(name= 'Bob', job= 'dev')
# print('{0[name]} {0[job]} {0[name]}'.format(D))
# print('{name} {job} {name}'.format(**D))
# print('%(name)s %(job)s %(name)s' % D) 

#----------------------------------------------
# print(len([1, 2, 3]))
# print([1, 2, 3] + [4, 5, 6])
# print(['Ni!'] * 4)

# print(str([1, 2]) + '34')
# print([1, 2] + list("34"))
# #print([1, 2] + 34)          #error
# print([1, 2] + ["34"])

# print(3 in [1, 2, 3])
# for x in [1, 2, 3]:
#     print(x, end=' ')

# res = [c * 4 for c in 'SPAM']
# print(res)

# res = []
# for c in 'SPAM':
#         res.append(c * 4)
# print(res)

# print(list(map(abs, [-1, -2, 0, 1, 2])))

# L = ['spam', 'Spam', 'SPAM!']
# print(L[2])
# print(L[-2])
# print(L[1:])

# L = ['spam', 'Spam', 'SPAM!']
# L[1] = 'eggs' 
# print(L)
# L[0:2] = ['eat', 'more']
# print(L)
# L[0:4] = ['spam', 'SPAM']
# print(L)

# L = [1, 2, 3]
# L[1:2] = [4,5]  #замена\вставка
# print(L)

# L[1:1] = [6,7]  #вставка
# print(L)

# L[1:2] = []     #удаление
# print(L)

# L = [1]
# L[:0] = [2, 3, 4]
# print(L)

# L[len(L):] = [5, 6, 7]
# print(L)

# L.extend([8, 9, 10])
# print(L)

# L = ['eat', 'more', 'SPAM']
# L.append('please')
# print(L)
# L.sort()
# print(L)
# L.append(['please', 'lol'])
# print(L)
# print(L[len(L) - 1][1])

# L = ['abc', 'ABD', 'aBe']
# L.sort()
# print(L)

# L = ['abc', 'ABD', 'aBe']
# L.sort(key=str.lower)
# print(L)

# L.sort(key=str.lower, reverse=True)
# print(L)

# L = ['spam', 'eggs', 'ham']
# print(L.index('eggs'))
# L.insert(1, 'toast')
# print(L)
# L.remove('eggs')
# print(L)
# print(L.pop(1))
# print(L)
# print(L.count('spam'))

# L = ['spam', 'eggs', 'ham', 'toast']
# del L[0]
# print(L)
# del L[1:]
# print(L)

#--------------------------------------------------------
# D = {'spam' : 2, 'ham' : 1, 'eggs' : 3}
# # print(D['spam'])
# # print(D)

# # print(len(D))
# # print('ham' in D)
# # print(list(D.keys()))

# D['ham'] = ['grill', 'bake', 'fry']
# print(D)
# del D['eggs']
# print(D)
# D['brunch'] = 'Bacon'
# print(D)
# D = {'spam' : 2, 'ham' : 1, 'eggs' : 3}
# print(list(D.values()))
# print(list(D.items()))
# print(list(D))

# print(D.get('spam'))
# print(D.get('spams'))
# print(D.get('toast', 88))

# print(D)
# D = {'spam' : 2, 'ham' : 1, 'eggs' : 3}
# D2 = {'toast': 4, 'muffin':5, 'eggs':10}
# D.update(D2)
# print(D)

# print(D.pop('muffin'))
# print(D)

# table = {'1975': 'Holy Grail',
#          '1979': 'Life of Brian',
#          '1983': 'The Meaning of Life'}

# year = '1983'
# movie = table[year]
# print(movie)

# for year in table:
#     print(year + '\t' + table[year])


# table = {'Holy Grail': '1975',
#          'Life of Brian': '1979',
#          'The Meaning of Life': '1983'}

# print(list(table.items()))
# print([title for (title, year) in table.items() if year == '1975'])
# Matrix = {}
# Matrix[(2,3,6)] = 10 
# if(2, 3, 6) in Matrix:
#         print(Matrix[(2, 3, 6)])
# else:
#     print(0)

# try:
#     print(Matrix[(2, 3, 6)])
# except KeyError:
#      print(0)

# print(Matrix.get((2, 3, 4), 0))
# print(Matrix.get((2, 3, 6), 0))

# rec = {}
# rec['name'] = 'Bob'
# rec['age'] = 40.5
# rec['job'] = 'developer/manager'
# print(rec['name'])

# print(list(zip(['a', 'b', 'c'] , [1, 2, 3])))
# a = list(zip(['a', 'b', 'c'] , [1, 2, 3]))
# print(a)
# print(a[1])
# D = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
# print(D)

# D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1,2,3])}
# print(D)

# D = {x: x ** 2 for x in [1, 2, 3, 4]}
# print(D)

# D= {c: c* 4 for c in 'SPAM'}
# print(D)

# D = {c.lower(): c + '!' for c in['SPAM', 'EGGS', 'HAM']}
# print(D)

# D = dict.fromkeys(['a', 'b', 'c'], 0)
# print(D)
# D = {k:0 for k in['a', 'b', 'c']}
# print(D)
# D = dict.fromkeys('spam')
# print(D)

# D = {'a' : 1, 'b' : 2, 'c' : 3}
# # print(D)
# K = D.keys()
# V = D.values()
# # print(list(K))
# # print(list(V))
# del D['b']
# # print(D)
# # print(list(K))
# # print(list(V))

# print(K, V)

# print(K | {'x' : 4})
# #print(V & {'x' : 4}.values()) #error

# D = {'a': 1, 'b' : 2, 'c' : 3}
# print(D.keys() & D.keys())
# print(D.keys() & {'b'})
# print(D.keys() & {'b': 1})
# print(D.keys() | {'b', 'c', 'd'})

# D = {'a' : 1}
# print(D)
# print(list(D.items()))
# print(D.items() | D.keys())
# print(D.items() | D)
# print(D.items() | {('c', 3), ('d', 4)})
# print(dict(D.items() | {('c' , 3) , ('d', 4)}))

#-------------------------------------------------------
# print((1, 2) + (3, 4))
# print((1, 2) * 4)
# T = (1, 2, 3, 4)
# print(T[0], T[1:3])

# x = (40) # целое число
# x = (40,) #кортеж

# T = ('cc', 'aa', 'dd', 'bb')
# tmp = list(T)
# tmp.sort()
# print(tmp)
# T = tuple(tmp)
# print(T)
# T = ('cc', 'aa', 'dd', 'bb')
# print(T)
# print(sorted(T))
# T = sorted(T)
# print(T)
# T = (1, 2, 3, 4, 5)
# L = [x + 20 for x in T]
# print(L) 

# T  = (1, 2, 3, 2, 4, 2)
# print(T.index(2))
# print(T.count(2))

# T = (1, [2, 3], 4)
# T[1][0] = 'spam'
# print(T)

# bob = ('Bob', 40.5, ['dev', 'mgr'])
# print(bob)
# print(bob[0], bob[2], bob[2][0])
# from collections import namedtuple
# Rec = namedtuple('Rec1', ['name', 'age', 'jobs'])
# bob = Rec('Bob', age = 40.5, jobs=['dev', 'mgr'])
# print(bob)
# print(bob[0], bob[2])
# print(bob.name, bob.jobs)

# O = bob._asdict()
# print(O['name'], O['jobs'])

# bob = {'name': 'Bob', 'age' : 40.5, 'jobs': ['dev', 'mgr']}
# job, name, age = bob.values()
# print(name, job)

#-----------------------------------
# mygile = open('myfile.txt', 'w')
# print(mygile.write('hello text file\n'))
# print(mygile.write('goodbye text file\n'))
# mygile.close()
# myfile = open('myfile.txt')
# print(myfile.readline())
# print(myfile.readline())
# print(myfile.readline())

# print(open('myfile.txt').read())

# for line in open('myfile.txt'):
#     print(line, end='')

# X, Y, Z = 43, 44, 45
# S = 'Spam'
# D = {'a':1, 'b':2}
# L = [1, 2, 3]
# F = open('datafile.txt', 'w')
# F.write(S + '\n')
# F.write('%s, %s, %s\n' % (X, Y, Z))
# F.write(str(L) + '$' + str(D) + '\n')
# F.close()

# chars = open('datafile.txt').read()
# print(chars)

# F = open('datafile.txt')
# line = F.readline()
# print(line.rstrip())

# line = F.readline()
# parts = line.split(',')
# print(parts)

# numbers = [int(P) for P in parts]
# print(numbers)

# for x in parts:
#     print(int(x) + 2)

# line = F.readline()
# print(line)
# parts = line.split('$')
# print(parts)
# print(eval(parts[0]))
# objects = [eval(P) for P in parts]
# print(objects)


# D = {'a': 1, 'b': 2}
# F = open('datafile.pkl', 'wb')
# import pickle
# pickle.dump(D, F)
# F.close()

# F = open('datafile.pkl', 'rb')
# E = pickle.load(F)
# print(E)

# name = dict(first='Bob', last = 'Smith')
# rec = dict(name = name, job=['dev', 'mgr'], age=40.5)
# print(rec)
# import json
# print(json.dumps(rec))
# json.dump(rec, fp=open('testjson.txt', 'w'), indent=4)
# print(open('testjson.txt').read())
# P = json.load(open('testjson.txt'))
# print(P)

# F = open('data.bin', 'wb')
# import struct
# data = struct.pack('>i4sh', 7, b'spam', 8)
# print(data)
# F.write(data)
# F.close()

# F = open('data.bin', 'rb')
# data = F.read()
# print(data)
# values = struct.unpack('<i4sh', data)
# print(values)

# L = [4, 5, 6]
# X = L * 4
# Y = [L] * 4
# print(X)
# print(Y)
# L[1] = 0
# print(X)
# print(Y)

#-----------------------------------------
# while True:
#     reply = input('Enter text:')
#     if reply == 'stop' : break
#     print(reply.upper())

# while True:
#     reply = input('Enter text:')
#     if reply == 'stop' : break
#     print(int(reply) ** 2)
# print('Bye')

# S = '123'
# T = 'txt'
# print(S.isdigit(), T.isdigit())

# while True:
#     reply = input('Enter text: ')
#     if reply == 'stop':
#         break
#     elif not reply.isdigit():
#         print('Bad' * 8)
#     else:
#         print(int(reply) ** 2)
# print('Bye')

# while True:
#     reply = input('Enter text: ')
#     if reply == 'stop': break
#     try:
#         num = int(reply)
#     except:
#         print('Bad!' * 8)
#     else:
#         print(num ** 2)
# print('Bye')

# while True:
#     reply = input("Enter text: ")
#     if reply == 'stop':
#         break
#     elif not reply.isdigit():
#         print('Bad!' * 8)
#     else:
#         num = int(reply)
#         if num < 20:
#             print('low')
#         else:
#             print(num ** 2)
# print('Bye')

#--------------------------------
# nudge = 1
# wink = 2
# A, B = nudge, wink
# print(A, B)
# [C, D] = [nudge, wink]
# print(C, D)

# nudge = 1
# wink = 2
# nudge, wink = wink, nudge
# print(nudge, wink)

# L = [1, 2, 3, 4]
# while L:
#         front, L = L[0], L[1:]
#         print(front, L)

seq = [1, 2, 3, 4]
# a, b, c, d = seq
# print(a, b, c, d)
# #a, b = seq              #error
# a, *b = seq
# print(a)
# print(b)

# *a, b = seq
# print(a)
# print(b)

# a, *b, c = seq
# print(a)
# print(b)
# print(c)

# a, *b, c, d = seq
# print(a)
# print(b)
# print(c)
# print(d)

# a, *b, = 'spam'
# print(a, b)

# a, *b, c = 'spam'
# print(a, b, c)

# S = 'spam'
# print(S[0], S[1:])
# print(S[0], S[1:3], S[3])

# L = [1, 2, 3, 4]
# while L:
#     front, *L = L
#     print(front, L)

# seq = [1, 2, 3, 4]
# a, *b = seq
# print(a,b)

# a, b = seq[0], seq[1:]
# print(a,b)

# *a, b = seq
# print(a, b)

# a,b  = seq[:-1], seq[-1]
# print(a,b)

# for(a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
#     print(a, b, c)

#---------------------------------------------------
# a = b = c = 'spam'
# print(a,b,c)

# a = b = []
# b.append(42)
# print(a, b)

# L = [1, 2]
# L = L + [3]
# print(L)
# L.append(4)
# print(L)
# L = L + [5, 6]
# print(L)
# L.extend([7, 8])
# print(L)
# L += [9,10]
# print(L)

# L = [1, 2]
# M = L
# L = L + [3,4]
# print(L)
# print(M)

# L = [1,2]
# M = L
# L += [3,4]
# print(L)
# print(M)

#-------------------------------------------------------------------------------------------
# print([object, ...][, sep=' '][, end='\n'][,file=sys.stdout][, flush=False])

# print()

# x = 'spam'
# y = 99
# z = ['eggs']
# print(x, y, z)

# print()
# print(x, y, z, sep='')
# print(x, y, z, sep=', ')

# print()
# print(x, y, z, end='')
# print(x, y, z, end=''); print(x, y, z)
# print(x, y, z, end='hahaha\n')

# print(x, y, z, end='', sep='   \n     ')

# print(x, y, z, sep='   ', file=open('data.txt', 'w'))
# print(x, y, z)
# print(open('data.txt').read())


# text = '%s: %-.4f, %05d' % ('Result', 3.14159, 42)
# print(text)
# print('%s: %-.4f, %05d' % ('Result', 3.14159, 42))


# import sys
# sys.stdout.write('hello world\n')

# import sys
# temp = sys.stdout
# sys.stdout = open('log.txt', 'a')
# print('spam')
# print(1, 2, 3, end= '')
# sys.stdout.close()
# sys.stdout = temp

# print('bback here')
# print(open('log.txt').read())

import sys
sys.stderr.write(('Bad!' * 8) + '\n')

