class Body(object):
    
    def __init__(self):
        self.leftLag = False
        self.rightLag = False
        self.leftArm = False 
        self.rightArm = False
        self.head = False
        self.chest = False 

    def getLeftlag(self):
        self.leftLag = True
    
    def getRightLag(self): 
        self.rightLag= True
        
    def getLeftArm(self): 
       self.getLeftArm = True 
        
    def getRightArm(self): 
        self.rightArm = True
    
    def getHead(self):
        self.head = True
    
    def getChest(self): 
        self.chest = True