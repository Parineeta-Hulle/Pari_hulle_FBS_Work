def reverse_number(num, rev=0):
    if num == 0:             
        return rev
    digit = num % 10            
    return reverse_number(num // 10, rev * 10 + digit)


n = int(input("Enter a number: "))
print("Reversed number:", reverse_number(n))