user = input("Enter the User name:")
password = int(input("Enter the password:"))

if user == 'admin' and password == 10:
    print("Welcome ",user)
else:
    print("Access Denied")
