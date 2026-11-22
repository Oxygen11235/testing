#Program Name: Tkinter Math Flashcards

#Description: This is a GUI that provides math flashcards based on 4 levels.
#						Level 1: Only uses integers 1-3
#						Level 2: Only uses integers 1-6
#						Level 3: Only uses integers 1-9
#						Level 4: Only uses integers 1-12

#import tkinter tools
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import *

#import random module for flashcards
import random

#all functions are here
def pressstart():
    tab_control.select(levelselecttab)   #the first six functions switch to different tabs
    reaction.configure(image = "")
    messageplayer.configure(text = "")
    bar["value"] = 0
    
def getinstructions():
    tab_control.select(instructionstab) 
    
def backmenu():
    tab_control.select(welcometab)

def tolvlselecttab():
    tab_control.select(levelselecttab)
        
def toamountquestions():
    tab_control.select(amountquestionstab)
    
def anotherquestion():      #the next 3 count total, correct, and incorrect questions
    global totalquestions
    totalquestions += 1
    
def anothercorrect():
    global correct
    correct += 1

def anotherincorrect():
    global incorrect
    incorrect += 1
    
def switch():     #switches tabs
    tab_control.select(amountquestionstab)

def toflashcards():   #first step when flashcards start
    global correct        #calls variables so they can be reset
    global incorrect
    global totalquestions

    correct = 0    #resets these values for a new round
    incorrect = 0
    totalquestions = 0
    
    showcorrect.configure(text="Total Answers Correct: 0")
    showincorrect.configure(text="Total Answers Incorrect: 0")
    
    tab_control.select(flashcardstab)
    
    generatequestion()     #calls next function

def generatequestion():          #randomly generates the flashcard (step 2)
    
    global randomnumber1         #variables below
    global randomnumber2		 #calls variables to change value of
    global operator
    global answer
    
    randomnumber1 = random.randint(1, 3 * int(radiovalue.get()))  #calls spinbox
    randomnumber2 = random.randint(1, 3 * int(radiovalue.get()))
    operator = random.choice("+-x")

    if operator == "+":                             #different answers based on operator
        answer = str(randomnumber1 + randomnumber2)
    elif operator == "-":
        answer = str(randomnumber1 - randomnumber2)
    else:
        answer = str(randomnumber1 * randomnumber2)

    question.configure(text = str(randomnumber1) + "   " + str(operator) + "    " +
            str(randomnumber2) + "    =    ")

def validate():    #checks answer
    anotherquestion()

    showtotal.configure(text = "Total Questions Answered: " + str(totalquestions))
    
    if inputtedanswer.get() == str(answer):        #checks for correct input
        anothercorrect()
        showcorrect.configure(text = "Total Answers Correct: " + str(correct))
        messageplayer.configure(text = "Correct!")
        reaction.configure(image = img1)
    else:
        anotherincorrect()
        showincorrect.configure(text = "Total Answers Incorrect: " + str(incorrect))
        messageplayer.configure(text = "Incorrect! The correct answer is: " + str(answer))
        reaction.configure(image = img2)
    percentage.configure(text = "Percentage Mark: " + str(round((correct/totalquestions)*100)) + "%")
    bar["value"] = (totalquestions/spinbox2.get()) * 100
    inputtedanswer.delete(0, END)   #this deletes the input from index 0 to
                 #the last index (the entire input)

def run():
   
    validate()

    if totalquestions >= int(selectamount.get()):
        finishscreen()
    else:
        generatequestion()
    
def finishscreen():
    tab_control.select(lastscreen)

def restart():
    tab_control.select(welcometab)
#global variables
correct = 0
incorrect = 0
totalquestions = 0
randomnumber1 = 0
randomnumber2 = 0
operator = "0"
answer = "0"

#create GUI with title and screen size
window = Tk()
window.title("Math Flashcards GUI")
window.geometry("700x400")

#create notebook tabs
tab_control = ttk.Notebook(window) #creates tab
welcometab = Frame(tab_control)    #places it
tab_control.add(welcometab, text = "Welcome!")
levelselecttab = Frame(tab_control)
tab_control.add(levelselecttab, text = "Select Level")
amountquestionstab = Frame(tab_control)
tab_control.add(amountquestionstab, text = "# of Questions")
flashcardstab = Frame(tab_control)
tab_control.add(flashcardstab, text = "Flashcards!")
instructionstab = Frame(tab_control)
tab_control.add(instructionstab, text = "Instructions!")
lastscreen = Frame(tab_control)
tab_control.add(lastscreen, text = "Finish Screen")

#widgets for welcometab
welcome = Label(welcometab, text = "Welcome to Math Flashcards!",
                font = ("Arial Bold", 12),
                width = 70,
                height = 5)
welcome.grid(row = 0, column = 0)

space1 = Label(welcometab, text = "", height = 3)
space1.grid(row = 1, column = 0)

startbutton = Button(welcometab, text = "Press to Start",
                     font = ("Arial Bold", 11),
                     command = pressstart,
                     bg = "lightgreen",
                     width = 20,
                     height = 3)
startbutton.grid(row = 2, column = 0)

space2 = Label(welcometab, text = "", height = 6)
space2.grid(row = 3, column = 0)

instructionsbutton = Button(welcometab, text = "Instructions",
                            command = getinstructions,
                            bg = "lightblue",
                            width = 12,
                            height = 2)
