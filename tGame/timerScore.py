import time
import number

class timerScore:
    def __init__(self,x,timerY,scoreY,boards):
        self.start_time=time.time()
        self.x=x
        self.timerY=timerY
        self.scoreY=scoreY
        self.score=0
        self.boards=boards
        self.number=number.number()

    def resetStartTime(self):
        self.start_time=time.time()

    def getMinSec(self,seconds):
        return f'{seconds//60:02d}',f'{seconds%60:02d}'

    def increaseScore(self):
        self.score+=100

    def getScore(self):
        return self.score
    
    def setScore(self,score):
        self.score=score
    
    def resetTime(self):
        self.start_time=time.time()

    # returns the current time and at the same time display the time of the board
    def getGameTime(self):
        min,sec=self.getMinSec(round(time.time()-self.start_time))
        i=0
        for e in str(min):
            for j,ee in enumerate(self.number.getANumber(e)):
                for x,eee in enumerate(ee):
                    self.boards.boardArr[j][i+x]=(0,0,0)
                    if eee ==1:
                        self.boards.boardArr[j][i+x]=(0,225,0)
            i+=4
        i+=1
        for e in str(sec):
            for j,ee in enumerate(self.number.getANumber(e)):
                for x,eee in enumerate(ee):
                    self.boards.boardArr[j][i+x]=(0,0,0)
                    if eee ==1:
                        self.boards.boardArr[j][i+x]=(0,225,0)
            i+=4
        
        return min,sec

    def displayGameScore(self):
        i=0
        for e in str(self.score):
            for j,ee in enumerate(self.number.getANumber(e)):
                for x,eee in enumerate(ee):
                    self.boards.boardArr[j+5][i+x]=(0,0,0)
                    if eee ==1:
                        self.boards.boardArr[j+5][i+x]=(0,225,0)
            i+=4
            
    