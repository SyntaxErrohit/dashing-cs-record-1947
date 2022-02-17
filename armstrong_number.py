n = int(input('Enter a number: '))
copy = n
total = 0

while n > 0:
    digit = n % 10
    total += (digit**3)
    n //= 10

if copy == total:
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')
