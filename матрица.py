m = int(input('Введите количество строк: '))
n = int(input('Введите количество столбцов: '))

matrix = [[0 for _ in range(n)] for _ in range(m)]
for i in range(m):
    stroka = input(f'Введите {i+1} строчку: ')
    c = 0
    for elem in stroka.split(' '):
        matrix[i][c] = int(elem)
        c += 1
print(matrix)

isk_chislo = int(input('Введите искомое значение: '))

def poisk_po_stolb(matrix, chislo, stolb):
    for i in range(m):
        if matrix[i][stolb] == chislo:
            print('Индекс элемента:', i + 1, stolb + 1)
            exit()
        elif matrix[i][stolb] > chislo:
            return i
    print('Такого элемента нет в матрице')
    exit()

def poisk_po_stroke(matrix, chislo, stroka):
    for i in range(n-1, -1, -1):
        if matrix[stroka][i] == chislo:
            print('Индекс элемента:', stroka + 1, i + 1)
            exit()
        elif matrix[stroka][i] < chislo:
            return i
    print('Такого элемента нет в матрице')
    exit()

stb = n-1
stk = m-1
while stb > -1 and stk > -1:
    stk = poisk_po_stolb(matrix, isk_chislo, stb)
    stb = poisk_po_stroke(matrix, isk_chislo, stk)







