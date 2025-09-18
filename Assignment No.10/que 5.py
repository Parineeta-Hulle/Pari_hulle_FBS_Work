numbers = [12, 34, 56, 78, 12, 34, 12]


num = int(input("Enter a number: "))


count = numbers.count(num)
if count > 0:
    print(num, "is present in the list,", "occurs", count, "time(s).")
else:
    print(num, "is not present in the list.")