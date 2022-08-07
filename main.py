
#       ████████████████████████████████████████████████████████████████████████████████████████████████████
#       █─▄▄▄─█▄─██─▄█▄─▄▄▀█▄─▄███▄─█─▄█░█─▄▄▄▄███─▄▄▄─█─▄▄─█▄─▄▄▀█▄─▄▄─███▄─▄▄─█▄─▄▄▀█▄─▄█─▄─▄─█─▄▄─█▄─▄▄▀█
#       █─███▀██─██─███─▄─▄██─██▀██▄─▄██▄█▄▄▄▄─███─███▀█─██─██─██─██─▄█▀████─▄█▀██─██─██─████─███─██─██─▄─▄█
#       ▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▀▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▀▀▄▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀
#Made by Curly
#Made on 2022-6-3
#Path: main.py
#Modules:
#tkinter
#subprocess
#os
#sys
#time

#
#
#
#

#    ░█████╗░░█████╗░██████╗░███████╗  ██████╗░███████╗██╗░░░░░░█████╗░░██╗░░░░░░░██╗
#    ██╔══██╗██╔══██╗██╔══██╗██╔════╝  ██╔══██╗██╔════╝██║░░░░░██╔══██╗░██║░░██╗░░██║
#    ██║░░╚═╝██║░░██║██║░░██║█████╗░░  ██████╦╝█████╗░░██║░░░░░██║░░██║░╚██╗████╗██╔╝
#    ██║░░██╗██║░░██║██║░░██║██╔══╝░░  ██╔══██╗██╔══╝░░██║░░░░░██║░░██║░░████╔═████║░
#    ╚█████╔╝╚█████╔╝██████╔╝███████╗  ██████╦╝███████╗███████╗╚█████╔╝░░╚██╔╝░╚██╔╝░
#    ░╚════╝░░╚════╝░╚═════╝░╚══════╝  ╚═════╝░╚══════╝╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░
#
#
#
###############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################




from asyncio import SubprocessProtocol
from tkinter import *
import os
import time
import random
import math
import sys
import subprocess

from tkinter.filedialog import asksaveasfilename, askopenfilename
#Make sure the user is running python 3.6 or higher
if sys.version_info[0] < 3:
    print("This program requires Python 3.6 or higher.")
    sys.exit(1)
os.command("pip install tkinter")

#Variabls
Code_Editor = Tk()
Code_Editor.title("Curly's Code_Editor")
#Make window size
Code_Editor.geometry("800x600")


#Code_Editor.geometry("800x600")
#Code_Editor.resizable(0,0)
#Make the textbox for the code
textbox = Text(Code_Editor, width=80, height=20, bg="grey", fg="white", font=("Helvetica", 12))
textbox.pack()


#make the buttons functtions
def set_file_path(path):
    global file_path
    file_path = path

def alert(text):
    #If text is not a string
    if not isinstance(text, str):
        #Make it a string
        text = str(text)


    #Make a new window
    alert = Tk()

    alert.title("Alert")
    #Make the textbox
    textbox = Text(alert, width=80, height=20, bg="black", fg="white", font=("Helvetica", 12))
    textbox.pack()
    #Set the text in the textbox
    textbox.insert(1.0, text)
    #Make the buttons
    button = Button(alert, text="OK", command=alert.destroy)
    button.pack()
file_path =""
#Make the setup what makes the folder "EXPORTS"

def setup():
    #Make the folder
    os.system("mkdir EXPORTS")


def clear():
    textbox.delete(1.0, END)
#Run the code in a new terminal
def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()





  

def save():
    #Open the file ex
    path = asksaveasfilename(filetypes=[('Python Files', '*')])
    with open(path, 'w') as file:
        code = textbox.get(1.0, END)
        file.write(code)
        set_file_path(path)
    
 

def load():
    path = askopenfilename(filetypes=[('Python Files', '*')])
    with open(path, 'r') as file:
        code = file.read()
        textbox.delete(1.0, END)
        textbox.insert(1.0, code)





    
    
def exit():
    #Exit the program
    Code_Editor.destroy()
def help():
    #Make a new window what shows the help
    txt = "Curly's Code_Editor\n\n"
    txt += "This is a simple Code_Editor for programming .\n\n"
    txt += "The Code_Editor has the following features:\n\n"
    txt += "1. Save\n"
    txt += "2. Load\n"
    txt += "3. Run\n"
    txt += "4. Clear\n"
    txt += "5. Help\n"
    txt += "6. Exit\n"
    txt += "7. Setup\n"
    txt += "And the most important one is:\n"
    txt += "8. Editing the Code_Editor \n"

    txt += "\n\n"

    #Make a new window
    help = Tk()
    help.title("Help")
    #Make the textbox
    textbox = Text(help, width=80, height=20, bg="grey", fg="white", font=("Helvetica", 12))
    textbox.pack()
    #Set the text in the textbox
    textbox.insert(1.0, txt)
    #Make the buttons




#Make the buttons for saving and opening files
menu = Menu(Code_Editor)
Code_Editor.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Load", command=load)
filemenu.add_command(label="Exit", command=exit)
#Make the buttons for the help
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help", command=help)
#Make the buttons for the run
runmenu = Menu(menu)
menu.add_cascade(label="Run", menu=runmenu)
runmenu.add_command(label="Run (python)", command=run)
runmenu.add_command(label="Clear", command=clear)
#Make the buttons for the setup
setupmenu = Menu(menu)
menu.add_cascade(label="Setup", menu=setupmenu)
setupmenu.add_command(label="Setup", command=setup)
#Binds
Code_Editor.bind("<Control-s>", save)
Code_Editor.bind("<Control-o>", load)
Code_Editor.bind("<Control-r>", run)
Code_Editor.bind("<Control-c>", clear)
Code_Editor.bind("<Control-h>", help)
Code_Editor.bind("<Control-e>", exit)
Code_Editor.bind("<Control-u>", setup)
#Background
Code_Editor.configure(background='black')

if __name__ == '__main__':
    #Make the folder
    setup()
    #Start the program
    Code_Editor.mainloop()