instructionsbutton.grid(row = 4, column = 0)

#widgets for Select Level Tab
backbutton1 = Button(levelselecttab, text = "Back",
                     command = backmenu,
                     width = 12,
                     height = 2)
backbutton1.grid(row = 0, column = 0)

heading = Label(levelselecttab, text = "Select Level",
                font = ("Arial Bold", 15),
                width = 42,
                height = 3)
heading.grid(row = 1, column = 1)

radiovalue = IntVar()
lvl1 = Radiobutton(levelselecttab, text = "Level 1: Only uses integers 1 to 3",
                                   value = 1, variable = radiovalue)
lvl2 = Radiobutton(levelselecttab, text = "Level 2: Only uses integers 1 to 6",
                                   value = 2, variable = radiovalue)
lvl3 = Radiobutton(levelselecttab, text = "Level 3: Only uses integers 1 to 9",
                                   value = 3, variable = radiovalue)
lvl4 = Radiobutton(levelselecttab, text = "Level 4: Only uses integers 1 to 12",
                                   value = 4, variable = radiovalue)

lvl1.grid(row = 2, column = 1)
lvl2.grid(row = 3, column = 1)
lvl3.grid(row = 4, column = 1)
lvl4.grid(row = 5, column = 1)

printit = Button(levelselecttab, text = "Continue", command = switch)
printit.grid(row = 6, column = 1)

#widgets for # of Questions Tab
backbutton2 = Button(amountquestionstab, text = "Back",
                     command = tolvlselecttab,
                     width = 12,
                     height = 2)
backbutton2.grid(row = 0, column = 0)

title3 = Label(amountquestionstab, text = "Select Amount of Questions",
                                   font = ("Arial Bold", 12),
                                   width = 50,
                                   height = 5)
title3.grid(row = 1, column = 1)

spinbox2 = IntVar()
selectamount = Spinbox(amountquestionstab, from_ = 1, to = 10, textvariable = spinbox2)
selectamount.grid(row = 2, column = 1)

continue2 = Button(amountquestionstab, text = "Continue", command = toflashcards)
continue2.grid(row = 3, column = 1)

#widgets for Flashcards Tab
backbutton3 = Button(flashcardstab, text = "Back",
                     command = toamountquestions,
                     width = 12,
                     height = 2)
backbutton3.grid(row = 0, column = 0)

titlecard = Label(flashcardstab, text = "Math Flashcards!",
                  font = ("Arial Bold", 12),
                  width = 50,
                  height = 5)
titlecard.grid(row = 1, column = 3, sticky = E, columnspan = 3)

question = Label(flashcardstab, text = "", font = ("Arial", 16))
question.grid(row = 2, column = 3, sticky = E)

inputtedanswer = Entry(flashcardstab, width = 10)
inputtedanswer.grid(row = 2, column = 4, sticky = EW)

checkanswer = Button(flashcardstab, text = "Check Answer", command = run)
checkanswer.grid(row = 4, column = 4, sticky = EW)

messageplayer = Label(flashcardstab, text = "")
messageplayer.grid(row = 5, column = 4)

img1 = PhotoImage(file = "thumbs-up.png").subsample(12,12)
img2 = PhotoImage(file = "thumbsdown2.png").subsample(8,8)

reaction = Label(flashcardstab, pady = 10)
reaction.grid(row = 6, column = 4)

style = ttk.Style()
style.theme_use("default")
style.configure("black.Horizontal.TProgressbar", background = "black")

bar = Progressbar(flashcardstab, length = 400, style = "black.Horizontal.TProgressbar",)
bar.grid(row = 7, column = 3, columnspan = 4)

bar["value"] = 0

#widgets for instructionstab
backbutton4 = Button(instructionstab, text = "Back",
                     command = backmenu,
                     width = 12,
                     height = 2)
backbutton4.grid(row = 0, column = 0)

instruct = Label(instructionstab, text = "Instructions!",
                 font = ("Arial Bold", 12),
                 width = 50)
instruct.grid(row = 1, column = 1)

#widgets for finishing screen
congrats = Label(lastscreen, text = "Congratulations!",
                 font = ("Arial Bold", 16),
                 width = 53,
                 pady = 10)
congrats.grid(row = 0, column = 0)

showtotal = Label(lastscreen, text = "Total Questions Answered: 0",
                              pady = 10)
showtotal.grid(row = 1, column = 0)

showcorrect = Label(lastscreen, text = "Total Answers Correct: 0",
                                pady = 10)
showcorrect.grid(row = 2, column = 0)

showincorrect = Label(lastscreen, text = "Total Answers Incorrect: 0",
                                  pady = 10)
showincorrect.grid(row = 3, column = 0)

percentage = Label(lastscreen, text = "Percentage Mark: ", pady = 10)
percentage.grid(row = 4 ,column = 0)

emptylabelagain = Label(lastscreen, text = "",
                                    pady = 10)
emptylabelagain.grid(row = 5, column = 0)

restartbtn = Button(lastscreen, text = "Play Again?",command = restart,
                                bg = "blue",
                                fg = "white")
restartbtn.grid(row = 6, column = 0)
#hide tabs
#style = ttk.Style()
#style.layout("TNotebook.Tab", [])

tab_control.pack(expand = 1, fill = "both")

#keeps the program running
window.mainloop()
