import random

class TextFile(object):
    def __init__(self):
        self.__setFileNema__()
        self.__file = open(self.__fileNema ,'r')


    #def __setOpeningMode__(self):
    #    self.__openingMode = str(input(self.OPENINGGUIDE)).lower()
    
    
    def __setFileNema__(self):
        self.__fileNema = str(input("Enter File Nema : ").lower())


    
    #def __toWriteFile__(self):
    #   self.__file.write(str(input("Enter Word :")).lower())
    #    while(str(input("continue yes or No")) != self.STOP):
    #        self.__file.write(str(input("Enter Word :")).lower()) 

    def closeFile(self):
        self.__file.close() 
    
    
    def wordRandom(self):
        words = self.__file.readlines() 
        return random.choice(words)            

