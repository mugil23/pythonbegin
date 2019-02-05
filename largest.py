print("enter three numbers:")
 
x = int(input())
y = int(input())
z = int(input())
 
if x>y and x>z:
	print(x, " is largest")
elif y>x and y>z:
	print(y, " is largest")
else:
	print(z, " is largest")
