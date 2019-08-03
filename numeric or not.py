user_input = input ()
try:
   a = int(user_input)
   print("yes")
except ValueError:
   print("no")
