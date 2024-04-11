x = '123456789'
sum = 0
for a in range(1, 10):
    sum = int(x[:a]) * 8 + (a)
    print(sum)
print()
sum2 = 0
for b in range(1, 10):
    sum2 = int(x[:b]) * 9 + (b+1)
    print(sum2)
print()
z = '111111111'
for c in range(1, 10):
    sum3 = int(z[:c])**2
    print(sum3)