kolstup = int(input('Введите количество ступенек лестницы: '))
# 1111 121 211 112 22 31 13
shagi = [0 for i in range(kolstup)]
if kolstup <= 0:
    print('Лестницы не существует..')
else:
    for i in range(kolstup):
        if i == 0:
            shagi[i] = 1
        elif i == 1:
            shagi[i] = 2
        elif i == 2:
            shagi[i] = 4
        else:
            shagi[i] = shagi[i-1] + shagi[i-2] + shagi[i-3]

print('Количество возможных способов преодолеть лестницу:', shagi[-1])