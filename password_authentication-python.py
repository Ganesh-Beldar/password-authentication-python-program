password = ["Mahesh@123","Sagar@321","Pass@123"]

user_pass = input("Enter user password:")

if user_pass in password:
    print("Login Successful")
else:
    print("Wrong Password")