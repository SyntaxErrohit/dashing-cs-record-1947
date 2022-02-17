s1 = input("Enter string: ")
s2 = s1[0].upper()
i = 1

while i < len(s1):
    s2 += s1[i]
    if s1[i] == " ":
        s2 += s1[i + 1].upper()
        i += 1
    i += 1

print("Original string:", s1)
print("Capitalized string:", s2)
