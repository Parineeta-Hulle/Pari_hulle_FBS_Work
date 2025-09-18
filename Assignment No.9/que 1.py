def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

def factorial_sum(n):
    if n == 1:
        return 1  
    return factorial(n) + factorial_sum(n - 1)


n = int(input("Enter a positive integer n: "))

print(f"The sum of the series 1! + 2! + ... + {n}! is:", factorial_sum(n))