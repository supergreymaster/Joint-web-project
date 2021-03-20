import pygame
from designer.secondary_functions import Request


class Title_animation:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Загрузка')
        size = Request.get_request("size_display", tup=True)
        screen = pygame.display.set_mode(size)

        clock = pygame.time.Clock()

        screen.fill(Request.get_request("color_background", tup=True))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

Title_animation()
