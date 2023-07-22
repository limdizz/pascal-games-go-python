import random

print('Hi. You and 5 of your opponents (handling by computer) roll two dices.\n'
      'The player with the highest amount of points wins. Good luck! :)')


def game():
    while True:
        player_dice1 = random.randint(1, 6)
        player_dice2 = random.randint(1, 6)

        opponent1_dice1 = random.randint(1, 6)
        opponent1_dice2 = random.randint(1, 6)

        opponent2_dice1 = random.randint(1, 6)
        opponent2_dice2 = random.randint(1, 6)

        opponent3_dice1 = random.randint(1, 6)
        opponent3_dice2 = random.randint(1, 6)

        opponent4_dice1 = random.randint(1, 6)
        opponent4_dice2 = random.randint(1, 6)

        opponent5_dice1 = random.randint(1, 6)
        opponent5_dice2 = random.randint(1, 6)

        player_answer = input('\nWill you roll the dice? (Y/N)\n').upper()
        all_scores = []
        if player_answer == 'Y':
            print(f'Your roll: {player_dice1, player_dice2} '
                  f'= {player_dice1 + player_dice2} points')
            all_scores.append(player_dice1 + player_dice2)

            print(f"First opponent's roll: {opponent1_dice1, opponent1_dice2} "
                  f"= {opponent1_dice1 + opponent1_dice2} points")
            all_scores.append(opponent1_dice1 + opponent1_dice2)

            print(f"Second opponent's roll: {opponent2_dice1, opponent2_dice2} "
                  f"= {opponent2_dice1 + opponent2_dice2} points")
            all_scores.append(opponent2_dice1 + opponent2_dice2)

            print(f"Third opponent's roll: {opponent3_dice1, opponent3_dice2} "
                  f"= {opponent3_dice1 + opponent3_dice2} points")
            all_scores.append(opponent3_dice1 + opponent3_dice2)

            print(f"Fourth opponent's roll: {opponent4_dice1, opponent4_dice2} "
                  f"= {opponent4_dice1 + opponent4_dice2} points")
            all_scores.append(opponent4_dice1 + opponent4_dice2)

            print(f"Fifth opponent's roll: {opponent5_dice1, opponent5_dice2} "
                  f"= {opponent5_dice1 + opponent5_dice2} points")
            all_scores.append(opponent5_dice1 + opponent5_dice2)

            print(all_scores)

            high_score = max(all_scores)

            if all_scores[0] == high_score:
                if all_scores.count(all_scores[0]) == 1:
                    print(f"You win with {high_score} points!")

            if all_scores[1] == high_score:
                if all_scores.count(all_scores[1]) == 1:
                    print(f"First opponent wins with {high_score} points.")

            if all_scores[2] == high_score:
                if all_scores.count(all_scores[2]) == 1:
                    print(f"Second opponent wins with {high_score} points.")

            if all_scores[3] == high_score:
                if all_scores.count(all_scores[3]) == 1:
                    print(f"Third opponent wins with {high_score} points.")

            if all_scores[4] == high_score:
                if all_scores.count(all_scores[4]) == 1:
                    print(f"Fourth opponent wins with {high_score} points.")

            if all_scores[5] == high_score:
                if all_scores.count(all_scores[5]) == 1:
                    print(f"Fifth opponent wins with {high_score} points.")

            if all_scores[5] == high_score == all_scores[4] or \
                    all_scores[5] == high_score == all_scores[3] or \
                    all_scores[5] == high_score == all_scores[2] or \
                    all_scores[5] == high_score == all_scores[1] or \
                    all_scores[5] == high_score == all_scores[0] or \
                    all_scores[4] == high_score == all_scores[3] or \
                    all_scores[4] == high_score == all_scores[2] or \
                    all_scores[4] == high_score == all_scores[1] or \
                    all_scores[4] == high_score == all_scores[0] or \
                    all_scores[3] == high_score == all_scores[2] or \
                    all_scores[3] == high_score == all_scores[1] or \
                    all_scores[3] == high_score == all_scores[0] or \
                    all_scores[2] == high_score == all_scores[0] or \
                    all_scores[2] == high_score == all_scores[1] or \
                    all_scores[1] == high_score == all_scores[0]:
                print("It's a draw!")

        elif player_answer == 'N':
            break

        else:
            print('Seems like you have written a wrong letter. Check your answer.')
            game()


game()
