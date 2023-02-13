from random import randint

print('Hey! I thought of a number from 0 to 100. Guess it now!')
tries = 0
num = randint(0, 101)

while True:
    tries += 1
    user_number = int(input('Enter a number: '))
    if user_number < num:
        print('Not bad, but my number is larger :) ')
    elif user_number > num:
        print("Oh, it's so big. Take a smaller number :)")
    if user_number == num:
        print(f'Congratulations! You have guessed in {tries} tries! '
              'Thanks for playing!')
        break
