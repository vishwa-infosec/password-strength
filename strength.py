def strength(password):
    # initialize boolean variables
    lowercase = False
    uppercase = False
    numbers = False
    special = False
    # initialize percentage as 0 to change later
    percentage = 0
    # iterate letters in password to check if it contains lower,upper,number,special character
    for letter in password:
        if letter in "abcdefghijklmnopqrstuvwxyz":
            lowercase = True
        if letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            uppercase = True
        if letter in "1234567890":
            numbers = True
        if letter in "!@#$%^&*()_-+=|\}{][':;>.<,?/`~:/":
            special = True
    # add percentage of password according to conditions
    if lowercase == True:
        percentage += 20
    if uppercase == True:
        percentage += 20
    if numbers == True:
        percentage += 20
    if special == True:
        percentage += 20
    if len(password) >= 16:
        percentage += 20
    print("Your password is {} percent Strong\n".format(percentage))
    if lowercase == True and uppercase == True and numbers == True and special == True:
        print("Your Passwrd is highly strong\n")
    if lowercase == False:
        print("Lowercase is missing in your password\n")
    if uppercase == False:
        print("Uppercase is missing in your password\n")
    if numbers == False:
        print("Number is missing in your password\n")
    if special == False:
        print("Special Character is missing in your password\n")
    if len(password) < 16:
        print("Hackers nowadays are capable of compromising password that are less than 16 digit, We recommend using atleast 16 digit password\n")


# get input of password from user
password = input("Enter Your Password: ")
strength(password)
