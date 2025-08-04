a = int(input("Enter the a:"))
b =int(input("Enter the b:"))
c =int(input("Enter the c:"))
if(a + b > c and a + c > b and b + c > a):
    print("valid triangle")
else:
    print("not valid")