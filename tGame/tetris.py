import tetrimino
import random
import hold_next_box
import timerScore
import collision

# the tetris class operates on top of all the other classes
# tetris class contains all the functions for the game to operate on the board
class tetris(collision.collision):
    def __init__(self,strips,boards,music):
        self.boards = boards
        self.timerScore=timerScore.timerScore(450,485,415,self.boards)
        self.holdBox = hold_next_box.pattern_box(12,20,self.boards)
        self.nextBox = hold_next_box.pattern_box(12,14,self.boards)
        self.music=music

        I=tetrimino.I()
        O = tetrimino.O()
        T = tetrimino.T()
        L = tetrimino.L()
        J = tetrimino.J()
        S = tetrimino.S()
        Z = tetrimino.Z()
        self.arr=[I,O,T,L,J,S,Z]

        self.nextPattern=self.getRandomPattern()
        self.currentPattern=0
        self.timerScore.displayGameScore()
        self.strips=strips

        super().__init__(self.boards)

    def displayBoard(self):
        self.update_strip()

    def getRandomPattern(self):
        return random.randint(0,6)

    # spawns the pattern on the very top using some of the
    # initial attribute provide from the tetrimino class
    # it will also check for death so the game will end if death is true
    def spawnPattern(self):
        self.patternExchanged=False
        self.currentPattern = self.nextPattern
        self.nextPattern=self.getRandomPattern()
        self.pattern=self.arr[self.currentPattern].getPattern()
        self.patternPhase=0
        self.patternColor=self.arr[self.currentPattern].getColor()
        self.xpos,self.ypos=self.arr[self.currentPattern].getSpawnXY()

        self.nextBox.cleanPatternOnBox()
        self.nextBox.getPatternForBox(self.arr[self.nextPattern])
        self.nextBox.showPatternOnBox()

        if self.checkDeath():
            return True

        self.checkRowFull()
        self.showPattern(self.xpos,self.ypos, self.pattern[self.patternPhase])

    # this function will try to update the board object to display the pattern on the
    # sim on the appropriate position
    def showPattern(self,xpos,ypos,pattern):
        for y,e in enumerate(pattern):
            for x,ee in enumerate(e):
                if 10<=ypos+y<=30 and 1<=xpos+x<=10:
                    if ee==1:
                        self.boards.boardArr[ypos+y][xpos+x]=self.patternColor
        self.boards.update_strip()

    # this function is similar to the showPattern function but instead of displaying
    # the pattern with it's color this function will try to display the pattern with
    # no color i.e. removing the pattern from the board
    def cleanSpot(self,xpos,ypos,pattern):
        for y,e in enumerate(pattern):
            for x,ee in enumerate(e):
                if 10<=ypos+y<=30 and 1<=xpos+x<=10:
                    if ee == 1:
                        self.boards.boardArr[ypos + y][xpos + x] = (0, 0, 0)

    # this function moves the pattern down a block at a time and check
    # for any collision if so it will spawn a new pattern
    def patternMoveDown(self):
        self.cleanSpot(self.xpos, self.ypos, self.pattern[self.patternPhase])
        if self.collisionBottom(self.ypos+1,self.xpos,self.pattern[self.patternPhase]):
            self.showPattern(self.xpos, self.ypos, self.pattern[self.patternPhase])
            if self.spawnPattern():
                return True
        else:
            self.ypos += 1
        self.showPattern(self.xpos,self.ypos,self.pattern[self.patternPhase])
        self.timerScore.displayGameScore()

    # moves the pattern left and check for any collision if so the pattern will not move
    def moveLeft(self):
        self.cleanSpot(self.xpos, self.ypos, self.pattern[self.patternPhase])
        if not self.collisionLeft(self.ypos, self.xpos - 1, self.pattern[self.patternPhase]):
            self.xpos -= 1
        self.showPattern(self.xpos, self.ypos, self.pattern[self.patternPhase])

    # moves the pattern right and check for any collision if so the pattern will not move
    def moveRight(self):
        self.cleanSpot(self.xpos, self.ypos, self.pattern[self.patternPhase])
        if not self.collisionRight(self.ypos, self.xpos+1, self.pattern[self.patternPhase]):
            self.xpos += 1
        self.showPattern(self.xpos, self.ypos, self.pattern[self.patternPhase])

    # switch the pattern with the player current pattern to the pattern stored in the
    # hold box and the player can only switch the pattern only once per spawn
    def switchPattern(self):
        if not self.patternExchanged:
            self.patternExchanged = True
            self.cleanSpot(self.xpos,self.ypos,self.pattern[self.patternPhase])
            if self.holdBox.getPattern():
                self.holdBox.cleanPatternOnBox()
                tempVar1,tempVar2,tempVar3,tempVar4,tempVar5=self.holdBox.getPatternInfo()
                self.holdBox.getPatternForBox(self.arr[self.currentPattern], self.currentPattern)
                self.pattern,self.patternPhase=tempVar1,0
                self.patternColor,self.currentPattern=tempVar2,tempVar5
                self.xpos,self.ypos=tempVar3,tempVar4
            else:
                self.holdBox.getPatternForBox(self.arr[self.currentPattern], self.currentPattern)
                self.spawnPattern()

            self.holdBox.showPatternOnBox()
            self.checkRowFull()

    # check all the row in the board for any row that is full. if a row is
    # full then it will be cleared and the player will get 100 points
    def checkRowFull(self):
        rowFull=False
        for i in range(12,31):
            tempArr=self.boards.boardArr[i][1:11]
            if tempArr.count((0,0,0))==0:
                rowFull=True
                for j in range(i,11,-1):
                    for x in range(1,11):
                        self.boards.boardArr[j][x]=self.boards.boardArr[j-1][x]
                self.timerScore.increaseScore()
        if rowFull:
            self.music.levelUpNoise()

    def checkDeath(self):
        for e in self.boards.boardArr[11]:
            if e!=(0,0,0) and e!=(218,204,231):
                return True

    # rotates the pattern to it's next phase and check for any collision if so
    # the pattern will not rotate
    def rotation(self):
        self.cleanSpot(self.xpos, self.ypos, self.pattern[self.patternPhase])
        if (self.collisionRotate(self.pattern, self.xpos,self.ypos, self.patternPhase) != True):
            self.patternPhase += 1
            self.patternPhase %= len(self.pattern)
        self.showPattern(self.xpos, self.ypos, self.pattern[self.patternPhase])
