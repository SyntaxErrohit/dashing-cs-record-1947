d = {}
z = int(input('Enter number of students: '))

for i in range(z):
    r = int(input('Enter roll number: '))
    n = input('Enter name: ')
    m = int(input('Enter marks: '))
    d[r] = [n,m]

print('Students who scored above 75...')

for i in d:
    if d[i][-1] > 75:
        print('Roll number:', i)
        print('Name:', d[i][0])
        print('Marks:', d[i][-1])
