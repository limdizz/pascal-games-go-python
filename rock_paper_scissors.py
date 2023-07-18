import random

print('Hello! This is Rock Paper Scissors game. You move first.\n'
      'You should choose R (Rock) or P (Paper) or S (Scissors),'
      ' then computer moves.\nA rock can beat scissors,'
      ' a paper can beat the rock and scissors can beat the paper.\nGood luck!\n')


def play_again_suggestion():
    player_permission = input('Do you want to try again? (Y/N)\n').upper()
    if player_permission == 'Y':
        game()
    else:
        print('OK. You can always come back. Thank you for playing!')


def win_message():
    print('Congratulations! You are the winner!')


def lose_message():
    print("You lost! Don't get upset, take another chance :)")


def game():
    player_letter = ''
    while not (player_letter == 'R' or player_letter == 'P' or player_letter == 'S'):
        player_letter = input('Would you like to choose R or P or S?\nYour move: ').upper()
        if player_letter == 'R':
            computer_letter = random.choice(['P', 'S'])
            if computer_letter == 'S':
                print(f"Computer's move: {computer_letter}")
                win_message()
                play_again_suggestion()
            else:
                print(f"Computer's move: {computer_letter}")
                lose_message()
                play_again_suggestion()

        elif player_letter == 'P':
            computer_letter = random.choice(['R', 'S'])
            if computer_letter == 'R':
                print(f"Computer's move: {computer_letter}")
                win_message()
                play_again_suggestion()
            else:
                print(f"Computer's move: {computer_letter}")
                lose_message()
                play_again_suggestion()

        elif player_letter == 'S':
            computer_letter = random.choice(['P', 'R'])
            if computer_letter == 'P':
                print(f"Computer's move: {computer_letter}")
                win_message()
                play_again_suggestion()
            else:
                print(f"Computer's move: {computer_letter}")
                lose_message()
                play_again_suggestion()


game()
