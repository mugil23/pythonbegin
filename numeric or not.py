user_input = input ()
try:
   a = int(user_input)
   print("Yes")
except ValueError:
   print("no")
