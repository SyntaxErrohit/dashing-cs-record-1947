country = []
ch = 'y'

while ch == 'y' or ch == 'yes':
    cn = input('Enter country name: ').upper()
    cc = input('Enter capital name: ').upper()
    cp = int(input('Enter population: '))
    country.append((cp, cn, cc))
    ch = input('Do you want to continue: ').lower()

country.sort(reverse=True)
print('Country list...')
print('-'*56)
print(f"{'Country':15}{'Capital':15}{'Population':15}")
print('-'*56)

for cp, cn, cc in country:
    print(f"{cn:15}{cc:15}{cp:15}")

print('-'*56)
