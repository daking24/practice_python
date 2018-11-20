'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

    -Rock beats scissors
    -Scissors beats paper
    -Paper beats rock
'''

import random
    def compare(player1, player2):
        if player1 == player2:
            print("You both put {} {}, It's a draw!!".format(player1, player2))
        elif player1 == 'rock':
            if player2 == 'paper':
                print('Paper wins!!')
            else:
                print('Scissor win!!')

        elif player1 == 'scissor':
            if player2 == 'paper':
                print('Scissor wins!!')
            else:
                print('Rock Wins!!')
        elif player1 == 'paper':
            if player2 == 'rock':
                print('Paper wins!!')
            else:
                print('Scissors wins')
        
        else:
            return('Invalid input')
            sys.exit(0)
            

if __name__ == '__main__':
    print('''
    You Vs The Computer

        Enter Either 
            -rock
            -paper
            -scissor
    ''')
    player1 = input("Choose either rock or paper or scissor > ")
    player2 = random.choice(['rock', 'paper', 'scissor'])

