import random

# Hash-map for dice values
diceMap = {       
    'D4': list(range(1, 5)),
    'D6': list(range(1, 7)),
    'D12': list(range(1, 13)),
    'D20': list(range(1, 21)),
    'D40': list(range(1, 41))
}


def rollDice(diceType):
    """Roll a single die of the specified type and return the result"""
    if diceType in diceMap:
        dice = diceMap[diceType]
        return random.choice(dice)
    return None


if __name__ == '__main__':
    print('Starting Dice Game...')
    
    #this was needed in order to make the GUI work, which was only taking strings. This was an easier work around that did not require a complete rewrite of the code and allows both files to work independently and be usable together in a main.py in the future. 
    diceMapNumbers = {1: 'D4', 2: 'D6', 3: 'D12', 4: 'D20', 5: 'D40'}
    
    while True:
        try:
            # Get player input
            while True:
                try:
                    print('Welcome to the Dice App, please choose which dice you would like to roll. You may choose more than one!\n'
                        '1. 4-sided die\n'
                        '2. 6-sided die\n'
                        '3. 12-sided die\n'
                        '4. 20-sided die\n'
                        '5. 40-sided die\n'
                        'Please enter values (e.g., "1 3 4"): ')

                    playerChoice = [int(i) for i in input().split()]
                    
                    if all(c in [1, 2, 3, 4, 5] for c in playerChoice):
                        print(f'You chose {playerChoice}, lets go ahead and give them a roll!')
                        break
                    else:
                        print('Error, incorrect values. Please try again')
                        continue   
                except ValueError:
                    print('Invalid input, please try again')
                    continue
            
            # Roll each die
            for num in playerChoice:
                diceType = diceMapNumbers[num]
                result = rollDice(diceType)
                
                print(f'You rolled {diceType}: {result}')
                
                # Critical hit or fail logic
                if diceType == 'D20' and result == 20:
                    print('***You hit a Natural 20! Critical hit!***')
                elif diceType == 'D20' and result == 1:
                    print('Oh no! You rolled a critical fail!')
            
            # Play again prompt
            while True:
                try: 
                    print('Would you like to play again? Input "Y" for yes or "N" for no')
                    playAgain = input().lower()
                    if playAgain == 'y':
                        break
                    elif playAgain == 'n':
                        print('Thanks for playing! Have a good day!')
                        quit()
                    else:
                        print('Invalid input, please try again')
                        continue
                except ValueError:
                    continue
        
        except ValueError:
            continue
