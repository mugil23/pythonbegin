s = 0
n,a,d = map(int,input().split(" "))
for i in range(0,n):
	s = s + a
	a = a + d
print(s)
