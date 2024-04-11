x = input('Введите число: ')
y = x.isdigit()
while y != True:
    x = input('Ошибка. Попробуйте ещё раз. Введите число: ')
    y = x.isdigit()
print('Введено целое число: ', x)