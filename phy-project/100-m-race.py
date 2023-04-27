import pygame
import math
import sys


# drawing the track and other things
def make_track():
    pygame.draw.rect(gameDisplay, (255, 255, 255), (0, 0, 700, 470))
    pygame.draw.rect(gameDisplay, (255, 0, 0), (300, 40, 50, 400))
    for i in range(0, 50, 13):
        pygame.draw.line(gameDisplay, (255, 255, 255), (300 + i, 40), (300 + i, 440))
    pygame.draw.line(gameDisplay, (255, 255, 255), (300, 420), (350, 420))
    pygame.draw.line(gameDisplay, (255, 255, 255), (300, 60), (350, 60))
    pygame.draw.circle(gameDisplay, (0, 0, 0), (326, 440), 3)
    pygame.draw.circle(gameDisplay, (0, 0, 0), (326, 40), 3)
    gameDisplay.blit(end_p, (350, 40))
    gameDisplay.blit(start_p, (350, 440))
    runner(round(runner_x), round(runner_y))


# making the runner
def runner(x, y):
    pygame.draw.circle(gameDisplay, (0, 255, 0), (x, y), 4)
    pygame.draw.line(gameDisplay, (0, 0, 0), (x, y + 4), (x, y + 14))
    pygame.draw.line(gameDisplay, (0, 0, 0), (x, y + 14), (x - 5, y + 19))
    pygame.draw.line(gameDisplay, (0, 0, 0), (x, y + 14), (x + 5, y + 19))
    pygame.draw.line(gameDisplay, (0, 0, 0), (x, y + 7), (x - 5, y + 10))
    pygame.draw.line(gameDisplay, (0, 0, 0), (x, y + 7), (x + 5, y + 10))


def angle_indicator(deg):
    pygame.draw.rect(gameDisplay, (255, 255, 255), (489, 520, 101, 50))
    pygame.draw.line(gameDisplay, (0, 0, 0), (489, 570), (589, 570))
    pygame.draw.line(gameDisplay, (0, 0, 0), (539, 570), (539, 520))
    if deg <= 0:
        pygame.draw.line(gameDisplay, (124, 252, 0), (539, 570),
                         (539 - round(math.sin(math.radians(abs(deg))) * 50),
                          570 - round(math.cos(math.radians(abs(deg))) * 50)))
    else:
        pygame.draw.line(gameDisplay, (124, 252, 0), (539, 570),
                         (539 + round(math.sin(math.radians(deg)) * 50), 570 - round(math.cos(math.radians(deg)) * 50)))


