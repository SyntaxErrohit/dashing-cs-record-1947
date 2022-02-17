n = input("Enter your name: ")
u = int(input("Enter number of units used: "))

if u <= 100:
    r = 50
elif 100 < u and u <= 200:
    r = u*0.5
elif 200 < u and u <= 400:
    r = u*0.8-60
else:
    r = u-140

print("Name:", n)
print("Units used:", u)
print("Total Bill Amount:", r)
