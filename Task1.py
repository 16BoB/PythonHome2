# 1) Вводим с клавиатуры целое число X и У.
# Выводим на экран количество чисел между Х и У, которые делятся на 2 и 3

num1 = int(input("Введите от какого числа начать: "))
num2 = int(input("Введите до какого числа: "))

if num2 == num1:
    print("Числа равны, нет промежутка")
elif num2 < num1:
    temp = num1
    num1 = num2
    num2 = temp

count = 0
for i in range(num1, num2 + 1):
    if i%2 == 0 and i%3 == 0:
        count +=1


print(f"чисел в промежутке от {num1} до {num2}, которые делятся на 2 и 3 = {count}")