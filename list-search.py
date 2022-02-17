l = []
ch = 'y'

while ch == 'y':
    e = input('Enter element: ')
    l.append(e)
    ch = input('Do you want to continue:(y/n) ')

s = input('Enter element to search: ')
if s in l:
    print('Element', s, 'is found at', l.index(s))
else:
    print('Element not found')