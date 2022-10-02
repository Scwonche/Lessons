# 1 нечетные позиции
a = [1, 5, 3, 3, 5, 6]
k = 0
for i in range(len(a)):
    if i % 2 != 0:
        k += a[i]
print(k)
# 2 подсчет пар списка
for i in range(len(a) // 2):
    print(a[i] + a[len(a) - i - 1])
# 3 список вещественных чисел
b = [1.2, 8.6, 7.3, 10.5]
c = []
for x in b:
    l = x - int(x)
    c.append(l)
print(*c)
print(max(c) - min(c))


# 4 преобразование  n - число, m - основание, куда переводить
def tras(n, m=2):
    s = ''
    while n > 0:
        s += str(n % m)
        n = n // m
    return s[::-1]


n = 1432
print(tras(n))


# 5 негафиббоначи
fib1 = fib2 = 1
f = [-1,1,0,1]
n = int(input())

for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    f.append(fib2)
    if i % 2 != 0:
        f = [-fib2] + f
    else:
        f = [fib2] + f
print(*f)