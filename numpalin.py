number = input('Enter any number : ')
try:
    val = int(number)
    if number == str(number)[::-1]:
        print('The given number is PALINDROME')
    else:
        print('The given number is NOT a palindrome')
except ValueError:
    print("That's not a valid number, Try Again !")
