p1 = int(input("Age of person 1:"))
p2 = int(input("Age of person 2:"))
p3 = int(input("Age of person 3:"))
p4 = int(input("Age of person 4:"))
p5 = int(input("Age of person 5:"))
ticket_amt = int(input("Enter ticket amount:"))

if(p1<12):
    disc_amt = ticket_amt * 0.3
    amt1 = ticket_amt-disc_amt
elif(p1>59):
    disc_amt = ticket_amt*0.5
    amt1 = ticket_amt-disc_amt
else:
    amt1 = ticket_amt

if(p2<12):
    disc_amt = ticket_amt*0.3
    amt2 = ticket_amt - disc_amt
elif(p2>59):
    disc_amt = ticket_amt*0.5
    amt2 = ticket_amt-disc_amt
else:
    amt2= ticket_amt

if(p3<12):
    disc_amt = ticket_amt *0.3
    amt3 = ticket_amt-disc_amt
elif(p3>59):
    disc_amt = ticket_amt * 0.5
    amt3 = ticket_amt-disc_amt
else:
    amt3 = ticket_amt

if(p4<12):
    disc_amt = ticket_amt*0.3
    amt4 = ticket_amt-disc_amt
elif(p4>59):
    disc_amt = ticket_amt*0.5
    amt4 = ticket_amt-disc_amt
else:
    amt4 = ticket_amt

if(p5<12):
    disc_amt = ticket_amt*0.3
    amt5 = ticket_amt-disc_amt
elif(p5>59):
    disc_amt = ticket_amt*0.5
    amt5 = ticket_amt - disc_amt
else:
    amt5 = ticket_amt

total_amt = amt1+amt2+amt3+amt4+amt5
print(total_amt)