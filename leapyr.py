yr = int(input("enter the year: "))

if yr % 4 == 0 and yr % 100 != 0:
    print(yr, "is a Leap Year")
elif yr % 100 == 0:
    print(yr, "is not a Leap Year")
elif yr % 400 ==0:
    print(yr, "is a Leap Year")
else:
    print(yr, "is not a Leap Year")
