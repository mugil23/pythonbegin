number = input('input : ')
try:
    val = int(number)
    if number == str(number)[::-1]:
        print('yes')
    else:
        print('no')
except ValueError:
    print("That's not a valid number, Try Again !")
