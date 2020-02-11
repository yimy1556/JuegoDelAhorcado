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
        self.lyrics = ' '
        
    
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
        gameOver = False
        while gameOver != True:
            player = self.turnOfPlayers()
            self.__showStage__(player)
            self.lyrics = player.getLettersEnteredCorrect()
            player.repeatedLetter(self.lyrics)
            gameOver = self.__gameOver__(player)


    def __fullWord__(self, player):
        full = True
        for lyrics in player.word:
            if full == False: return
            full = lyrics in player.lettersEnteredCorrect 
        player.endOfGame = full

    def __gameOver__(self ,player):
        self.__fullWord__(player)
        if player.lostLives == 8:
            player.endOfGame = True
        return player.endOfGame

    def __winner__(self):
        player = self.players.popleft()
        print("Congratulations Player {} In Name {} For Winning".format(player.playerNumber).format(player.playerName))



    def __getPlayers__(self):
        self.players = collections.deque()
        for x in range(int(self.__numberOfPlayers)):
            print("Information for player {}".format(x))
            file = TextFile()
            self.players.appendleft(Player(str(file.wordRandom()),int(x)))
            file.closeFile()


    def __showStage__(self ,player):
        print("\n ### Player {} ###".format(player.playerName))
        print("{} \n".format(self.IMAGES[player.lostLives]))
        self.__showWord__(player)


    def __showWord__(self ,player):
        for lyrics in player.word:
            if lyrics in player.lettersEnteredCorrect.values():
                print(" {} ".format(lyrics), end="")
            elif lyrics not in player.lettersEnteredCorrect..values() and lyrics != ' ':
                print(" # ",end = "")
            else:
                print("   ",end = "")
        print("\n")
        print(player.word)