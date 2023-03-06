def mult(a):
    n = len(a)
    key = []
    res = ''
    for i in range(n):
        key.append(ord(a[i]))
    for i in range(n):
        res += str(round(n * ((key[i] * 0.668) % 1)))
        #n * (key * 0.1 - (key * 0.1) // 1))
    return res


a = input()
#key = 25
print(mult(a))