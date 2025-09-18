def armstrong_sum(num, power):
    if num == 0:         
        return 0
    digit = num % 10
    return (digit ** power) + armstrong_sum(num // 10, power)

n = int(input("Enter a number: "))
power = len(str(n))        
if armstrong_sum(n, power) == n:
    print(n, "is an Armstrong number.")
else:
    print(n, "is not an Armstrong number.")