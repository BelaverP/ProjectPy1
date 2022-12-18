import pygame


class GameOver():

    def __init__(self, screen):

        self.screen = screen
        self.image = pygame.image.load('Images/GameOver.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottom = 200
        self.rect.centerx = 500


    def ouput(self):
        self.screen.blit(self.image, self.rect)