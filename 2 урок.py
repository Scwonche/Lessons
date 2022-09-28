# 1 сумма цифр
k = False
while k == False:
    try:
        n = float(input('Введите число'))
        k = True
        s = list(str(n))
        s.remove('.')
        print(sum(map(int,s)))
    except ValueError:
        print('Еще раз')
# 2 набор произведений
n = int(input('введите число'))
s = [1]
for i in range(2,n + 1):
    x = i * s[i - 2]
    s.append(x)
print(*s)

# 3 список
a = []
for i in range(1,n+1):
    t = (1+1/i)**i
    a.append(round(t,1))
print(sum(a))

# 4 произведение по позициям
k1,k2 = map(int,input('введите позиции через пробел').split())
n = int(input('Введите размер списка'))
b = [i for i in range(-n,n+1)]
print(*b)
print(b[k1-1]*b[k2-1])
# 5 перемешивание списка (условие же выполнено?))

import random

n = int(input('Введите размер списка'))
ind = [i for i in range(n)]
print(ind)
print(random.sample(ind,n))