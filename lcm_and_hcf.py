a = int(input("Enter a: "))
b = int(input("Enter b: "))
hcf = 1

if a > b:
    a, b = b, a
for i in range(1, b + 1):
    if a % i == 0 and b % i == 0:
        hcf = i
lcm = (a * b) // hcf

print("LCM of", a, "and", b, "is", lcm)
print("HCF of", a, "and", b, "is", hcf)
