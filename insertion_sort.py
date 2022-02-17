a = eval(input('Enter list of numbers:'))
print('Before sorting: ', a)

for i in range(len(a)):
    t = a[i]
    j = i - 1
    while j >= 0 and a[j] > t:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = t

print('After sorting: ', a)