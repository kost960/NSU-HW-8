stars = '*'
space = ' '
N = int(input('Введите число: '))
for i in range(1, N + 1):
    sum = (space * (N-i))+(stars*i)
    print(sum)