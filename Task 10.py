N = int(input("Введите число:\n"))
result = []
for i in range(1, N + 1):
    sum = 0
    for y in range(1, i):
        if i % y == 0:
            sum += y
    if sum == i:
        result.append(i)

print(*result if len(result) != 0 else [0], sep='\n')