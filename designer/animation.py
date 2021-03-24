import pygame
from designer.secondary_functions import Request, pprint

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


class Title_animation:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Загрузка')
        request = Request()
        size = request.get_request("size_display", True)

        pprint(size)

        screen = pygame.display.set_mode(size)

        clock = pygame.time.Clock()

        color_back = request.get_request("color_background", True)
        pprint(color_back)
        screen.fill(color_back)

        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if pygame.time.get_ticks() == 3000:
                running = False

Title_animation()
all_sprites = 0
