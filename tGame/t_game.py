import tetris
import board
import boards
import neopixel
import time
import RPi.GPIO as GPIO
import sys
import tetris_music

run=True
GPIO.setmode(GPIO.BCM)

# setting up the board and strips
pixel_pin = board.D21
num_pixels = 512
ORDER = neopixel.RGB
strips = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER)
boards = boards.boards(50, 0, 32, 16,strips)
music=tetris_music.music()

tetris=tetris.tetris(strips,boards,music)
tetris.spawnPattern()

# some var
lastTime=time.time()
gameEnd=False
level=1
lastLevelScore=0
gameSpeedMultiplier=1
updateTimeInterval=0.5
holdDown=False

# var and setup for inputs
down=19
up=20
left=26
right=16
btn=13
GPIO.setup(down, GPIO.IN)
GPIO.setup(up, GPIO.IN)
GPIO.setup(left, GPIO.IN)
GPIO.setup(right, GPIO.IN)
GPIO.setup(btn, GPIO.IN)

# mean game loop
try:
    while run:

        # down input makes the pattern drop faster when holding down
        if GPIO.input(down):
            updateTimeInterval=0.08
        else:
            updateTimeInterval=0.5

        # left right inputs moves the pattern left right
        # up inputs change the state the of the pattern
        # the btn inputs does the pattern switch the current pattern with pattern on hold
        # holdDown stops the user from spamming the inputs and only takes in one inputs at a time
        # holdDown resets when the user are not holding down on the inputs
        if not holdDown:
            if GPIO.input(btn):
                tetris.switchPattern()
                holdDown=True
            elif GPIO.input(left):
                tetris.moveLeft()
                holdDown=True
            elif GPIO.input(right):
                tetris.moveRight()
                holdDown=True
            elif GPIO.input(up):
                tetris.rotation()
                holdDown=True
        elif not (GPIO.input(btn) or GPIO.input(left) or GPIO.input(right) or GPIO.input(up)):
            holdDown=False
        
        # the update speed of the board depends on the updateTimeInterval and gameSpeedMultiplier
        # during each update program also check for death and if death is true player will have 2
        # option. restart the game(btn down) or turn of the program(btn down and up down)
        if time.time()-lastTime>=updateTimeInterval/gameSpeedMultiplier and not gameEnd:
            if tetris.patternMoveDown():
                music.gameOverTheme()
                while True:
                    if GPIO.input(btn):
                        boards.reset_strip()
                        tetris.timerScore.setScore(0)
                        tetris.timerScore.resetTime()
                        tetris.spawnPattern()
                        tetris.holdBox.removePatternInfo()
                        holdDown=True
                        break
                    elif GPIO.input(up) and GPIO.input(btn):
                        strips.deinit()
                        sys.exit(0)
            lastTime=time.time()

        currentScored=tetris.timerScore.getScore()
        scoresEarned=currentScored-lastLevelScore

        # checks for level ups and if condition meets player will be leveled up
        # and the game speed will increase by increasing the gameSpeedMultiplier
        if level<3 and scoresEarned==1000:
            level+=1
            gameSpeedMultiplier+=0.25
            lastLevelScore=currentScored
            music.levelUpNoise()
        elif level<5 and scoresEarned==1500:
            level+=1
            gameSpeedMultiplier+=0.3
            lastLevelScore=currentScored
            musiclevelUpNoise()
        elif level<7 and scoresEarned==2000:
            level+=1
            gameSpeedMultiplier+=0.35
            lastLevelScore=currentScored
            music.levelUpNoise()
        elif level>=7 and scoresEarned==3000:
            level+=1
            gameSpeedMultiplier+=0.4
            lastLevelScore=currentScored
            music.levelUpNoise()
        
        tetris.timerScore.getGameTime()
        music.checkReplay()
finally:
    strips.deinit()