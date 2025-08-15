start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

for num in range(start, end + 1):
   
    digits = str(num)
    power = len(digits)
    
    sum_of_powers = 0
    for d in digits:
        sum_of_powers += int(d) ** power
    
    if sum_of_powers == num:
        print(num)


        