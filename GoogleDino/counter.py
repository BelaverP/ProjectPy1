import pygame


class Counter():

    def __init__(self, screen):

        self.screen = screen
        self.font = pygame.font.Font(None, 40)
        self.count = 0
        self.text = self.font.render(str(self.count), True, "black")

    def ouput(self):
        self.screen.blit(self.text, (150, 50))
