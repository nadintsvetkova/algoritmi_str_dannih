

def poisk_missing_number(massiv):
    for i in range(min(massiv), max(massiv)):
        if i not in massiv:
            return i

massive = [4, -1, 1, 5, -7, -3, 2, -10]

result = poisk_missing_number(massive)
sorted_massive = sorted(massive)
print("Неотсортированный массив: ", massive)
print("Отсортированный массив: ", sorted_massive)
print("Наименьшее пропущенное число: ", result)


