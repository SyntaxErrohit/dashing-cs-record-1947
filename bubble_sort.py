l = eval(input('Enter a list of numbers: '))
print('Before sorting: ', l)

for i in range(len(l)):
    for j in range(len(l) - i - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]

print('After sorting: ', l)