def velocity_vector(runner_speed, wind_speed, track_boost, launch_angle):
    pygame.draw.rect(gameDisplay, (240, 230, 140), (490, 160, 210, 250))
    pygame.draw.rect(gameDisplay, (0, 0, 0), (495, 165, 206, 240), 1)
    if launch_angle <= 0:
        pygame.draw.line(gameDisplay, (0, 255, 0), (601, 350),
                         (round(601 - math.sin(math.radians(abs(launch_angle))) * runner_speed),
                          round(350 - math.cos(math.radians(abs(launch_angle))) * runner_speed)), 3)
        pygame.draw.line(gameDisplay, (255, 0, 0),
                         (round(601 - math.sin(math.radians(abs(launch_angle))) * runner_speed),
                          round(350 - math.cos(math.radians(abs(launch_angle))) * runner_speed)),
                         (round(601 - math.sin(math.radians(abs(launch_angle))) * runner_speed + wind_speed),
                          round(350 - math.cos(math.radians(abs(launch_angle))) * runner_speed)), 3)
        pygame.draw.line(gameDisplay, (0, 0, 255),
                         (round(601 - math.sin(math.radians(abs(launch_angle))) * runner_speed + wind_speed),
                          round(350 - math.cos(math.radians(abs(launch_angle))) * runner_speed)),
                         (round(601 - math.sin(math.radians(abs(launch_angle))) * runner_speed + wind_speed),
                          round(350 - math.cos(math.radians(abs(launch_angle))) * runner_speed - track_boost)),
                         3)
        pygame.draw.line(gameDisplay, (169, 169, 169), (601, 350),
                         (round(601 - math.sin(math.radians(abs(launch_angle))) * runner_speed + wind_speed),
                          round(350 - math.cos(math.radians(abs(launch_angle))) * runner_speed - track_boost)),
                         3)
    else:
        pygame.draw.line(gameDisplay, (124, 252, 0), (601, 350),
                         (round(601 + math.sin(math.radians(launch_angle)) * runner_speed),
                          round(350 - math.cos(math.radians(launch_angle)) * runner_speed)), 3)
        pygame.draw.line(gameDisplay, (255, 0, 0),
                         (round(601 + math.sin(math.radians(abs(launch_angle))) * runner_speed),
                          round(350 - math.cos(math.radians(abs(launch_angle))) * runner_speed)),
                         (round(601 + math.sin(math.radians(abs(launch_angle))) * runner_speed + wind_speed),
                          round(350 - math.cos(math.radians(abs(launch_angle))) * runner_speed)), 3)
        pygame.draw.line(gameDisplay, (0, 0, 255),
                         (round(601 + math.sin(math.radians(abs(launch_angle))) * runner_speed + wind_speed),
                          round(350 - math.cos(math.radians(abs(launch_angle))) * runner_speed)),
                         (round(601 + math.sin(math.radians(abs(launch_angle))) * runner_speed + wind_speed),
                          round(350 - math.cos(math.radians(abs(launch_angle))) * runner_speed - track_boost)),
                         3)
        pygame.draw.line(gameDisplay, (169, 169, 169), (601, 350),
                         (round(601 + math.sin(math.radians(abs(launch_angle))) * runner_speed + wind_speed),
                          round(350 - math.cos(math.radians(abs(launch_angle))) * runner_speed - track_boost)),
                         3)
    return (math.sin(math.radians(launch_angle)) * runner_speed + wind_speed) / 250, (
            math.cos(math.radians(launch_angle)) * runner_speed + track_boost) / 250


runner_x = 326
runner_y = 440

# intialize the pygame(have to be done every progam)
pygame.init()

# set up icon
# icon=pygame.image.load('ss.jpg')
# pygame.display.set_icon(icon)

# set the windows size
gameDisplay = pygame.display.set_mode((700, 650))
# set the name of the windows
pygame.display.set_caption('Physics Assignment')
# change background
gameDisplay.fill((255, 255, 255))

# text
font1 = pygame.font.SysFont('Times New Roman', 15)
font2 = pygame.font.SysFont('Times New Roman', 22)
end_p = font1.render('End point', False, (0, 0, 0))
start_p = font1.render('Start point', False, (0, 0, 0))
method = font2.render('Method:', False, (0, 0, 0))
runner_s = font1.render('Participant Speed:', False, (0, 0, 0))
wind_s = font1.render('Wind Speed:', False, (0, 0, 0))
time_d = font1.render('Time Delay:', False, (0, 0, 0))
track_b = font1.render('Track Boost:', False, (0, 0, 0))
launch_a = font1.render('Launch Angle:', False, (0, 0, 0))
velocity_v = font1.render('Velocity Vector:', False, (0, 0, 0))
time_t = font1.render('Time:', False, (0, 0, 0))
animation_speed = font1.render('Animation Speed:', False, (0, 0, 0))
long_ways = font1.render('Long Way:', False, (0, 0, 0))
north = font1.render('N', False, (0, 0, 0))

gameDisplay.blit(method, (70, 450))
gameDisplay.blit(runner_s, (200, 480))
gameDisplay.blit(launch_a, (430, 578))
gameDisplay.blit(time_t, (10, 10))
gameDisplay.blit(animation_speed, (200, 10))
gameDisplay.blit(north, (535, 495))


