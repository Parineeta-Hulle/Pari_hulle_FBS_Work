num =int(input("Enter the three digit number:"))
if 100 <= num <=999:
    first = num //100
    second = (num //10) % 10
    third = num % 10


    if first == 2 * second and third == second //2:
        print("yes, you have done it")
    else:
        print("please try next time")
else:
     print("not a three digit")