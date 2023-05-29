def proverka(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2 or x1 + y1 == x2 + y2 or x1 - y1 == x2 - y2

def poisk(n):
    if n == 0:
        return [[]]
    smaller_solutions = poisk(n - 1)
    return [solution + [(n, i + 1)] for i in range(8) for solution in smaller_solutions
            if all(not proverka(n, i + 1, x, y) for x, y in solution)]

print(len(poisk(7)))