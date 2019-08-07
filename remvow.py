m = input("")
print(len(m))
print(m)
s = ""
for i in m:
  if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
    pass
  else:
    s+=i
m = s
print(m)
