from ahorcado import *

class Player(object):
    def __init__(self ,word ,playerNumber):
        self.playerNumber = playerNumber
        self.word = word.lower()
        self.lettersEnteredCorrect = set()
        self.endOfGame  = False
        self.lostLives = 0
        self.__getNema__()

    def getOpponentText(self ,text):
        self.opponentText = text


    def getLettersEnteredCorrect(self):
        lyrics = str(input("Enter The Letter That Belongs To The Word")).lower()
        if lyrics in self.word:
            self.lettersEnteredCorrect.add(lyrics)
        return lyrics

    def repeatedLetter(self, lyrics):
        if lyrics in self.lettersEnteredCorrect:
            print("Letter Entered Already Entered You Lose Your Turn")

    def printText(self):
        print("la palabra era {}".format(self.playerText))

    def __getNema__(self):
        self.playerName = str(input('Enter Player Name : '))

    def GameOver(self):
        self.endOfGame = True

    def printNema(self):
        print ("Your Name is {}".format(self.playerName))
    
