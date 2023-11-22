#Author: Ramtin Soleymani
#Description: This simple game is Tic_Tac_Toe


from tkinter import *
import random


root = Tk()
root.title('Tic Tac Toe')

root.geometry ("900x550")

def clearFrame():
    for widget in root.winfo_children():
        widget.destroy()

def backToStart():
    backButton = Button(root, text = "Back", padx = 50, command = startMenu)
    backButton.grid()

class mainGame():
   
    def nextTurn(self, row, column):
        
        if self.buttonLayout[row][column]['text'] == "" and self.checkWinner() is False:

            if self.player == "X":
                
                self.buttonLayout[row][column]['text'] = "X"
                self.computerMove()
                
                if self.checkWinner() is True:
                    self.label.config(text="X wins!")    

                elif self.checkWinner() == "Tie":
                    self.label.config(text="It's a Tie!")

            else:   
               
                self.buttonLayout[row][column]['text'] = "O"
                self.computerMove()

                if self.checkWinner() is True:
                    self.label.config(text="O wins!")

                elif self.checkWinner() == "Tie":
                    self.label.config(text="It's a Tie!")
   
    def checkWinner(self):
 
        for row in range(3):
            if self.buttonLayout[row][0]['text'] == self.buttonLayout[row][1]['text'] == self.buttonLayout[row][2]['text'] != "":
                self.buttonLayout[row][0].config(bg="green")
                self.buttonLayout[row][1].config(bg="green")
                self.buttonLayout[row][2].config(bg="green")
                return True
        
        for column in range(3):
            if self.buttonLayout[0][column]['text'] == self.buttonLayout[1][column]['text'] == self.buttonLayout[2][column]['text'] != "":
                self.buttonLayout[0][column].config(bg="green")
                self.buttonLayout[1][column].config(bg="green")
                self.buttonLayout[2][column].config(bg="green")
                return True

        if self.buttonLayout[0][0]['text'] == self.buttonLayout[1][1]['text'] == self.buttonLayout[2][2]['text'] != "":
            self.buttonLayout[0][0].config(bg="green")
            self.buttonLayout[1][1].config(bg="green")
            self.buttonLayout[2][2].config(bg="green")
            return True

        elif self.buttonLayout[0][2]['text'] == self.buttonLayout[1][1]['text'] == self.buttonLayout[2][0]['text'] != "":
            self.buttonLayout[0][2].config(bg="green")
            self.buttonLayout[1][1].config(bg="green")
            self.buttonLayout[2][0].config(bg="green")
            return True

        elif self.checkTie() is True:

            for row in range(3):
                for column in range(3):
                    self.buttonLayout[row][column].config(bg="yellow")
            return "Tie"

        else:

            return False

    def checkTie(self):
        spaces = 9

        for row in range(3):
            for column in range(3):
                if self.buttonLayout[row][column]['text'] != "":
                    spaces -= 1

        if spaces == 0:
            return True
        else:
            return False

    def computerMove(self):
        test = True        
        while(test is True):
            row = random.randint(0,2)
            column = random.randint(0,2)
            if self.checkWinner() is not False:
                test = False
            elif self.buttonLayout[row][column]['text'] == "":
                self.buttonLayout[row][column]['text'] = self.computer
                test = False
            


    def __main__ (self, player):
        clearFrame()

        self.player = player
        self.buttonLayout = [["","",""], ["","",""], ["","",""]]
        
        compFirstRow = None
        compFirstCol = None
        

        self.label = Label(root, text = "")
        self.label.grid()

        if self.player == ("O"):
            self.computer = "X"
            compFirstRow = random.randint(0,2)
            compFirstCol = random.randint(0,2)
        
        elif self.player == ("X"):
            self.computer = "O"
                
        if compFirstRow is None and compFirstCol is None:
            for row in range(3):
                for column in range(3):
                    self.buttonLayout[row][column] = Button(root, text = "", padx = 150, pady = 60, command = lambda row = row, column = column :self.nextTurn(row ,column))
                    self.buttonLayout[row][column].grid(row = row, column = column)
        else:
            for row in range(3):
                for column in range(3):
                    if row == compFirstRow and column == compFirstCol:
                        self.buttonLayout[row][column] = Button(root, text = "X", padx = 150, pady = 60, command = lambda row = row, column = column :self.nextTurn(row ,column))
                        self.buttonLayout[row][column].grid(row= row, column = column)

                    else:
                        self.buttonLayout[row][column] = Button(root, text = "", padx = 150, pady = 60, command = lambda row = row, column = column :self.nextTurn(row ,column))
                        self.buttonLayout[row][column].grid(row = row, column = column)

        backToStart()

        

class pickSides(mainGame):

    def playerX(self):
        super().__main__("X")

    def playerO(self):
        super().__main__("O")


    def __init__(self):

        clearFrame()
        stX = Button(root, text = "X", padx = 450, pady = 80, command = self.playerX)
        stO = Button(root, text = "O", padx = 450, pady = 80, command = self.playerO)
        stX.grid()
        stO.grid()


def gameHelp():
    clearFrame()
    gameInstruction = Label(root, text = "The object of Tic Tac Toe is to get three in a row.\n You play on a three by three game board. The first player is known as X and the second is O.\n Players alternate placing Xs and Os on the game board until either oppent has three in a row or all nine squares are filled.\n X always goes first, and in the event that no one has three in a row, the stalemate is called. \n Good Luck :) \n \n \nThis program was created by Ramtin Soleymani!\n\nRefrences: https://www.youtube.com/watch?v=_mjZjpOmN0k")
    gameInstruction.grid()
    backToStart()

def sideCheck():
    checkSides = pickSides()
    checkSides.__init__()
    
    gameDescription = Label(root, text = "Please choose which to start with first. \n \n")
    gameDescription.grid()
    backToStart()
    

def startMenu():
    clearFrame()
    
    startButton = Button(root, text = "Start", padx = 450, pady = 80, command = sideCheck)
    helpButton = Button(root, text = "Help", padx = 450, pady = 80, command = gameHelp)
    quitButton = Button(root, text = "Quit", padx = 450, pady = 80, command = root.quit)

    startButton.grid()
    helpButton.grid()
    quitButton.grid()


startMenu()

root.mainloop()


