a=list()
b=input()
try:
	c=int(b)
except:
	print("invalid input")
else:
	for i in range(1,6):
		a.append(str(i*c))
print(" ".join((a))) 
