num = int(input("Enter the three digit number:"))
temp = num

d1 = temp % 10
temp = temp // 10

d2 = temp % 10
temp = temp // 10

d3 = temp % 10
temp = temp // 10

print("D1:",d1)
print("D2:",d2)
print("D3:",d3)



