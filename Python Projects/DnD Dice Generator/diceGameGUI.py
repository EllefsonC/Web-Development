from ctypes import windll

# Fix for high DPI monitors
try:
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

from diceGame import diceMap, rollDice
import tkinter as tk

if __name__ == '__main__':
    print('Loading GUI...')
    
    # Creating start window
    root = tk.Tk()
    root.geometry('1000x800')
    root.configure(bg='#1a1a1a')
    root.title('DnD Dice Engine')
    root.iconbitmap('DiceGame/images/dice.ico')
    
    label = tk.Label(root, text='Welcome to the DnD Dice Engine!', font=('Arial', 28), bg="#540D9C", fg='white')
    label.pack(pady=30)

    textbox = tk.Text(root, width=40, height=7, wrap="word", font=('Arial', 25), bg='#1a1a1a', fg='white', borderwidth=0)
    textbox.insert("1.0", 'This script is intended for DnD players who forget their dice before their dungeon crawl.\n')
    textbox.insert("end", 'Enjoy!', 'right')
    textbox.tag_configure('right', justify='right')
    textbox.configure(state='disabled')
    textbox.pack()

    def begin_main_program():
        root.destroy()
        
        #New window for dice selection
        rootNew = tk.Tk()
        rootNew.geometry('1000x800')  
        rootNew.title('Select Your Dice')
        rootNew.configure(bg='#1a1a1a')
        rootNew.iconbitmap('DiceGame/images/dice.ico')
        #Dice counting dictionary
        diceCount = {
            'D4': 0,
            'D6': 0,
            'D12': 0,
            'D20': 0,
            'D40': 0
        }
        
        countLabels = {}

        #Increment dice count
        def incrementDice(diceType):
            diceCount[diceType] += 1
            countLabels[diceType].config(text=str(diceCount[diceType]))
        
        #Decrement dice count
        def resetDice(diceType):
            if diceCount[diceType] > 0:
                diceCount[diceType] -= 1
            countLabels[diceType].config(text=str(diceCount[diceType]))
        
        #Roll all selected dice
        def handleRoll():
            results = []
            
            #Loop through each dice type and roll the specified count
            for diceType, count in diceCount.items():
                for i in range(count):
                    result = rollDice(diceType)
                    results.append(f'{diceType}: {result}')
                    
                    #Critical hit/fail logic
                    if diceType == 'D20' and result == 20:
                        results.append('***Natural 20! Critical hit!***')
                    elif diceType == 'D20' and result == 1:
                        results.append('Oh no! Critical fail!')
            
            #Display results
            resultDisplay.configure(state='normal')
            resultDisplay.delete('1.0', 'end')
            resultDisplay.insert('1.0', '\n'.join(results) if results else 'No dice selected!')
            resultDisplay.configure(state='disabled')
        
        #Instructions at top, this feels like so much code for one sentence.
        textbox1 = tk.Text(rootNew, width=50, height=1, wrap='word', font=('Arial', 26), bg='#1a1a1a', fg='white', borderwidth=0)
        textbox1.insert("1.0", 'Please choose your dice, you may choose multiple!')
        textbox1.configure(state='disabled')
        textbox1.pack(pady=20)
        
        #Main container for left and right side
        mainFrame = tk.Frame(rootNew, bg='#1a1a1a')
        mainFrame.pack(fill='both', expand=True, padx=20, pady=10)
        
        #Dice Selectors
        leftFrame = tk.Frame(mainFrame, bg='#1a1a1a')
        leftFrame.pack(side='left', fill='both', expand=True, padx=10)
        
        tk.Label(leftFrame, text='Select Dice:', font=('Arial', 18, 'bold'), bg='#1a1a1a', fg='white').pack(pady=10)
        
        diceFrame = tk.Frame(leftFrame, bg='#1a1a1a')
        diceFrame.pack(pady=10)
        
        #Create counter controls for each dice type
        for diceType in diceCount.keys():
            frame = tk.Frame(diceFrame, bg='#1a1a1a')
            frame.pack(pady=8)
            
            tk.Label(frame, text=diceType, font=('Arial', 18), bg='#1a1a1a', fg='white', width=5).pack(side='left', padx=5)
            tk.Button(frame, text='-', font=('Arial', 16), command=lambda dt=diceType: resetDice(dt), bg='#540D9C', fg='white', width=3).pack(side='left', padx=2)
            
            countLabels[diceType] = tk.Label(frame, text='0', font=('Arial', 18), bg='#2a2a2a', fg='white', width=4)
            countLabels[diceType].pack(side='left', padx=8)
            
            tk.Button(frame, text='+', font=('Arial', 16), command=lambda dt=diceType: incrementDice(dt), bg='#540D9C', fg='white', width=3).pack(side='left', padx=2)
        
        def clearAll():
            for diceType in diceCount.keys():
                diceCount[diceType] = 0
                countLabels[diceType].config(text='0')
        clearButton = tk.Button(leftFrame, text='Clear All!', font=('Arial, 16'), bg="#610808", fg ='white', width=12, height=1, borderwidth=0, command=clearAll)
        clearButton.pack(pady=10)
        
        rollButton = tk.Button(leftFrame, text='Roll!', font=('Arial', 22, 'bold'), bg='#540D9C', fg='white', width=12, height=1, borderwidth=0, command=handleRoll)
        rollButton.pack(pady=10)
        

        rightFrame = tk.Frame(mainFrame, bg='#1a1a1a')
        rightFrame.pack(side='right', fill='both', expand=True, padx=10)
        
        tk.Label(rightFrame, text='Results:', font=('Arial', 18, 'bold'), bg='#1a1a1a', fg='white').pack(pady=10)
        
        resultDisplay = tk.Text(rightFrame, width=40, height=25, wrap='word', font=('Arial', 22), bg='#2a2a2a', fg='white', borderwidth=2, relief='solid')
        resultDisplay.pack(fill='both', expand=True)
        resultDisplay.configure(state='disabled')

        rootNew.mainloop()

    
    startButton = tk.Button(root, text='Let \'em roll!', font=('Arial', 20), bg='black', fg='white', command=begin_main_program)
    startButton.pack(side='bottom', pady=40)
    
    
    root.mainloop()
