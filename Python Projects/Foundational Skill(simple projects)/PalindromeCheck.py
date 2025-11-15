num = 121.0

# Mathmatical approach to determining if a number is a palindrome
def palindromeCheckInt(x):
    originalNum = x
    
    
    reverseNum = 0
    while x > 0:
        lastNum = x % 10
        reverseNum = (reverseNum * 10) + lastNum
        x = x // 10

    print(f'Original Number: {originalNum}, Reversed Number: {reverseNum}')
    if originalNum == reverseNum:
        print(f'Int number is Palindrome')
    else:
        print('Int number is not a palindrome')

#simpler string conversion and comparison, using slicing to inverse string and compare values
def palindromeCheckStr(x):
    str_x = str(x)
    
    if str_x[::-1] == str_x:
        print('Yes, palindrome')
    else:
        print('No, this is not a palindrome')

palindromeCheckInt(num)
