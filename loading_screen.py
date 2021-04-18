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
        print(self.rect)
        self.rect = self.rect.move(5, 0)


class Particle(pg.sprite.Sprite):
    def __init__(self, center_x, center_y, image, dx, dy, *group):
        super().__init__(*group)
        self.image = image
        self.rect = self.image.get_rect(centerx=center_x, centery=center_y)
        self.dx = dx
        self.dy = dy

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        self.dy += 1
        self.dx *= 1.2


class Intro:
    def __init__(self, width, height, sprite_width, sprite_height, particle_width, paticle_height):
        pg.init()
        self.size = self.width, self.height = width, height
        self.screen = pg.display.set_mode(self.size)
        self.clock = pg.time.Clock()
        self.all_sprites = pg.sprite.Group()
        self.sprite_image = pg.transform.scale(load_image('logo.png'), (sprite_width, sprite_height))
        self.particle_image = pg.transform.scale(load_image('star.jpg', -1), (particle_width, paticle_height))
        self.sprite = AnimatedSprite(0, height // 2, self.sprite_image, self.all_sprites)
        # self.sprite = AnimatedSprite(0, height // 2, sprite_width, sprite_height,
        #                              'logo.png', self.all_sprites)
        self.FPS = 30
        self.main_cycle()

    def create_particles(self):
        [Particle(self.width // 2, self.height // 2, self.particle_image, choice(range(-5, 5)),
                  choice(range(4, 10)), self.all_sprites) for i in range(20)]

    def main_cycle(self):
        f = 0
        cur_frame = 0
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    terminate()
            self.clock.tick(self.FPS)
            self.screen.fill((255, 255, 255))
            if cur_frame > 59:
                self.all_sprites.update()
                self.all_sprites.draw(self.screen)
                if self.sprite.rect.centerx < self.width // 2:
                    self.sprite.movement()
                else:
                    if not f:
                        self.create_particles()
                        f = 1
            cur_frame += 1
            pg.display.flip()


intro = Intro(800, 700, 300, 50, 50, 50)