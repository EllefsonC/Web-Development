import random

rock = 'r'
paper = 'p'
scissor = 's'
options = ['r', 'p', 's']

#rock > scissor
#rock < paper
#paper < scissor

while True:
    while True:
        try:
            print('Welcome to Rock/Paper/Scissors\n'
                'Type R for Rock\n'
                'Type P for Paper\n'
                'Type S for Scissors\n'
                'Please input your selection:')
            player = input().lower()
            if player in options:
                break
            else:
                print('Invalid input, please try again')
                        
        except ValueError:
            continue
    computer = random.choice(options)

    print(f'Your selection was: {player.upper()}, and The computer chose: {computer.upper()}')


    if  (player == rock and computer == scissor) or \
        (player == scissor and computer == paper) or \
        (player == paper and computer == rock):
        print('Player Wins:)')
        
    elif player == computer:
        print('This game is a tie')
        
    else:
        print('The Computer Wins!')
        
    while True:
        try:
            print('Would you like to play again? Please select the following options to continue:\n'
                  '1. Again Please\n'
                  '2. No Thanks')
            user = int(input())
            if user == 1:
                break
            elif user == 2:
                print('Have a Good Day!')
                quit()
            else:
                if user != [1, 2]:
                    print('Invalid entry, please try a whole number from the list!')   
                
        except ValueError:
            continue
