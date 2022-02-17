n = int(input('Enter even number of element: '))
l = []

while n%2 == 1:
    n = int(input('Enter even number of element: '))

for i in range(n):
    e = int(input('Enter number: '))
    l.append(e)

print('Before swapping:', l)

for i in range(0,n,2):
    l[i], l[i+1] = l[i+1], l[i]

print('After swapping:', l)