x = int(input("Enter x: "))
n = int(input("Enter n: "))
summ = 0

for i in range(1, n + 1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    summ += x ** i / fact

print(summ)
