# 1 День недели
import math

n = int(input('введите день недели'))
if n < 1 or n > 7:
    print('нет такого дня недели')
elif n == 6 or n == 7:
    print('да')
else:
    print('нет')

# 2 Логическое выражение
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            print(x, y, z, int(not (x or y or z) == (not x and not y and not z)))

# 3 Координаты по четвертям
x, y = map(int, input('введите координаты через пробел').split())
if x == 0 or y == 0:
    if x == y == 0:
        print('начало координат')
    elif x != 0:
        print('ось Х')
    else:
        print('ось Y')
elif x > 0 and y > 0:
    print('1 четверть')
elif x > 0 > y:
    print('4 четверть')
elif x < 0 < y:
    print('2 четверть')
else:
    print('3 четверть')
# 4 Обратная задача координат(ограничение надо ли?)
k = int(input('введите номер четверти'))
if k == 1:
    print('x>0;y>0')
elif k == 2:
    print('x<0;y>0')
elif k == 3:
    print('x<0;y<0')
else:
    print('x>0;y<0')
# 5 Расстояние между точками
x1,y1 = map(int, input('введите 1 точки координаты через пробел').split())
x2,y2 = map(int, input('введите 2 точки координаты через пробел').split())
r = math.sqrt((x2-x1)**2+(y2-y1)**2)
print(f'расстояние между точками А({x1},{y1})и B({x2},{y2}) равно {r:.2f}')