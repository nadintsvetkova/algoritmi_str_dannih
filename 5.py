
class ThreeStacks:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.array = [None] * (stack_size * 3)  # Одномерный массив для трех стеков
        self.pointers = [-1, -1, -1]  # Указатели вершин стеков

    def is_full(self, stack_number):
        return self.pointers[stack_number] == self.stack_size - 1

    def is_empty(self, stack_number):
        return self.pointers[stack_number] == -1

    def push(self, stack_number, value):
        if self.is_full(stack_number):
            print("Стек переполнен")
            return

        self.pointers[stack_number] += 1
        index = stack_number * self.stack_size + self.pointers[stack_number]
        self.array[index] = value

    def pop(self, stack_number):
        if self.is_empty(stack_number):
            print("Стек пуст")
            return None

        index = stack_number * self.stack_size + self.pointers[stack_number]
        value = self.array[index]
        self.array[index] = None
        self.pointers[stack_number] -= 1
        return value


# Пример использования
stacks = ThreeStacks(3)  # Создаем трехстековый массив с размером стеков 3

stacks.push(0, 1)  # Добавляем элемент 1 в стек 1
stacks.push(1, 2)  # Добавляем элемент 2 в стек 2
stacks.push(2, 3)  # Добавляем элемент 3 в стек 3

print(stacks.array)  # Выводим текущее состояние массива

value = stacks.pop(0)  # Удаляем элемент из стека 1
print("Удаленный элемент из стека 1:", value)

print(stacks.array)  # Выводим текущее состояние массива
