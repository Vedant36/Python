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
dim = pg.Rect(0, 0, 640, 360)
pg.init()
fpsClock = pg.time.Clock()
sdf = pg.display.set_mode(dim.size, 0, 32)
pg.display.set_caption('Platformer 1.2')

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
        self.c = dim.copy()
        self.c2= [self.c.x,self.c.y]

    # move {{{2
    def move(self, tiles):
        """Step through a single frame"""
        self.r.x += int(self.p.x)
        collisions = self.r.collidelistall(tiles)
        for tile in collisions:
            if self.p.x > 0:
                self.r.right = tiles[tile].left
            elif self.p.x < 0:
                self.r.left = tiles[tile].right

        self.p.y += 1
        self.r.y += int(self.p.y)
        collisions = self.r.collidelistall(tiles)
        self.l[1] = True
        for tile in collisions:
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

        self.InAir = all(self.l)
        self.l[0] = self.l[1]
        if self.r.clamp(map_rect) != self.r:
            self.r.clamp_ip(map_rect)
            self.p.y += 1

# Helper functions {{{1
# Keydown handler {{{2
def handle_keydown(key, v):
    """Handles pygame.KEYDOWN events"""
    running = True
    match key:
        case pg.K_ESCAPE|pg.K_q:
            running = False
        case pg.K_SPACE:
            if v.JumpCount>0 and time.time()-v.k<24/FPS:
                v.p.y = -12
                v.JumpCount -= 1
        case pg.K_h:
            v.p.x = -SPEED
            v.Slipping = False
            v.VertFlip = True
        case pg.K_l:
            v.p.x = SPEED
            v.Slipping = False
            v.VertFlip = False
    return running

# Keyup handler {{{2
def handle_keyup(key, v):
    """Handles pygame.KEYUP events"""
    reload = False
    match key:
        case pg.K_h:
            if v.p.x != SPEED:
                v.Slipping = True
        case pg.K_l:
            if v.p.x != -SPEED:
                v.Slipping = True
        case pg.K_r:
            reload = True
    return reload

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
SPEED = 4
running = True
pg.event.set_allowed((pg.QUIT, pg.KEYDOWN, pg.KEYUP))

# Game Loop {{{1
while running:
    # redraw {{{2
    sdf.fill((44,232,245))
    sdf.blit(map_sprite,(0,0),area = v.c)
    sdf.blit(pg.transform.flip(v.i,v.VertFlip,False), (v.r.x-v.c.x,v.r.y-v.c.y))
    pg.display.update()
    fpsClock.tick(FPS)

    # logic {{{2
    v.move(rects)
    v.c2[0] = min((v.c2[0] + max(0, v.r.centerx - v.c.centerx) / 24), map_rect.w - dim.w)
    v.c2[1] = min((v.c2[1] + max(0, v.r.centery - v.c.centery) / 24), map_rect.h - dim.h)
    v.c.topleft = int(v.c2[0]),int(v.c2[1])
    v.c.clamp_ip(map_rect)

    # event handler {{{2
    for eve in pg.event.get():
        # variable changes: running, v.p.{x,y}, v.{tags}
        match eve.type:
            case pg.QUIT:
                running = False
            case pg.KEYDOWN:
                running = handle_keydown(eve.key, v)
            case pg.KEYUP:
                if handle_keyup(eve.key, v):
                    map_sprite, player_sprite, rects = load_data()
                    map_rect = map_sprite.get_rect()
                    v.JumpCount = 0
                    v.i = player_sprite
                    v.r.topleft = STARTING_POSITION
                    v.VertFlip = False
    # }}}2
pg.quit()
