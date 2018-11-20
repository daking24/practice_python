'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

    - Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''
import random

def guess_number():
    my_number = random.randint(1,3)
    tries = 0
    while tries  < 3:
        your_number = int(input('Enter Your Number: '))
        if your_number > my_number:
            print("Too High!!")
            print("My number was",my_number)
        elif your_number < my_number:
            print('Too Low!!')
            print("My number was", my_number)

        elif your_number == my_number:
            print('Correct!!')
            print('Impressive!!')
            print('Number of tries', tries)
            break
        tries += 1


if __name__ == '__main__':    
    guess_number()

