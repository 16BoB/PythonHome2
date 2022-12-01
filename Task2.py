# 2) Вводим с клавиатуры целое число X
# Далее вводим Х целых чисел.
# Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.

input_nums = int(input("Сколько чисел будете вводить: "))

max_num = float('-inf')
max_num2 = max_num
for i in range(input_nums):
    new_num = int(input(f"Введите {i + 1} число: "))
    if new_num > max_num or new_num > max_num2:
        if new_num > max_num:
            max_num2 = max_num
            max_num = new_num
        else: max_num2 = new_num
       
print(f"Первый максимальный элемент:{max_num}")
print(f"Второй максимальный элемент:{max_num2}")

