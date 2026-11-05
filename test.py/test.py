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

D = {}
D['name'] = 'Bob'
D['job'] = 'dev'
D['age'] = 40
print(D)
print(D['name'])





