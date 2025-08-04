a = int(input("Enter the a:"))
b =int(input("Enter the b:"))
c =int(input("Enter the c:"))
if (a == b == c):
    print("equilateral triangle")
elif(a == b or b == c or a == c):
    print("isolation triangle")
else:
    print("scelan triangle")
    