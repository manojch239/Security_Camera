# Password generator with GUI 
from tkinter import *
import pyperclip
import random

root = Tk() #intialize tkinter
root.geometry("400x400") #dimensions of the GUI 

pass_str = StringVar() #string variable to store password

pass_len = IntVar() # int variable to store password length

#password generator function

def pass_generate():
    keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
                'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
                'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
                'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
                '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
                '*', '(', ')']

    password = ""
    for x in range(pass_len.get()):
        password = password + random.choice(keys)
    pass_str.set(password)
    
# function to copy password to clipboard

def copy2clipboard():
    
    random_password = pass_str.get()
    pyperclip.copy(random_password)
    
#creating a txt label widget
Label(root,text = "Password Generator Application",font="calibri 20 bold").pack()
Label(root, text="Enter password length").pack(pady=3)

#Entry wideget to take password length from user
Entry(root, textvariable=pass_len).pack(pady=3)

#button to call generator func
Button(root,text = "Generate Password",command=pass_generate).pack(pady=7)

#Entry widget to show generated password
Entry(root,textvariable=pass_str).pack(pady=3)

#button to call copy2clipboard function
Button(root,text = "Copy to clipboard", command=copy2clipboard).pack()

# run mainloop
root.mainloop()