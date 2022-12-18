import pygame

class Floor():

    def __init__(self, screen):

        self.screen = screen
        self.image = pygame.image.load('Images/floor.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (2000, 72))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.bottom = 450
        self.rect.centerx = 1000

    def ouput(self):
        self.screen.blit(self.image, self.rect)
