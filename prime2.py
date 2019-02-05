number = int(input(" "))

# prime number is always greater than 1
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print('no')
            break
    else:
        print('yes')
else:
  print(number, "is not a prime number")
