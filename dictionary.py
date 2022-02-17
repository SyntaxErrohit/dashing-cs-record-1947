n = int(input('Enter number of products: '))
d = {}

for i in range(n):
    p = input('Enter product name: ')
    d[p] = int(input('Enter price: '))

print(d)

while True:
    c = input('Do you want to search: (y/n) ')
    if c != 'y':
        break
    s = input('Enter product name to check: ')
    if s in d:
        print(d[s])
    else:
        print('Sorry, product not found')