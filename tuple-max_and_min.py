t = ()
ch = 'y'

while ch == 'y':
    e = int(input('Enter number: '))
    t += (e,)
    ch = input('Do you want to continue:(y/n) ')

print('Given tuple is:', t)
print('Largest number is:', max(t))
print('Smallest number is:', min(t))