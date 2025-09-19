str1 = input("Enter first string: ")
str2 = input("Enter second string: ")


c1 = 0
for _ in str1:
    c1 += 1

c2 = 0
for _ in str2:
    c2 += 1

if c1 > c2:
    print("Larger string:", str1)
elif c2 > c1:
    print("Larger string:", str2)
else:
    print("Both strings are equal in length")
