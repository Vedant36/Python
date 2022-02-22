#!/usr/bin/env python3
"""Simple Platformer Game"""
# pylint: disable=C0103
# Imports {{{1
from json import load
import time
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
pg = __import__('pygame')

# Initialisation {{{1
FPS = 60
Map = pg.Rect(0, 0, 640, 360)
pg.init()
fpsClock = pg.time.Clock()
Screen = pg.display.set_mode(Map.size, 0, 32)
pg.display.set_caption('Platformer 1.3')
KEYS = {
    "left": pg.K_a,
    "right": pg.K_d
}

# Player Class {{{1
# TODO: replace class because only one instance of it is ever used
class Player:
    """Player"""
    # Initialization {{{2
    p = pg.math.Vector2(0,0)    # momentum
    InAir = True                # in the air while jumping
    Slipping = False            # player is slipping to stop
    VertFlip = False            # is the player facing left
    JumpCount = 0
    l = [True, True]          # variables to control the inAir var
    k = time.time()
    def __init__(self, starting_position, img):
        self.r = img.get_rect(topleft=starting_position)
        self.i = img                        # player image
        self.c = Map.copy()

    # move {{{2
    def move(self, tiles):
        """Step through a single frame"""
        # Handle x-coordinate {{{3
        self.r.x += int(self.p.x)
        for tile in self.r.collidelistall(tiles):
            if self.p.x > 0:
                self.r.right = tiles[tile].left
            elif self.p.x < 0:
                self.r.left = tiles[tile].right

        # Handle y-coordinate {{{3
        self.p.y += 1
        self.r.y += int(self.p.y)
        self.l[1] = True
        for tile in self.r.collidelistall(tiles):
            if self.p.y > 0:
                self.l[1] = False
                self.r.bottom = tiles[tile].top
                if self.Slipping:
                    self.p.x -= self.p.x*0.2
                    if -0.01<self.p.x<0.01:
                        self.p.x = 0
                if self.p.x == 0:
                    self.Slipping = False
                self.JumpCount = 2
                self.k = time.time()
            elif self.p.y < 0:
                self.r.top = tiles[tile].bottom
                self.p.y *= -1
                self.p.x *= 1.1
            self.p.y = 0
        # }}}3
        self.InAir = all(self.l)
        self.l[0] = self.l[1]
        if self.r.clamp(map_rect) != self.r:
            self.r.clamp_ip(map_rect)
            self.p.y += 1

# Helper functions {{{1
# Keydown handler {{{2
def handle_keydown(key, player):
    """Handles pygame.KEYDOWN events"""
    if key in {pg.K_ESCAPE,pg.K_q}:
        return False
    if key == pg.K_SPACE:
        if player.JumpCount>0 and time.time()-v.k<24/FPS:
            player.p.y = SPEED[1]
            player.JumpCount -= 1
    elif key == KEYS["left"]:
        player.p.x = -SPEED[0]
        player.Slipping = False
        player.VertFlip = True
    elif key == KEYS["right"]:
        player.p.x = SPEED[0]
        player.Slipping = False
        player.VertFlip = False
    return True

# Keyup handler {{{2
def handle_keyup(key, player):
    """Handles pygame.KEYUP events"""
    if key == KEYS["left"]:
        if player.p.x != SPEED[0]:
            player.Slipping = True
    elif key == KEYS["right"]:
        if player.p.x != -SPEED[0]:
            player.Slipping = True
    elif key == pg.K_r:
        return True
    return False

# data loader {{{2
def load_data():
    """Loads rectangular coordinates for the map"""
    map4 = pg.image.load('levels/map4.png').convert_alpha()
    player = pg.image.load('data/pixelperson.png').convert_alpha()
    with open('levels/map4.json', encoding='utf-8') as fp:
        data = load(fp)
        w = data['width']
        # The file stores the topleft values of all the collision boxes
        rectlist = [pg.Rect(32*(a%w),32*(a//w),32,32)
            for a,b in enumerate(data['layers'][0]['data']) if b != 0]
        return (map4, player, rectlist)

# Loading the data {{{1
STARTING_POSITION = [160, 128]
map_sprite, player_sprite, rects = load_data()
map_rect = map_sprite.get_rect()
v = Player(STARTING_POSITION, player_sprite)
SPEED = [5, -12]
running = True
pg.event.set_allowed((pg.QUIT, pg.KEYDOWN, pg.KEYUP))

# Game Loop {{{1
while running:
    # redraw {{{2
    Screen.fill((44,232,245))
    Screen.blit(map_sprite,(0,0),area = v.c)
    Screen.blit(pg.transform.flip(v.i,v.VertFlip,False), (v.r.x-v.c.x,v.r.y-v.c.y))
    pg.display.update()
    fpsClock.tick(FPS)

    # logic {{{2
    v.move(rects)
    v.c.x = min(max(0, v.c.x + (v.r.centerx - v.c.centerx) / 24), map_rect.w - Map.w)
    v.c.y = min(max(0, v.c.y + (v.r.centery - v.c.centery) / 24), map_rect.h - Map.h)
    v.c.clamp_ip(map_rect)

    # event handler {{{2
    for eve in pg.event.get():
        # variable changes: running, v.p.{x,y}, v.{tags}
        if eve.type == pg.QUIT:
            running = False
        elif eve.type == pg.KEYDOWN:
            running = handle_keydown(eve.key, v)
        elif eve.type == pg.KEYUP:
            if handle_keyup(eve.key, v):
                map_sprite, player_sprite, rects = load_data()
                map_rect = map_sprite.get_rect()
                v.JumpCount = 0
                v.i = player_sprite
                v.r.topleft = STARTING_POSITION
                v.VertFlip = False
    # }}}2
pg.quit()
