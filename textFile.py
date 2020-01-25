import random

class TextFile(object):
    OPENINGGUIDE = "Enter The Opening Mode R(Mode Of Reading) or W (Mode Of writing)"
    STOP = "no"
    CREATE = "W"
    rowAmount = 0

    def __init__(self ,fileNema):
        __setFileNema__()
        __setOpeningMode__()
        self.__file = open(self.__fileNema ,self.__openingMode)
        if self.__openingMode == self.CREATE.lower():
            __toWriteFile__():
        


    def __setOpeningMode__(self):
        self.__openingMode = str(input(OPENINGGUIDE)).lower()
    
    def __setFileNema__(self):
        self.__fileNema = str(input("Enter File Nema : ").lower())

    def __toWriteFile__(self):
        while(str(input("continue yes or No")).lower != self.STOP)
            self.__file.write(str(int("Enter Word :")).lower()) 

    def closeFile(self):
        self.__file.close() 
    
    def wordRandom(self):
        pass

    def __fileRowAmount__(self):
        for word in self.file:
           self.rowAmount += 1
        return self.rowAmount