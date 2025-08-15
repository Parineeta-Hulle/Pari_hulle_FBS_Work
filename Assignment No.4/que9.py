start = int(input("Start: "))
end = int(input("End: "))
div = int(input("Divisor: "))

for i in range(start, end + 1):
    if i % div == 0:
        print(i)