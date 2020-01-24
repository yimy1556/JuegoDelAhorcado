from body import *

class Player(object):

    def __init__(self ,text):
        self.playerText = text  
        self.endOfGame  = False
        self.__getNema__()
     
    def getOpponentText(self ,text):
        self.opponentText = text

    def __getNema__(self):
        self.__playerName = str(input('Enter Player Name : '))


    def GameOver(self):
        self.endOfGame = True

    def printNema(self):
        print ("Your Name is {}".format(self.__playerName))
