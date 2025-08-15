num = 145
temp = num
sum = 0
while(temp > 0):
    d = temp % 10
    temp = temp // 10
    i = 1
    fact =1
    while(i<= d):
        fact *=i
        i+=1
    sum +=fact
if(sum == num):
            print("it is strong no")
else:
            print("not strong no")
