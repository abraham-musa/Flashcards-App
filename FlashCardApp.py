#This is a study guide program that obtains the terminology and definitions from a txt file and convert them into flash cards
#The program testes the user's knowledge by randomly generating terminologies from the txt file
#In the txt file, each line represents a flashcard. The word and definition should be seperated by a "|"


from Tkinter import *
import os
import random


#opens the txt file and splits each line into dictionary pairs
def openFile():
    filePath = '/Users/koonfaixie/Documents/Flashcards files/'
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
#invokes cardshuffler, resets counter, enables buttons
    def start(self):
        self.cardCounter = -1
        self.shuffler()
        self.startButton.config(state=DISABLED)
        self.nextButton.config(state=NORMAL)
        self.checkButton.config(state=NORMAL)
#shuffles cards
    def shuffler(self):
        d = openFile()
        temp=[]
        dList=[]
        for key, value in d.iteritems():
            temp= [key,value]
            dList.append(temp)
        random.shuffle(dList)
        self.shuffledCards = dList
#nextCard
    def addCounter(self):
        self.cardCounter = self.cardCounter + 1
        print self.cardCounter
        return self.shuffledCards[self.cardCounter]
#previousCard
    def subtractCounter(self):
        self.cardCounter = self.cardCounter - 1
        print self.cardCounter
        return self.shuffledCards[self.cardCounter]

    #calls for the previous card and displays it on the GUI screen
    def previousCard(self):
        if self.cardCounter == 0:
            self.previousButton.config(state=DISABLED)            
        self.currentCard = self.subtractCounter()
        self.cardDisplay.delete('1.0', END)
        self.cardDisplay.insert('1.0','\n'+self.currentCard[0]+'\n'*4+'Type your answer Below:\n')
        self.flipped = False
    #calls for self.randomCardGenerator to generate a random card and displays it on the GUI screen
    def nextCard(self): 
        #if the previousButton has been clicked, returns currentCard instead of a newly generated one
        try:
            self.currentCard = self.addCounter()
            self.cardDisplay.delete('1.0', END)
            self.cardDisplay.insert('1.0','\n'+self.currentCard[0]+'\n'*4+'Type your answer Below:\n')
            self.flipped = False
            self.previousButton.config(state=NORMAL)
        except:
            self.cardDisplay.delete('1.0', END)
            self.cardDisplay.insert('1.0','\nNo more flashcards left! Please press start again to shuffle the deck\n')
            self.previousButton.config(state=DISABLED)
            self.nextButton.config(state=DISABLED)
            self.checkButton.config(state=DISABLED)
            self.startButton.config(state=NORMAL)

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
        self.startButton = Button(self)
        self.startButton["text"] = "Start",
        self.startButton["command"] = self.start

        self.startButton.pack({"side": "left"})

        self.previousButton = Button(self, state=DISABLED)
        self.previousButton["text"] = "Previous",
        self.previousButton["command"] = self.previousCard

        self.previousButton.pack({"side": "top"})

        self.nextButton = Button(self, state=DISABLED)
        self.nextButton["text"] = "Next",
        self.nextButton["command"] = self.nextCard

        self.nextButton.pack({"side": "top"})

        self.checkButton = Button(self, state=DISABLED)
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
        self.flipped = False
        self.cardCounter = -1
        self.shuffledCards = []
        self.pack()
        self.createWidgets()
        



root = Tk()
root.title("Flash Card App")
app = Application(master=root)
app.mainloop()



