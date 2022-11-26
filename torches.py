from random import randint

INITIAL_COUNT = 15

num = int()
player = 1  # the current player number
counter = INITIAL_COUNT  # the current number of torches

print("It's a game called 'Torches'. There are 15 torches. \n"
      "You move first. You can take from 1 to 3 torches. "
      "Then I move. You will win if you leave me with 0 torches. \n"
      "Good luck! \n")

while counter != 0:
    if player == 1:
        correct = bool()
        while not correct:
            print(f'Your turn. There are {counter} torches.')
            num = int(input('How many torches are you taking?'))
            correct = (num >= 1) and (num <= 3) and (num <= counter)
            if not correct:
                print('Wrong! Try again')

    else:
        num = randint(1, 3)
        if num > counter:
            num = counter
        print(f"My turn. I'm taking {num} torches.")
    counter -= num

    if player == 1:
        player = 2
    else:
        player = 1

if player == 1:
    print('You won! Congratulations!')
else:
    print("You lost. Don't get upset, try again!")
