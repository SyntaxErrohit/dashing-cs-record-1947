l = int(input("Enter lines: "))
n = 1
a = 97

for i in range(1, l + 1):
    for z in range(i):
        if i % 2 == 1:
            print(n, end=" ")
            n += 1
        else:
            print(chr(a), end=" ")
            a += 1
    print()
