
class boards:
    def __init__(self,x,y,l,w,strips):
        self.x=x
        self.y=y
        self.l=l
        self.w=w
        self.strips=strips
        self.boardArr=[[(0,0,0) for i in range(w)] for j in range(l)]

        if l==32:
            for i in range(20):
                self.boardArr[11+i][0]=(218,204,231)
                self.boardArr[11+i][11] = (218, 204, 231)
            for i in range(12):
                self.boardArr[10][i] = (218, 204, 231)
                self.boardArr[31][i] = (218, 204, 231)

    # takes the data from the boardArr and formats them into the strips so it can be
    # display on the led strips
    def update_strip(self):
        ind=511
        for i in range(self.l):
            if i%2==0:
                for j in range(self.w//2):
                    self.strips[ind-j]=self.boardArr[i][8+j]
                    self.strips[ind - j-256] = self.boardArr[i][j]
            else:
                for j in range(self.w // 2):
                    self.strips[ind-j] = self.boardArr[i][15-j]
                    self.strips[ind - j - 256] = self.boardArr[i][7-j]
            ind -= 8
        self.strips.show()

    # resets the boardArr to the default and is only used the player restarts the game
    def reset_strip(self):
        self.boardArr=[[(0,0,0) for i in range(self.w)] for j in range(self.l)]

        if self.l==32:
            for i in range(20):
                self.boardArr[11+i][0]=(218,204,231)
                self.boardArr[11+i][11] = (218, 204, 231)
            for i in range(12):
                self.boardArr[10][i] = (218, 204, 231)
                self.boardArr[31][i] = (218, 204, 231)