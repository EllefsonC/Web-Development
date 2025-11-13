from ctypes import windll
#I had to look this up, but this is a fix to the common issue of Tkinter not performing well on high DPS monitors and coming out blurry.

try:
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

import random
import tkinter as tk
import tkinter.font as tkFont

# ***tkinter GUI***
#Creating start window
root = tk.Tk()
root.geometry('800x600')
root.configure(bg='#1a1a1a')




#root init
root.title('DnD Dice Engine')
label = tk.Label(root, text='Welcome to the DnD Dice Engine!', font=('Arial', 28), bg="#540D9C", fg='white')
label.pack(pady=30)



#text box... duh
textbox = tk.Text(root,width= 40, height = 3, wrap="word", font=('Arial', 16), bg='#1a1a1a', fg='white')
textbox.insert("1.0", 'This script is intended for DnD players who forget their dice before their dungeon crawl.\n')
textbox.insert("end", 'Enjoy!', 'right')
textbox.tag_configure('right', justify='right')
#disables text input
textbox.configure(state= 'disabled')
textbox.pack()



def begin_main_program():
    root.destroy()
    
    #New Window, created after startButton Clicked on root window
    rootNew = tk.Tk()
    rootNew.geometry('800x600')
    rootNew.title('Select Your Dice')
    rootNew.configure(bg='#1a1a1a')

    rollButton = tk.Button(rootNew, text='Roll!', font=('Arial', 20),bg='black', fg='white', width=6, height=1, borderwidth=0)
    rollButton.pack(side='right', anchor='se', pady=100)



    textbox1= tk.Text(rootNew, width=30, height=2, wrap='word', font=('Arial', 16), bg='#1a1a1a', fg='white', borderwidth=0)
    textbox1.insert("1.0", 'Please choose your dice, you may chose multiple!')
    textbox1.configure(state='disabled')
    textbox1.pack(ipadx=100)



    listbox = tk.Listbox(rootNew, height=10, width=10,
                    bg= 'grey', activestyle = 'dotbox', font=('Arial', 18), borderwidth=0)
    listbox.insert(1, 'D4')
    listbox.insert(2, 'D6')
    listbox.insert(3, 'D12')
    listbox.insert(4, 'D20')
    listbox.insert(5, 'D40')
    listbox.pack(padx=2, pady=100, side='left')

    rootNew.mainloop()  
        



#button that will begin core of script prompts
startButton = tk.Button(root, text='Let \'em roll!', font=('Arial', 20),bg='black', fg='white', command=begin_main_program)
startButton.pack(side='bottom', pady=40)


   
      
root.mainloop()
