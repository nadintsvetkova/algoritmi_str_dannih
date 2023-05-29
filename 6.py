# alpha = 0.5  # коэффициент сглаживания
prev_output = 0  # предыдущее значение выходного сигнала

inputs = [1, 2, 3, 4, 5]  # список входных значений

for input in inputs:
    output = 0.5 * input + (1 - 0.5) * prev_output
    prev_output = output
    print("output:", output)

