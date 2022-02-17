n = int(input('Enter a number: '))
factors = 0

for i in range(1, n+1):
    if n%i == 0:
        factors = factors + 1

if factors == 2:
    print('It is a prime number')
else:
    print('It is not a prime number')