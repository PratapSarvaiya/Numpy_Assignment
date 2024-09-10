name = input("Please enter your name: ")
email = input("Please enter your email: ")
password = input("Please enter your password: ")

if name == " ":
    print("Please enter a valid name,can not empty")
else:
    if "@" not in email:
        print("Please enter a valid email")
    else:
        if len(password) < 0:
            print("No password entered,pis provide a valid password")
        else:
            print("Login/registration is successful")