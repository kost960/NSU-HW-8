income = 1
past_income = 0
people = -1
average = 0
print('Введите числа:')
while income != 0:
    income = float(input())
    people += 1
    sum = income + past_income
    past_income = sum
    if people >= 1:
        average = sum / people
print(average)
