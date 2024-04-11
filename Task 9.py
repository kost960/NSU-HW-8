N = int(input("Введите число: "))
lst=[]
for i in range(2, N+1):
    for j in lst:
        if i % j == 0:
            break
    else:
        lst.append(i)
for i in range(0, len(lst)):
    print(int(lst[i]))
