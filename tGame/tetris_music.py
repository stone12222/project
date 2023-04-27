import vlc
import time

class music:
    def __init__(self):
        self.tetris_Theme = vlc.MediaPlayer("/home/pi/Desktop/tGame/Tetris_Theme.mp3")
        self.clear_Row_Noise = vlc.MediaPlayer("/home/pi/Desktop/tGame/Clear_Row_Noise.mp3")
        self.level_Up_Noise = vlc.MediaPlayer("/home/pi/Desktop/tGame/Level_Up_Noise.mp3")
        self.game_Over_Theme = vlc.MediaPlayer("/home/pi/Desktop/tGame/Game_Over_Theme.mp3")
        self.nextTime=time.time()-36

    def checkReplay(self):
        if time.time()-self.nextTime >= 36:
                self.nextTime = time.time()
                print('play')
                self.tetrisTheme()

    def tetrisTheme(self):
        self.tetris_Theme.stop()
        self.tetris_Theme.play()
        
    def clearRowNoise(self):
        self.clear_Row_Noise.stop()
        self.clear_Row_Noise.play()
        
    def levelUpNoise(self):
        self.level_Up_Noise.stop()
        self.level_Up_Noise.play()
        
    def gameOverTheme(self):
        self.tetris_Theme.stop()
        self.clear_Row_Noise.stop()
        self.level_Up_Noise.stop()
        self.game_Over_Theme.stop()
        self.game_Over_Theme.play()
