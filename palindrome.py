n = int(input('Enter a number: '))
copy = n
rev = 0

while n>0:
    digit = n%10
    rev = rev*10 + digit
    n = n//10

if copy == rev:
    print('It is a palindrome number')
else:
    print('It is not a palindrome number')