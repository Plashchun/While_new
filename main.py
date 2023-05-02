n = int(input('enter from number: '))
i = 0
summ = 0
while i <= n:
    if i % 3 == 0:
        summ += i
    i += 1

print(f'Sum of numbers {n}: {summ}')