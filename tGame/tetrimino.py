# 7 tetris shapes (tetrimino, check from wiki)
# I, O, T, J/L, S/Z
# Each pattern will have a defined color and will not get
# a randomly generated color
# Each pattern have different phase and is stored in a 3d array called patterns

class I:
    def __init__(self):
        self.spawnx=4
        self.spawny=10
        self.color=(0,255,255)
        self.patterns=[
            [
                [0, 0, 0, 0],
                [1, 1, 1, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            [
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0]
            ],
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [1, 1, 1, 1],
                [0, 0, 0, 0]
            ],
            [
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0]
            ]
        ]
    def getColor(self):
        return self.color

    def getPattern(self):
        return self.patterns

    def getSpawnXY(self):
        return self.spawnx,self.spawny

class O:
    def __init__(self):
        self.spawnx = 4
        self.spawny = 10
        self.color = (255,255,0)
        self.patterns = [
            [
                [0, 0, 0, 0],
                [0, 1, 1, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0],
            ]
        ]

    def getColor(self):
        return self.color

    def getPattern(self):
        return self.patterns

    def getSpawnXY(self):
        return self.spawnx,self.spawny

class T:
    def __init__(self):
        self.spawnx = 4
        self.spawny = 11
        self.color = (128,0,128)
        self.patterns = [
            [
                [0, 1, 0],
                [1, 1, 1],
                [0, 0, 0]
            ],
            [
                [0, 1, 0],
                [0, 1, 1],
                [0, 1, 0]
            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [0, 1, 0]
            ],
            [
                [0, 1, 0],
                [1, 1, 0],
                [0, 1, 0]
            ]
        ]

    def getColor(self):
        return self.color

    def getPattern(self):
        return self.patterns

    def getSpawnXY(self):
        return self.spawnx,self.spawny

class L:
    def __init__(self):
        self.spawnx = 4
        self.spawny = 11
        self.color = (255,127,0)
        self.patterns = [
            [
                [0, 0, 1],
                [1, 1, 1],
                [0, 0, 0]
            ],
            [
                [0, 1, 0],
                [0, 1, 0],
                [0, 1, 1]
            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [1, 0, 0]
            ],
            [
                [1, 1, 0],
                [0, 1, 0],
                [0, 1, 0]
            ]
        ]

    def getColor(self):
        return self.color

    def getPattern(self):
        return self.patterns

    def getSpawnXY(self):
        return self.spawnx,self.spawny

class J:
    def __init__(self):
        self.spawnx = 4
        self.spawny = 11
        self.color = (0,0,255)
        self.patterns = [
            [
                [1, 0, 0],
                [1, 1, 1],
                [0, 0, 0]
            ],
            [
                [0, 1, 1],
                [0, 1, 0],
                [0, 1, 0]
            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [0, 0, 1]
            ],
            [
                [0, 1, 0],
                [0, 1, 0],
                [1, 1, 0]
            ]
        ]

    def getColor(self):
        return self.color

    def getPattern(self):
        return self.patterns

    def getSpawnXY(self):
        return self.spawnx,self.spawny

class S:
    def __init__(self):
        self.spawnx = 4
        self.spawny = 11
        self.color = (0,255,0)
        self.patterns = [
            [
                [0, 1, 1],
                [1, 1, 0],
                [0, 0, 0]
            ],
            [
                [0, 1, 0],
                [0, 1, 1],
                [0, 0, 1]
            ],
            [
                [0, 0, 0],
                [0, 1, 1],
                [1, 1, 0]
            ],
            [
                [1, 0, 0],
                [1, 1, 0],
                [0, 1, 0]
            ]
        ]

    def getColor(self):
        return self.color

    def getPattern(self):
        return self.patterns

    def getSpawnXY(self):
        return self.spawnx,self.spawny

class Z:
    def __init__(self):
        self.spawnx = 4
        self.spawny = 11
        self.color = (255,0,0)
        self.patterns = [
            [
                [1, 1, 0],
                [0, 1, 1],
                [0, 0, 0]
            ],
            [
                [0, 0, 1],
                [0, 1, 1],
                [0, 1, 0]
            ],
            [
                [0, 0, 0],
                [1, 1, 0],
                [0, 1, 1]
            ],
            [
                [0, 1, 0],
                [1, 1, 0],
                [1, 0, 0]
            ]
        ]

    def getColor(self):
        return self.color

    def getPattern(self):
        return self.patterns

    def getSpawnXY(self):
        return self.spawnx,self.spawny
