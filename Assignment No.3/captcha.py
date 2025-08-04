import random
correct_userid = "admin"
correct_password="1234"


userid =input("Enter the id:")
password = input("Enter the password:")

if userid == correct_userid and password == correct_password:
    captcha = random.randint(1111,9999)
    print("Captcha:", captcha)

    user_input = int(input("Enter the above captcha number:"))

    if user_input == captcha:
        print("Login successfull.")

    else:
        print("captcha did not match login failed")

else:
    print("Invalid user ID or password")

 
   