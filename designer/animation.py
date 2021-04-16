import pygame
from designer.secondary_functions import Request, pprint


class Title_animation:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Загрузка')
        request = Request()
        size = request.get_request("size_display", tup=True)

        print(size)

        screen = pygame.display.set_mode(size)

        clock = pygame.time.Clock()

        color_back = request.get_request("background", color=True)
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
