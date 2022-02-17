s = []
for z in range(40):
    print('Enter details for student', z + 1)
    n = input('Enter name: ').upper()
    e = float(input('Enter english marks: '))
    p = float(input('Enter physics marks: '))
    c = float(input('Enter chemistry marks: '))
    m = float(input('Enter maths marks: '))
    cs = float(input('Enter cs marks: '))
    s.append((n, e, p, c, m, cs))
    print()
    print(f"{'Name':<15}{'English':>12}{'Physics':>12}{'Chemistry':>12}",end='')
    print(f"{'Maths':>12}{'Cs':>12}{'Total':>8}{'Percentage':>12}{'Grade':^10}")
    print('-' * 102)
    for n, e, p, c, m, cs in s:
        n = n.strip()
        t = e + p + c + m + cs
        a = t / 5
        if a > 90 and a <= 100: g = 'A1'
        elif a > 80 and a <= 90: g = 'A2'
        elif a > 70 and a <= 90: g = 'B1'
        elif a > 60 and a <= 90: g = 'B2'
        elif a > 50 and a <= 90: g = 'C1'
        elif a > 40 and a <= 90: g = 'C2'
        elif a > 32 and a <= 90: g = 'D'
        elif a > 20 and a <= 32: g = 'E1'
        else: g = 'E2'
        print(f"{n:<15}{e:>12}{p:>12}{c:>12}", end='')
        print(f"{m:>12}{cs:>12}{t:>8}{a:>12}{g:^10}")
        print('-' * 102)
    print()