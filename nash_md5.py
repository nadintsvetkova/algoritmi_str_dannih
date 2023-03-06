import math
text = input('Введите строку: ')
print('Исходный текст: ', text)
# Этап 0. Приведение текста в двоичный вид.
text_dv = ''
for bukva in text:
    text_dv += bin(ord(bukva)).replace('0b', '')

# Этап 1. Выравнивание потока.
iznach_dlina = len(text_dv)
text_vir = text_dv + '1'
while (len(text_vir) <= 448) or ((len(text_vir) - 448) % 512 != 0):
    text_vir += '0'

# Этап 2. Добавление длины.
if iznach_dlina >= 2**64:
    iznach_dlina = iznach_dlina % 2**64
bin_dlina = bin(iznach_dlina).replace('0b', '')
while len(bin_dlina) < 64:
    bin_dlina = '0' + bin_dlina
text_poln = text_vir + bin_dlina
# print('Выравненные текст в двоичном формате вместе с его длиной:', text_poln)

# Этап 3. Инициализация буфера.
buffer = [bin(int('01234567', 16)).replace('0b', ''), bin(int('89abcdef', 16)).replace('0b', ''),
          bin(int('fedcba98', 16)).replace('0b', ''), bin(int('76543210', 16)).replace('0b', '')]
S = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20,
     5, 9, 14, 20, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 6, 10, 15, 21, 6, 10, 15,
     21, 6, 10, 15, 21, 6, 10, 15, 21]
def F(x, y, z):
    return x & y | ~x & z
def G(x, y, z):
    return x & z | y & ~z
def H(x, y, z):
    return x ^ y ^ z
def I(x, y, z):
    return y ^ (x | ~ z)
def vibor(x, y, z, vibr_num):
    if vibr_num == 0:
        return F(x, y, z)
    elif vibr_num == 1:
        return G(x, y, z)
    elif vibr_num == 2:
        return H(x, y, z)
    else:
        return I(x, y, z)
# Этап 5. Шумовая составляющая.
T = []
for i in range(1, 65):
    T.append(int(2 ** 32 * abs(math.sin(i))))

# Этап 6. Функция для одного этапа.
for blocks in range(0, len(text_poln), 512):
    block = text_poln[blocks: blocks+512]
    X = []
    for j in range(0, 512, 32):
        X.append(block[j:j+32])
    i_T = 0
    it = 0
    for i in range(4):
        for k in range(16):
            a = buffer[0]
            b = buffer[1]
            c = buffer[2]
            d = buffer[3]
            rez_raunda = bin((int(b, 2) + (int(a, 2) + vibor(int(b, 2), int(c, 2),
                                             int(d, 2), i) + int(X[k], 2) + T[i_T]))).replace('0b', '')
            a = d
            d = c
            c = b
            b = b + bin((int(rez_raunda, 2) << S[it])).replace('0b', '')
            i_T += 1
            it += 1
    buffer[0], buffer[1], buffer[2], buffer[3] = buffer[0] + a, buffer[1] + b, buffer[2] + c, buffer[3] + d
otvet = ''
for i in range(4):
    otvet += hex(int(buffer[i], 2)).replace('0x', '').upper()
print('Зашифрованное сообщение: ', otvet)

