#This is a study guide program that obtains the terminology and definitions from a txt file and convert them into flash cards
#The program testes the user's knowledge by randomly generating terminologies from the txt file
#In the txt file, each line represents a flashcard. The word and definition should be seperated by a "|"


from Tkinter import *
import os
import random


#opens the txt file and splits each line into dictionary pairs
def openFile():
    filePath = '/Users/koonfaixie/Documents/StudyGuide files/'
    os.chdir(filePath)
    flashCards = open('Flashcards.txt')
    d = {}
    with flashCards as f:
        for line in f:
            (key, val) = line.split('|')
            d[key] = val.strip('\n')
    return d

#Application GUI
class Application(Frame):
    #generates a random card
    def randomCardGenerator(self):
        d = openFile()
        randomKey = random.choice(d.keys())
        randomValue =d[randomKey]
        return randomKey, randomValue
    #calls for the previous card and displays it on the GUI screen
    def previous(self):
        self.cardDisplay.delete('1.0', END)
        self.cardDisplay.insert('1.0','\n'+self.previousCard[0]+'\n'*4+'Type your answer Below:\n')
        self.previousButton.config(state=DISABLED)
        self.flipped = False
    #calls for self.randomCardGenerator to generate a random card and displays it on the GUI screen
    def nextCard(self): 
        #if the previousButton has been clicked, returns currentCard instead of a newly generated one
        if self.previousButton["state"]==DISABLED:     
            self.cardDisplay.delete('1.0', END)
            self.cardDisplay.insert('1.0','\n'+self.currentCard[0]+'\n'*4+'Type your answer Below:\n')
            self.previousButton.config(state=NORMAL)
            self.flipped = False
        #calls for self.randomCardGenerator only if the previousButton has not been clicked prior
        else:
            self.previousCard = self.currentCard
            self.currentCard = self.randomCardGenerator()
            self.cardDisplay.delete('1.0', END)
            self.cardDisplay.insert('1.0','\n'+self.currentCard[0]+'\n'*4+'Type your answer Below:\n')
            self.flipped = False
    #flips the flashcard over to check the answer
    def flip(self):
        if self.flipped == False:
            self.cardDisplay.delete('1.0', END)
            self.cardDisplay.insert('1.0','\n'+self.currentCard[1]+'\n\n'+'Was it Correct?\n')
            self.flipped = True
        else:            
            self.cardDisplay.delete('1.0', END)
            self.cardDisplay.insert('1.0','\n'+self.currentCard[0]+'\n'*4+'Type your answer Below:\n')
            self.flipped = False
    #GUI widgets/buttons creation
    def createWidgets(self):
        self.previousButton = Button(self, state=DISABLED)
        self.previousButton["text"] = "Previous",
        self.previousButton["command"] = self.previous

        self.previousButton.pack({"side": "top"})

        self.nextButton = Button(self)
        self.nextButton["text"] = "Next",
        self.nextButton["command"] = self.nextCard

        self.nextButton.pack({"side": "top"})

        self.checkButton = Button(self)
        self.checkButton["text"] = "Check"
        self.checkButton["command"] = self.flip

        self.checkButton.pack({"side": "top"})

        self.cardDisplay = Text(self, width= 80, height= 30)
        self.cardDisplay.pack(side=LEFT, fill=Y)
        self.scrollBar = Scrollbar(self)
        self.scrollBar.pack(side=RIGHT, fill=Y)
        self.scrollBar.config(command=self.cardDisplay.yview)
        self.cardDisplay.config(yscrollcommand=self.scrollBar.set)
    #creates a GUI frame and packages GUI/widgets. Sets a default status for flashcards
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.currentCard = ("Please press Next to proceed","Please press Next to proceed")
        self.previousCard = ("","")
        self.flipped = False
        self.pack()
        self.createWidgets()
        



root = Tk()
root.title("Flash Card App")
app = Application(master=root)
app.mainloop()



