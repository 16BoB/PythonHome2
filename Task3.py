# 3) Вводим с клавиатуры целое число - это зарплата.
# Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
# И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 3 рублевых и 1 рублевых

input_num = int(input("Введите число: "))

count_money = 0
while(input_num > 0):
    if input_num > 25:
        print(f'25ти рублёвых купюр - {input_num//25}')
        count_money += input_num//25
        input_num %= 25
    elif input_num >= 10:
        print(f'10ти рублёвых купюр - {input_num//10}')
        count_money += input_num//10
        input_num %= 10
    elif input_num >= 7:
        print(f'7ми рублёвых купюр - {input_num//7}')
        count_money += input_num//7
        input_num %= 7
    elif input_num >= 3:
        print(f'3х рублёвых купюр - {input_num//3}')
        count_money += input_num//3
        input_num %= 3
    else:
        print(f'рублёвых купюр - {input_num//1}')
        count_money += input_num//1
        input_num %= 1
print('Общее минимальное количество купюр = ', count_money)