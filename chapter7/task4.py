# 4. Дан s = "a,b,c,d". Получи список ['a','b','c','d'] 
# и обратно строку "a-b-c-d" (через join).

s = "a,b,c,d"
s = list(s[::2])
s = "-".join(s)
print(s)