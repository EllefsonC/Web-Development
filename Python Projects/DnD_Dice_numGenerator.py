import random

diceMap = {       

        1: list(range(1, 5)),   #d4
        2: list(range(1, 7)),   #d6
        3: list(range(1, 13)),  #d12
        4: list(range(1, 21)),  #d20
        5: list(range(1, 41))   #d40
        }


while True:
    try:
        #initial input
        while True:
            try:
                print('Welcome to the Dice App, please choose which dice you would like to roll. You may choose more than one!\n'
                    '1. 4-sided die\n'
                    '2. 6-sided die\n'
                    '3. 12-sided die\n'
                    '4. 20-sided die\n'
                    '5. 40-sided die\n'
                    'Please chose which dice you would like to roll and we will present the results! Please separate values with white space, example: "1 3 4"\n'
                    'Please enter values: ')

                playerChoice = [int(i) for i in input().split()]
                #ensures input is integer, and .split() allows for multiple user numbers for one input
                
                if all(c in [1, 2, 3, 4, 5] for c in playerChoice):
                    # input validation. Here the user input is compared so that all inputs are within the array. This specific line is called a generator expression. If all options are true, they break loop into dice mapping, else reloop
                    
                    print(f'You chose {playerChoice}, lets go ahead and give them a roll!')
                    break
                else:
                    print('Error, incorrect values. Please try again')
                    continue 
                
                
            except ValueError:
                print('Invalid input, please try again')
                continue
        #Actual dice rolling
        for i in playerChoice:
            dice = diceMap[i]
            result = random.choice(dice)
            print(f'You rolled d{len(dice)}: {result}')
        
        #Play again prompt/input validation
        while True:
            try: 
                print('Would you like to play again? Input "Y" for yes or "N" for no')
                playAgain = input().lower()
                if playAgain == 'y':
                    break
                elif playAgain =='n':
                    print('Thanks for playing! Have a good day!')
                    quit()
                else:
                    print('Invalid input, please try again')
                    continue
            except ValueError:
                continue
    
   
    except ValueError:
        continue
