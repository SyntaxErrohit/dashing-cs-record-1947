n = int(input('Enter a number: '))
copy = n
total = 0

while n > 0:
    f = 1
    digit = n % 10
    for i in range(1, digit+1):
        f *= i
    total += f
    n //= 10

if copy == total:
    print('Special Number')
else:
    print('Not a Special Number')
