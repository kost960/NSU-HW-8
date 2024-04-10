past_number = 0
number = 0
print('Введите числа:')
while number != -1:
    number = int(input())
    if number > past_number:
        past_number = number
print(past_number)