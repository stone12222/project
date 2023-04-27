# this class contains the information for the number pattern
# in a 4 by 3 pixel state so that numbers can be displayed on
# the board easily

class number:
    def __init__(self):
        pass
    
    def getANumber(self,number):
        if number=='0':
            return self.getZero()
        elif number=='1':
            return self.getOne()
        elif number=='2':
            return self.getTwo()
        elif number=='3':
            return self.getThree()
        elif number=='4':
            return self.getFour()
        elif number=='5':
            return self.getFive()
        elif number=='6':
            return self.getSix()
        elif number=='7':
            return self.getSeven()
        elif number=='8':
            return self.getEight()
        else:
            return self.getNine()
        
    
    def getZero(self):
        return [[1,1,1],
                [1,0,1],
                [1,0,1],
                [1,1,1]]
    
    def getOne(self):
        return [[0,1,0],
                [0,1,0],
                [0,1,0],
                [0,1,0]]
    
    def getTwo(self):
        return [[1,1,1],
                [0,0,1],
                [0,1,0],
                [1,1,1]]
    
    def getThree(self):
        return [[1,1,1],
                [0,1,0],
                [0,0,1],
                [1,1,1]]
    
    def getFour(self):
        return [[1,0,1],
                [1,0,1],
                [1,1,1],
                [0,0,1]]
    
    def getFive(self):
        return [[1,1,1],
                [1,1,0],
                [0,0,1],
                [1,1,0]]
     
    def getSix(self):
        return [[1,1,1],
                [1,0,0],
                [1,1,1],
                [1,1,1]]
    
    def getSeven(self):
        return [[1,1,1],
                [0,0,1],
                [0,1,0],
                [0,1,0]]
    
    def getEight(self):
        return [[1,1,1],
                [1,1,1],
                [1,1,1],
                [1,1,1]]
    
    def getNine(self):
        return [[1,1,1],
                [1,1,1],
                [0,0,1],
                [1,1,1]]
    