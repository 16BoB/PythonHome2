# 4) Вводим с клавиатуры многозначное число
# Необходимо узнать и сказать последовательность цифр этого числа при просмотре слева направо упорядочена по возрастанию или нет.
# Например 1579 - да ( 1 меньше 5, 5 меньше 7, а 7 меньше 9), 1427 - нет

str_num = input("Введите число: ")

split_num = 0
temp = 10
int_num = int(str_num)
for i in range(len(str_num)):
    split_num = int_num % 10
    if split_num < temp:
        temp = split_num
        int_num//=10
        if int_num == 0: print('да')
    else: 
        print('нет')
        break