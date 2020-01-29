import collections
from player import *
from textFile import *

class Ahorcado(object):
    ALLOWEDAMOUNT = ['1','2']
    IMAGES = ['''
    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']
    
    def __init__(self,):
        self.__getNumberOfPlayers__()
        self.__getPlayers__()
        
    
    def __getNumberOfPlayers__(self):
        self.__numberOfPlayers = str(input("Enter The Number of Players :"))
        if self.__numberOfPlayers in self.ALLOWEDAMOUNT:
            return
        self.__getNumberOfPlayers__()          

    
    def turnOfPlayers(self):
        jugador =  self.players.pop()
        self.players.appendleft(jugador)
        return jugador

    
    def playing(self):
        player = self.turnOfPlayers()
        self.__showStage__(player)
        lyrics = player.getLettersEnteredCorrect()
        player.repeatedLetter(lyrics)

    
    def __getPlayers__(self):
        self.players = collections.deque()
        for x in range(int(self.__numberOfPlayers)):
            print("Information for player {}".format(x))
            file = TextFile()
            self.players.appendleft(Player(str(file.wordRandom()),int(x)))
            file.closeFile()


    def __showStage__(self ,player):
        print("{} \n".format(self.IMAGES[player.lostLives]))
        self.__showWord__(player)


    def __showWord__(self ,player):
        for lyrics in player.word:
            if lyrics == '\n': continue
            if lyrics in player.lettersEnteredCorrect:
                print(" {} ".format(lyrics), end="")
            elif lyrics not in player.lettersEnteredCorrect and lyrics != ' ':
                print(" # ",end = "")
            else:
                print("   ",end = "")
        print("\n")
        print(player.word)