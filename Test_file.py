import pygame as pg
import sys
import os


FPS = 30


def terminate():
    pg.quit()
    sys.exit()


def load_image(name, colorkey=None):
    path = os.path.join('logo and icon', name)
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
    def __init__(self, right, top, width, height, image, *group):
        super().__init__(*group)
        self.image = pg.transform.scale(load_image(image), (width, height))
        self.rect = self.image.get_rect(right=right, top=top)

    def movement_1(self):
        print(self.rect)
        self.rect = self.rect.move(5, 0)

    def movement_2(self):
        pass


class Intro:
    def __init__(self, width, height, sprite_width, sprite_height):
        pg.init()
        self.size = self.width, self.height = width, height
        self.screen = pg.display.set_mode(self.size)
        self.clock = pg.time.Clock()
        self.all_sprites = pg.sprite.Group()
        self.sprite = AnimatedSprite(0, height // 2, sprite_width, sprite_height,
                                     'logo.png', self.all_sprites)
        self.main_cycle()

    def main_cycle(self):
        cur_frame = 0
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    terminate()
            self.clock.tick(FPS)
            self.screen.fill((255, 255, 255))
            if cur_frame > 59:
                self.all_sprites.update()
                self.all_sprites.draw(self.screen)
                if self.sprite.rect.centerx < self.width // 2:
                    self.sprite.movement_1()
                else:
                    # create_particles()
                    pass
            cur_frame += 1
            pg.display.flip()


intro = Intro(800, 700, 300, 50)