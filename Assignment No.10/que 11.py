numbers = [12, 24, 36, 48, 60, 72, 80, 90]


m = int(input("Enter first divisor (m): "))
n = int(input("Enter second divisor (n): "))

divisible_numbers = [num for num in numbers if num % m == 0 and num % n == 0]

print("Numbers divisible by", m, "and", n, ":", divisible_numbers)