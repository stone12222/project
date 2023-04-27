
# There are 2 special box in tetris, next pattern and hold pattern box
# Each box can only display one pattern in them at once
class pattern_box:
    def __init__(self,xx,yy,aboard):
        self.xx=xx
        self.yy=yy
        self.board=aboard
        self.pattern=None

    # gets the pattern that need to display in the box and store some
    # of the initial attribute of the pattern for later use
    def getPatternForBox(self,terimino,patternNumber=0):
        self.patternNumber=patternNumber
        self.pattern=terimino.getPattern()
        self.patternColor = terimino.getColor()
        self.xpos, self.ypos = terimino.getSpawnXY()

    def showPatternOnBox(self):
        for y,e in enumerate(self.pattern[0]):
            for x,ee in enumerate(e):
                if ee==1:
                    self.board.boardArr[self.yy+y][self.xx+x]=self.patternColor

    def cleanPatternOnBox(self):
        if self.pattern:
            for y, e in enumerate(self.pattern[0]):
                for x, ee in enumerate(e):
                    if ee == 1:
                        self.board.boardArr[self.yy + y][self.xx + x]=(0,0,0)

    def getPattern(self):
        return self.pattern

    # returns the initial attribute of the stored pattern and it only used for hold
    # pattern box
    def getPatternInfo(self):
        return self.pattern, self.patternColor,self.xpos,self.ypos,self.patternNumber
    
    def removePatternInfo(self):
        self.pattern=None
        self.patternColor=None
        self.xpos,self.ypos=None, None
        self.patternNumber=None


