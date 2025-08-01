days = int(input("Enter the days:"))
year = days//365
days = days % 365
weeks = days // 7
days = days % 7
print("year:",year)
print("weeks:",weeks)
print("days",days)
