#!/usr/bin/python
"""Simple Snake Game"""
# pylint: disable=C0103
# Imports {{{1
import sys
import random
import time
pg = __import__('pygame')
# Constants {{{1
FPS = 60
COLORS = {
    "bg": (0, 0, 0),
    "snake": (64, 255, 64),
    "food": (255, 32, 32),
    "font": (32, 192, 255)
}
box = 10
DIMENSIONS = (500, 300)
xl, yl = DIMENSIONS
SPEED = 6  # speed
sta = 5  # no. of blocks at
poi = 5  # no. of current length points
pro = last_key = pg.K_DOWN
Position = [[5, 15], [6, 15], [7, 15], [8, 15], [9, 15]]
# Snake food {{{1
def gen_food_location(position):
    """Return the new location for snek fod"""
    food = [random.randint(0, int(xl / box) - 1),
            random.randint(0, int(yl / box) - 1)]
    while food in Position:
        food = [random.randint(0, int(xl / box) - 1),
            random.randint(0, int(yl / box) - 1)]
    return food

# draw rectangles {{{1
def draw(color, *position):
    """Draw the given rectangles"""
    for i in position:
        pg.draw.rect(Screen, COLORS[color], (i[0] * box, i[1] * box, box, box))
        pg.draw.rect(Screen, COLORS["bg"], (i[0] * box, i[1] * box, box,
                     box), 1)

# Check is snek got fod {{{1
def check(_last_key, food):
    """Check if food eaten"""
    sto = Position.pop(0)
    Position.append([0, 0])
    if _last_key < pg.K_DOWN and _last_key + pro != pg.K_RIGHT + pg.K_LEFT:
        Position[-1][0] = Position[-2][0]
        if _last_key == pg.K_RIGHT:
            Position[-1][1] = Position[-2][1] - 1
        elif _last_key == pg.K_LEFT:
            Position[-1][1] = Position[-2][1] + 1
    elif _last_key > pg.K_LEFT:
        Position[-1][1] = Position[-2][1]
        if _last_key == pg.K_UP:  # and pro !=pg.K_DOWN:
            Position[-1][0] = Position[-2][0] - 1
        elif _last_key == pg.K_DOWN and pro != pg.K_UP:
            Position[-1][0] = Position[-2][0] + 1
    if Position[-1] == food[0]:
        Position.insert(0, sto)
        food = gen_food_location(Position)
        draw("snake", food)
        return food
    return None


# Draw text {{{1
def draw_text(text):
    """Draw text"""
    time.sleep(2)
    font = pg.font.Font(pg.font.get_default_font(), 20)
    font_surface = font.render(f'{text} {poi-5} points', True, COLORS["font"], (0, 0, 0))
    rect = font_surface.get_rect(center=(xl / 2, yl / 2))
    Screen.fill((0, 0, 0))
    Screen.blit(font_surface, rect)
    pg.display.update()
    time.sleep(2)
    pg.quit()
    sys.exit()

# Initialization {{{1
pg.init()
fpsClock = pg.time.Clock()
Screen = pg.display.set_mode(DIMENSIONS, 0, 32)
pg.display.set_caption('Snake Game 0.2')
pg.mixer.music.load('bensound-slowmotion.mp3')
pg.mixer.music.play(-1, 1)
food = gen_food_location(Position)
draw("snake", food)
pg.display.update()

counter = 0
paused = False
lis = {round(i*FPS/SPEED) for i in range(SPEED+1)}

# Game Loop {{{1
while True:
    # Event Loop {{{2
    ert = False
    for event in pg.event.get():
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_q:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                paused = not paused
            elif last_key != event.key and event.key in {pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN}:
                if (last_key in {pg.K_LEFT, pg.K_RIGHT} and event.key in {pg.K_UP, pg.K_DOWN}) or \
                        (last_key in {pg.K_UP, pg.K_DOWN} and event.key in {pg.K_LEFT, pg.K_RIGHT}):
                    last_key = event.key
        ert = True
        pro = last_key

    # dunno {{{2
    if (last_key == pro and counter in lis or last_key != pro) and not paused:
        wer = Position[0]
        www = check(last_key, food)
        if www is not None:
            food = www
            poi += 1
        if any(Position.count(i) - 1 for i in Position):
            draw_text('You Just Ate Yourself')
        if not (-1 < Position[-1][0] < xl / box and -1 < Position[-1][1] < yl / box):
            draw_text('You Experienced Kinetic Energy')
        pg.draw.rect(Screen, COLORS["bg"], (wer[0] * box, wer[1] * box, box,
                     box))
        draw("snake", *Position)
        ert = True
        if last_key != pro:
            counter = 0

    counter += 1
    if counter > FPS:
        counter %= FPS
    if not paused:
        pg.display.update()
    fpsClock.tick(FPS)
