while True:
    while True:
        try:
            print ('Welcome back!\n'
                   'Please enter a number:')
            number1 = float(input())
            break   
        except ValueError:
            print('Incorrect input, please try a number')
            
    while True:     
        try:
            print('Please input a second number')
            number2 = float(input())
            break
        except:
            print('Incorrect input, please try a number')



    while True:
        try:
            print('please select an operation for these two numbers:\n'
            '1. Addition\n'
            '2. Subtration\n'
            '3. Multiplication\n'
            '4. Division')
            operation = int(input())
            if operation in [1,2,3,4]:
                break
            else:
                print('Incorrect input, please try one of the selections.')
        except ValueError:
            #ValueError is a built in exception for when invalid data types are input
            print('Incorrect input, please try one of the selections.')



    number3 = None
    #number3 is declare as a variable, intended to be overwritten

    while True:
        try:
            if operation == 1:
                operation = '+'
                number3 = number1 + number2
                break
        
            elif operation == 2:
                operation = '-'
                number3 = number1 - number2 
                break
            
            elif operation == 3:
                operation = '*'
                number3 = number1 * number2
                break
                    
            elif operation == 4:
                operation = '/'
                if number2 != 0:
                    number3 = number1 / number2
                    break
                else:
                    if number2 == 0:
                        print('#### Error! Cannot divide by 0! ####')
                        break
        except ValueError:
            break

    print(f'{float(number1)} {operation} {float(number2)} is = {number3}')

    while True:
        try:
            print('Would you like to try another calculation?\n'
                '1. Yes\n'
                '2. No')
            
            #input must be an integer
            another_Calc = int(input())
            #another caluclation or exit script   
            if another_Calc == int(1):
                break
            elif another_Calc == int(2):
                print('Have a good day!')
                quit()
            #input validation
            else:
                print('Invalid input, please select 1 or 2')
          
        
        except ValueError:
            print('Invalid input, please select 1 or 2')
            continue
