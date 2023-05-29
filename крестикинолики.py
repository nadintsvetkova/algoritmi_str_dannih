pobeda = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
stroka = input('Введите строки игрового поля без пробела(1 - крестик, 0 - нолик): ')
cross = set()
nul = set()
for i in range(len(stroka)):
    if stroka[i] == '1':
        cross.add(i+1)
    else:
        nul.add((i+1))
countcross = 0
countnul = 0

for elem in pobeda:
    if elem&cross == elem:
        countcross += 1
    elif elem&nul == elem:
        countnul += 1

if countcross > countnul:
    print('Победили крестики!')
elif countnul > countcross:
    print('Победили нолики!')
else:
    print('Ничья!')
