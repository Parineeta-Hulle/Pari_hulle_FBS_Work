second = int(input("Enter the second:"))
Hours = second // 3600
second = second % 3600
Min = second // 60
second = second % 60

print(f 'hours{Hours} , Min{Min} , Second{second}')