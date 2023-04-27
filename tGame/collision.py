class collision:
    def __init__(self,board):
        self.board=board
        pass

    # checks for any collision detection on the bottom of the pattern
    # whether it's to the boarder or to another pattern
    def collisionBottom(self,ypos,xpos,pattern):
        patternLen=len(pattern)-1
        for i in range(patternLen,-1,-1):
            if pattern[i]!=[0]*(patternLen+1):
                for j in range(patternLen+1):
                    if pattern[i][j]!=0 and self.board.boardArr[ypos+i][xpos+j]!=(0,0,0):
                        return True

    # checks for any collision detection on the left of the pattern
    # whether it's to the boarder or to another pattern
    def collisionLeft(self, ypos, xpos, pattern):
        for collom in range(len(pattern)):
            for row in range(len(pattern)):
                if pattern[row][collom] == 1:
                    for j in range(len(pattern)):
                        if pattern[row][j] != 0 and self.board.boardArr[ypos + row][xpos + j] != (0, 0, 0):
                            return True

    # checks for any collision detection when pattern is rotating whether the
    # rotated pattern is out of the board or to overlapped with another pattern
    def collisionRotate(self, pattern, xpos, ypos, patternPhase):
        rotatedPatternPhase = patternPhase + 1
        rotatedPatternPhase %= len(pattern)

        for collom in range(len(pattern[rotatedPatternPhase])):
            for row in range(len(pattern[rotatedPatternPhase])):
                if pattern[rotatedPatternPhase][row][collom] == 1:
                    if not (1 <= xpos + collom <= 10):
                        return True
                    else:
                        for j in range(len(pattern[rotatedPatternPhase]) - 1, -1, -1):
                            if pattern[rotatedPatternPhase][row][j] != 0 and self.board.boardArr[ypos + row][
                                xpos + j + 1] != (0, 0, 0):
                                return True
                        for j in range(len(pattern[rotatedPatternPhase])):
                            if pattern[rotatedPatternPhase][row][j] != 0 and self.board.boardArr[ypos + row][
                                xpos + j - 1] != (0, 0, 0):
                                return True

    # checks for any collision detection on the right of the pattern
    # whether it's to the boarder or to another pattern
    def collisionRight(self, ypos, xpos,pattern):
        for collom in range(len(pattern) - 1, -1, -1):
            for row in range(len(pattern) - 1, -1, -1):
                if pattern[row][collom] == 1:
                    for j in range(len(pattern) - 1, -1, -1):
                        if pattern[row][j] != 0 and self.board.boardArr[ypos + row][xpos + j] != (0, 0, 0):
                            return True