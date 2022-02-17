e = []
for z in range(20):
    print('Enter data of employee:', z + 1)
    p = input('Enter PAN number: ')
    n = input('Enter name: ')
    s = float(input('Enter salary: '))
    e.append((p, n, s))
    print('\nEmployee tax calculation...')
    print(f"{'PAN no.':12}{'Name':25}{'Annual Salary':>15}\
    {'Tax':>15}{'Cess':>15}{'Surcharge':>15}{'Total Tax':>15}")
    print('-' * 118)
    for p, n, s in e:
        t = sc = 0
        if s > 250000:
            if s > 250000 and s <= 500000:
                t = s * 0.05 - 12500
            elif s > 500000 and s <= 1000000:
                t = s * 0.2 - 87500
            else:
                t = s * 0.3 - 187500
        c = t * 0.04
        if s > 5000000 and s <= 10000000:
            sc = t * 0.1
        elif s > 10000000:
            sc = t * 0.15
        tt = t + c + sc
        print(f"{p:12}{n:25}{s:15.2f}{t:15.2f}{c:15.2f}{sc:15.2f}{tt:15.2f}")
        print('-' * 118)
        print()