num = int(input("Enter Number :- "))
temp = num
rev = 0
while(num > 0):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if (temp == rev):
    print("The Number is Pallindrome")
else:
    print("The Number is Not Pallindrome")
