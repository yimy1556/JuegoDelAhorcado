from ahorcado import *

class Player(object):
    def __init__(self ,word ,playerNumber):
        self.playerNumber = playerNumber
        self.word = word
        self.lettersEnteredCorrect = set()
        self.endOfGame  = False
        self.winner  = False
        self.lostLives = 0
        self.__getNema__()

    def getOpponentText(self ,text):
        self.opponentText = text

    
    def getLettersEnteredCorrect(self ,lyrics):
        self.lettersEnteredCorrect.add(lyrics)

    def repeatedLetter(self, lyrics):
        if lyrics in self.lettersEnteredCorrect and len(self.lettersEnteredCorrect) != 1:
            print("!!! Letter Entered Already Entered You Lose Your Turn ¡¡¡")

    def printText(self):
        print("la palabra era {}".format(self.playerText))

    def __getNema__(self):
        self.playerName = str(input('Enter Player Name : '))



    def GameOver(self):
        self.endOfGame = True

    def printNema(self):
        print ("Your Name is {}".format(self.playerName))
    
