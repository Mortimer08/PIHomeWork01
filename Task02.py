# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

result = True
for x in range(2):
    for y in range(2):
        for z in range(2):
            left_item = not (x or y or z)
            right_item = not x and not y and not z
            if left_item != right_item:
                result = False
if result:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')
