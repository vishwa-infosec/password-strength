import string
password = input("Enter password:")
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digit = string.digits
symbol = string.punctuation
isalpha = 0
isalphasmall = 0
isdigit = 0
issymbol = 0
for i in password:
    if i in lower:
        isalpha = 1
    elif i in upper:
        isalphasmall = 1
    elif i in digit:
        isdigit = 1
    elif i in symbol:
        issymbol = 1

total = isalpha + isalphasmall + isdigit + issymbol

if total == 4:
    print("Password is very strong")
elif total == 3:
    print("Password is strong")
elif total == 2:
    print("Password is average")
elif total == 1:
    print("password is weak")
elif total == 0:
    print("Password is very weak")
