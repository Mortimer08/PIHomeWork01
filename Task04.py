# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

print('Номер четверти координатной плоскости')
quarter = int(input())
if quarter < 1 or quarter > 4:
    print('Введено некорректное значение')
elif quarter == 1:
    print('x > 0; y > 0')
elif quarter == 2:
    print('x < 0; y > 0')
elif quarter == 3:
    print('x < 0; y < 0')
elif quarter == 4:
    print('x > 0; y < 0')