# code for working buttons
class buttons:
    def __init__(self, x, y, s_face, text=''):
        self.x = x
        self.y = y
        self.text = text
        self.s_face = s_face
        self.clicked = False
        self.font = pygame.font.SysFont('Times New Roman', 12)

    def draw(self):
        if self.clicked:
            pygame.draw.rect(self.s_face, (255, 0, 0), (self.x, self.y, 80, 30))
        else:
            pygame.draw.rect(self.s_face, (173, 230, 230), (self.x, self.y, 80, 30))
        pygame.draw.rect(self.s_face, (0, 0, 0), (self.x, self.y, 80, 30), 1)
        word = self.font.render(self.text, False, (0, 0, 0))
        self.s_face.blit(word, (self.x + 80 // 2 - (len(self.text) * 6) // 2, self.y + 30 // 2 - 7))

    def click(self, pos):
        if self.x <= pos[0] <= self.x + 80 and self.y <= pos[1] <= self.y + 30:
            self.clicked = True
            return True
        else:
            self.clicked = False


# code for working slider
class sliders:
    def __init__(self, l_x, l_y, size, s_face, scale, pos, angle, units=''):
        if angle:
            self.s_x = l_x + size // 2
            self.rect_len = len(str(size // 2 * scale))
        else:
            self.s_x = l_x
            self.rect_len = len(str(size // scale))
        self.l_x = l_x
        self.l_y = l_y
        self.size = size
        self.s_face = s_face
        self.clicked = False
        self.font = pygame.font.SysFont('Times New Roman', 15)
        self.value = 0 / scale
        self.player_speed = self.font.render(str(self.value), False, (0, 0, 0))
        self.scale = scale
        self.pos = pos
        self.units = units

    def draw(self, pos, update, number):
        pygame.draw.rect(self.s_face, (255, 255, 255), (self.l_x - 6, self.l_y - 6, self.size + 12, 12))
        pygame.draw.line(self.s_face, (0, 0, 0), (self.l_x, self.l_y), (self.l_x + self.size, self.l_y), 4)
        if self.clicked or update:
            self.s_x = round(pos[0])
            self.value = (pos[0] - self.l_x) / self.scale
            if self.s_x > self.l_x + self.size:
                self.s_x = self.l_x + self.size
                self.value = self.size / self.scale
            elif self.s_x < self.l_x:
                self.s_x = self.l_x
                self.value = 0.0
            pygame.draw.circle(self.s_face, (255, 0, 0), (self.s_x, self.l_y), 6)
        else:
            pygame.draw.circle(self.s_face, (255, 204, 203), (self.s_x, self.l_y), 6)
        self.player_speed = self.font.render(str(self.value) + ' ' + self.units, False, (0, 0, 0))
        if number:
            pygame.draw.rect(self.s_face, (255, 255, 255), (self.pos[0], self.pos[1], self.rect_len * 27, 18))
            self.s_face.blit(self.player_speed, self.pos)
        return self.value

    def click(self, pos):
        if self.s_x - 6 <= pos[0] <= self.s_x + 6 and self.l_y - 6 <= pos[1] <= self.l_y + 6 and self.clicked == False:
            self.clicked = True
        else:
            self.clicked = False

    def draw_angle(self, pos, update, val, number):
        pygame.draw.rect(self.s_face, (255, 255, 255), (self.l_x - 6, self.l_y - 6, self.size + 12, 12))
        pygame.draw.line(self.s_face, (0, 0, 0), (self.l_x, self.l_y), (self.l_x + self.size, self.l_y), 4)
        if self.clicked or update:
            self.s_x = pos[0]
            if update:
                self.value = abs(val)
            elif self.s_x < self.l_x + self.size // 2:
                self.value = self.l_x + self.size // 2 - self.s_x
                if self.value > 90:
                    self.value = 90
                    self.s_x = self.l_x
            else:
                self.value = self.s_x - self.l_x - self.size // 2
                if self.value > 90:
                    self.value = 90
                    self.s_x = self.l_x + self.size
            pygame.draw.circle(self.s_face, (255, 0, 0), (self.s_x, self.l_y), 6)
        else:
            pygame.draw.circle(self.s_face, (255, 204, 203), (self.s_x, self.l_y), 6)
        if number:
            self.player_speed = self.font.render(str(self.value) + ' ' + self.units, False, (0, 0, 0))
            pygame.draw.rect(self.s_face, (255, 255, 255), (self.pos[0], self.pos[1], self.rect_len * 23 + 1, 15))
            self.s_face.blit(self.player_speed, self.pos)
        if self.s_x < self.l_x + self.size // 2:
            return self.value * -1
        else:
            return self.value


# code for working text box
class text_boxs:
    def __init__(self, x, y, size, s_face, font, number_behind, units):
        self.x = x
        self.y = y
        self.size = size
        self.s_face = s_face
        self.font = font
        self.number_behind = number_behind
        self.clicked = False
        self.units = units

    def draw(self):
        pygame.draw.rect(self.s_face, (0, 0, 0), (self.x, self.y, self.size[0], self.size[1]), 1)

    def click(self, pos):
        if self.x <= pos[0] <= self.x + self.size[0] and self.y <= pos[1] <= self.y + self.size[1] and not self.clicked:
            pygame.draw.rect(self.s_face, (255, 255, 255), (self.x + 1, self.y + 1, self.size[0] - 2, 15))
            self.clicked = True
            return True
        else:
            self.clicked = False

    def update(self, number, numbers, done, bar_max_val, angle):
        if not done:
            numbers += number
            pygame.draw.rect(self.s_face, (255, 255, 255), (self.x + 1, self.y + 1, self.size[0] - 2, 15))
            word = self.font.render(numbers + ' ' + self.units, False, (0, 0, 0))
            self.s_face.blit(word, (self.x + 2, self.y + 1))
            pygame.draw.rect(self.s_face, (255, 255, 255), (self.x + self.size[0], self.y, 400, 15))
            return numbers
        else:
            if numbers.count('.') and numbers.index('.') == len(numbers) - 1:
                numbers = numbers[0:len(numbers) - 1]
            if len(numbers) == 0:
                numbers = '0.0'
            pygame.draw.rect(self.s_face, (255, 255, 255), (self.x + 1, self.y + 1, self.size[0] - 2, 15))
            if angle:
                if abs(float(numbers)) > bar_max_val:
                    if float(numbers) < 0:
                        numbers = -bar_max_val
                    else:
                        numbers = bar_max_val
                else:
                    numbers = round(float(numbers) * 10 ** self.number_behind) / 10 ** self.number_behind
            else:
                if float(numbers) > bar_max_val:
                    numbers = bar_max_val
                elif float(numbers) < 0:
                    numbers = 0.0
                else:
                    numbers = round(float(numbers) * 10 ** self.number_behind) / 10 ** self.number_behind
            word = self.font.render(str(abs(numbers)) + ' ' + self.units, False, (0, 0, 0))
            self.s_face.blit(word, (self.x + 2, self.y + 1))
            pygame.draw.rect(self.s_face, (255, 255, 255), (self.x + self.size[0], self.y, 400, 15))
            self.clicked = False
            return numbers


# set up buttons
winds = buttons(10, 490, gameDisplay, 'Winds')
winds.draw()
time_delay = buttons(100, 490, gameDisplay, 'Time Delay')
time_delay.draw()
track_boost = buttons(10, 540, gameDisplay, 'Track Boost')
track_boost.draw()
start_buttons = buttons(360, 600, gameDisplay, 'Start')
start_buttons.draw()
stop_buttons = buttons(275, 600, gameDisplay, 'Stop')
stop_buttons.draw()
reset_buttons = buttons(190, 600, gameDisplay, 'Reset')
reset_buttons.draw()
long_way = buttons(100, 540, gameDisplay, 'Long Way')
long_way.draw()

# sleep or the fps rate of the program
sleep = pygame.time.Clock()

# setup text box
box1 = text_boxs(323, 480, (60, 20), gameDisplay, font1, 3, 'm/s')
box1.draw()
box2 = text_boxs(323, 540, (60, 20), gameDisplay, font1, 3, '')
box2.draw()
box3 = text_boxs(530, 578, (60, 20), gameDisplay, font1, 3, '°')
box3.draw()

# set up slider
runner_speed = sliders(280, 510, 100, gameDisplay, 10, (325, 481), False, 'm/s')
runner_speed.draw(0, False, True)
method_value = sliders(280, 570, 100, gameDisplay, 10, (325, 541), False, '')
method_value.draw(0, False, True)
launch_angle = sliders(450, 610, 180, gameDisplay, 1, (532, 580), True, '°')
launch_angle.draw_angle(0, False, 0, True)
animation_multipliers = sliders(330, 20, 100, gameDisplay, 100, (325, 541), False, '')
animation_multipliers.draw(0, False, False)

make_track()
angle_indicator(0)
velocity_vector(0, 0, 0, 0)

# program variable setup
speeds = 0
box1_number = ''
box2_number = ''
box3_number = ''
key_dict = {
    48: '0',
    49: '1',
    50: '2',
    51: '3',
    52: '4',
    53: '5',
    54: '6',
    55: '7',
    56: '8',
    57: '9'
}
wind = False
time = False
track = False
there = False
long = False
wind_n = 0
track_n = 0
longs_ways = 0
launch_ang = 0
time_n = 0
times = 0.0
move = False
change = True
velocity_x, velocity_y = 0, 0
animation_multiplier = 1.0
moved_x = 0
moved_y = 0

times_t = font1.render('0.00 s', False, (0, 0, 0))
gameDisplay.blit(times_t, (50, 11))

run=True

# mean game loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if not move and change and winds.click(event.pos):
                    pygame.draw.rect(gameDisplay, (255, 255, 255), (225, 540, 90, 20))
                    pygame.draw.rect(gameDisplay, (255, 255, 255), (323, 540, 80, 20))
                    pygame.draw.rect(gameDisplay, (255, 255, 255), (385, 564, 101, 12))
                    gameDisplay.blit(wind_s, (225, 540))
                    method_value = sliders(280, 570, 100, gameDisplay, 10, (325, 541), False, 'm/s')
                    method_value.draw(event.pos, False, True)
                    box2 = text_boxs(323, 540, (60, 20), gameDisplay, font1, 3, 'm/s')
                    wind = True
                    time = False
                    track = False
                    long = False
                    box2_number = ''
                if not move and change and time_delay.click(event.pos):
                    pygame.draw.rect(gameDisplay, (255, 255, 255), (225, 540, 90, 20))
                    pygame.draw.rect(gameDisplay, (255, 255, 255), (323, 540, 80, 20))
                    pygame.draw.rect(gameDisplay, (255, 255, 255), (385, 564, 101, 12))
                    gameDisplay.blit(time_d, (225, 540))
                    method_value = sliders(280, 570, 200, gameDisplay, 1, (325, 541), False, 's')
                    box2 = text_boxs(323, 540, (80, 20), gameDisplay, font1, 2, 's')
                    box2.draw()
                    method_value.draw(event.pos, False, True)
                    wind = False
                    time = True
                    track = False
                    long = False
                    box2_number = ''
                if not move and change and track_boost.click(event.pos):
                    pygame.draw.rect(gameDisplay, (255, 255, 255), (225, 540, 90, 20))
                    pygame.draw.rect(gameDisplay, (255, 255, 255), (323, 540, 80, 20))
                    pygame.draw.rect(gameDisplay, (255, 255, 255), (385, 564, 101, 12))
                    gameDisplay.blit(track_b, (225, 540))
                    method_value = sliders(280, 570, 100, gameDisplay, 10, (325, 541), False, 'm/s')
                    box2 = text_boxs(323, 540, (60, 20), gameDisplay, font1, 3, 'm/s')
                    method_value.draw(event.pos, False, True)
                    wind = False
                    time = False
                    track = True
                    long = False
                    box2_number = ''
                if start_buttons.click(event.pos):
                    move = True
                    change = False
                    times += time_n
                if stop_buttons.click(event.pos):
                    move = False
                if reset_buttons.click(event.pos):
                    move = False
                    change = True
                    times = 0
                    moved_x = 0
                    moved_y = 0
                    runner_x = 326
                    runner_y = 440
                    there = False
                    pygame.draw.rect(gameDisplay, (255, 255, 255), (50, 11, 150, 20))
                    times_t = font1.render('0.00 s', False, (0, 0, 0))
                    gameDisplay.blit(times_t, (50, 11))
                    longs_ways=method_value.value
                    moved_y = 0
                    moved_x = 0
                if not move and change and long_way.click(event.pos):
                    pygame.draw.rect(gameDisplay, (255, 255, 255), (225, 540, 90, 20))
                    gameDisplay.blit(long_ways, (225, 540))
                    method_value = sliders(280, 570, 200, gameDisplay, 1 / 3, (325, 541), False, 'm')
                    box2 = text_boxs(323, 540, (80, 20), gameDisplay, font1, 2, 'm')
                    box2.draw()
                    method_value.draw(event.pos, False, True)
                    wind = False
                    time = False
                    track = False
                    long = True
                    wind_n = 0
                    time_n = 0
                    track_n = 0
                    box2_number = ''

                winds.draw()
                time_delay.draw()
                track_boost.draw()
                start_buttons.draw()
                stop_buttons.draw()
                reset_buttons.draw()
                long_way.draw()

                if not move and change:
                    runner_speed.click(event.pos)
                    method_value.click(event.pos)
                    launch_angle.click(event.pos)
                animation_multipliers.click(event.pos)

                if not move and change and box2.click(event.pos):
                    box2_number = ''
                else:
                    box2.update('', box2_number, True, method_value.size // method_value.scale, False)
                    method_value.draw(event.pos, False, False)
                if not move and change and box1.click(event.pos):
                    box1_number = ''
                else:
                    box1.update('', box1_number, True, runner_speed.size // runner_speed.scale, False)
                    runner_speed.draw(event.pos, False, False)
                if not move and change and box3.click(event.pos):
                    box3_number = ''
                else:
                    box3.update('', box3_number, True, launch_angle.size // launch_angle.scale, True)
                    launch_angle.draw_angle(event.pos, False, 0, False)

                if not box1.clicked and runner_speed.clicked:
                    runner_speed.draw(event.pos, False, False)
                if not box2.clicked and method_value.clicked:
                    method_value.draw(event.pos, False, False)
                if not box3.clicked and launch_angle.clicked:
                    launch_angle.draw_angle(event.pos, False, 0, False)
                animation_multipliers.draw(event.pos, False, False)

        elif event.type == pygame.MOUSEMOTION:
            if not move and change and runner_speed.clicked:
                speeds = runner_speed.draw(event.pos, False, True)
                box1_number = str(speeds)
            elif not move and change and method_value.clicked:
                if wind:
                    wind_n = method_value.draw(event.pos, False, True)
                    box2_number = str(wind_n)
                elif track:
                    track_n = method_value.draw(event.pos, False, True)
                    box2_number = str(track_n)
                elif time:
                    time_n = method_value.draw(event.pos, False, True)
                    box2_number = str(time_n)
                elif long:
                    longs_ways = method_value.draw(event.pos, False, True)
                    box2_number = str(longs_ways)
                else:
                    box2_number = str(method_value.draw(event.pos, False, True))
            elif not move and change and launch_angle.clicked:
                launch_ang = launch_angle.draw_angle(event.pos, False, 0, True)
                box3_number = str(abs(launch_ang))
            elif animation_multipliers.clicked:
                animation_multiplier = 1 + animation_multipliers.draw(event.pos, False, False)

        elif event.type == pygame.KEYDOWN:
            if box1.clicked:
                if 48 <= event.key <= 57:
                    box1_number = box1.update(key_dict[event.key], box1_number, False, 10, False)
                elif event.key == 46:
                    if box1_number.count('.') == 0:
                        box1_number = box1.update('.', box1_number, False, 10, False)
                elif event.key == 8:
                    box1_number = box1.update('', box1_number[0:len(box1_number) - 1], False, 10, False)
                elif event.key == 13:
                    speeds = float(box1.update('', box1_number, True, 10, False))
                    runner_speed.draw((runner_speed.l_x + int(speeds * 10), 0), True, False)
            elif box2.clicked:
                if 48 <= event.key <= 57:
                    box2_number = box2.update(key_dict[event.key], box2_number, False, 10, False)
                elif event.key == 46:
                    if box2_number.count('.') == 0:
                        box2_number = box2.update('.', box2_number, False, 10, False)
                elif event.key == 8:
                    box2_number = box2.update('', box2_number[0:len(box2_number) - 1], False, 10, False)
                elif event.key == 13:
                    if wind:
                        wind_n = float(box2.update('', box2_number, True, 10, False))
                        method_value.draw((method_value.l_x + int(wind_n * 10), 0), True, False)
                    elif track:
                        track_n = float(box2.update('', box2_number, True, 10, False))
                        method_value.draw((method_value.l_x + int(track_n * 10), 0), True, False)
                    elif long:
                        longs_ways = float(box2.update('', box2_number, True, 600, False))
                        method_value.draw((method_value.l_x + longs_ways/3, 0), True, False)
                    elif time:
                        time_n = float(box2.update('', box2_number, True, 200, False))
                        method_value.draw((method_value.l_x + time_n, 0), True, False)
                    else:
                        method_value.draw(
                            (method_value.l_x + int(float(box2.update('', box2_number, True, 10, False)) * 10), 0),
                            True, False)
            elif box3.clicked:
                if 48 <= event.key <= 57:
                    box3_number = box3.update(key_dict[event.key], box3_number, False, 90, True)
                elif event.key == 46:
                    if box3_number.count('.') == 0:
                        box3_number = box3.update('.', box3_number, False, 90, True)
                elif event.key == 8:
                    box3_number = box3.update('', box3_number[0:len(box3_number) - 1], False, 90, True)
                elif event.key == 13:
                    launch_ang = float(box3.update('', box3_number, True, 90, True))
                    launch_angle.draw_angle((launch_angle.l_x + launch_angle.size // 2 + int(launch_ang), 0), True,
                                            launch_ang, False)
                elif event.key == 45:
                    if box3_number.count('-') == 0:
                        box3_number = box3.update('-', box3_number, False, 90, True)

    if move and not long:
        runner_y -= velocity_y
        runner_x += velocity_x
        times += 0.01
        pygame.draw.rect(gameDisplay, (255, 255, 255), (50, 11, 150, 20))
        if round(runner_y * 10) / 10 <= 40:
            runner_y = 40
            move = False
    elif move and long and longs_ways > 0:
        runner_y -= velocity_y
        runner_x += velocity_x
        moved_x += abs(velocity_x)
        moved_y += abs(velocity_y)
        times += 0.01
        pygame.draw.rect(gameDisplay, (255, 255, 255), (50, 11, 150, 20))
        if round(math.sqrt(moved_x ** 2 + moved_y ** 2) * 100) / 100 >= 4 * longs_ways:
            if (400 - moved_y) >= 0:
                if runner_x <= 326:
                    velocity_x, velocity_y = velocity_vector(speeds, 0, 0, round(math.degrees(
                        math.atan(moved_x / (400 - moved_y))) * 100) / 100)
                else:
                    velocity_x, velocity_y = velocity_vector(speeds, 0, 0, round(math.degrees(
                        math.atan(moved_x / (400 - moved_y))) * 100) / 100)
                    velocity_x *= -1
                longs_ways = math.sqrt((400 - moved_y) ** 2 + moved_x ** 2) / 4
            else:
                if runner_x <= 326:
                    velocity_x, velocity_y = velocity_vector(speeds, 0, 0, round(math.degrees(
                        math.atan(moved_x / abs(400 - moved_y))) * 100) / 100)
                    velocity_y *= -1
                else:
                    velocity_x, velocity_y = velocity_vector(speeds, 0, 0, round(math.degrees(
                        math.atan(moved_x / abs(400 - moved_y))) * 100) / 100)
                    velocity_y *= -1
                    velocity_x *= -1
                longs_ways = math.sqrt((400 - moved_y) ** 2 + moved_x ** 2) / 4
            if there:
                there = False
                move = False
            else:
                there = True
            velocity_x *= 10
            velocity_y *= 10
            moved_x = 0
            moved_y = 0
            print(longs_ways)

    make_track()
    angle_indicator(launch_ang)
    if not move:
        velocity_x, velocity_y = velocity_vector(speeds * 10, wind_n * 10, track_n * 10, launch_ang)
    else:
        velocity_vector(speeds * 10, wind_n * 10, track_n * 10, launch_ang)
    gameDisplay.blit(velocity_v, (550, 135))
    box2.draw()
    gameDisplay.blit(method, (70, 450))
    times_t = font1.render('Time: ' + str(round(times * 100) / 100) + ' s', False, (0, 0, 0))
    gameDisplay.blit(times_t, (10, 11))
    animation_multipliers.draw((animation_multipliers.s_x, 0), False, False)
    gameDisplay.blit(animation_speed, (200, 10))

    # update the program
    pygame.display.update()
    sleep.tick(round(500 * animation_multiplier))

sys.exit(0)