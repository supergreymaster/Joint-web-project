import pygame as pg
import sys
import os
from random import choice


def terminate():
    pg.quit()
    sys.exit()


def load_image(name, colorkey=None):
    path = os.path.join('data', name)
    if not os.path.isfile(path):
        terminate()
    image = pg.image.load(path)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class AnimatedSprite(pg.sprite.Sprite):
    def __init__(self, right, top, image, *group):
        super().__init__(*group)
        self.image = image
        self.rect = self.image.get_rect(right=right, top=top)

    def movement(self):
        self.rect = self.rect.move(5, 0)


def play_intro(width, height, sprite_width, sprite_height):
    pg.init()
    size = width, height = width, height
    screen = pg.display.set_mode(size)
    clock = pg.time.Clock()
    all_sprites = pg.sprite.Group()
    sprite_image = pg.transform.scale(load_image('logo.png'), (sprite_width, sprite_height))
    sprite = AnimatedSprite(0, height // 2, sprite_image, all_sprites)
    # self.sprite = AnimatedSprite(0, height // 2, sprite_width, sprite_height,
    #                              'logo.png', self.all_sprites)
    FPS = 60
    cur_frame = 0
    while True:
        print(cur_frame)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
        clock.tick(FPS)
        screen.fill((255, 255, 255))
        if cur_frame > 59:
            all_sprites.update()
            all_sprites.draw(screen)
            if sprite.rect.centerx < width // 2:
                sprite.movement()
        if cur_frame > 250:
            terminate()
        cur_frame += 1
        pg.display.flip()


# class Intro:
#     def __init__(self, width, height, sprite_width, sprite_height, particle_width, paticle_height):


play_intro(800, 700, 300, 50)


