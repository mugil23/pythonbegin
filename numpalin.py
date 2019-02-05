numb = input('input : ')
try:
    val = int(numb)
    if numb == str(numb)[::-1]:
        print('yes')
    else:
        print('no')
except ValueError:
    print("That's not a valid number, Try Again !")
