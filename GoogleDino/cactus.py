import pygame
import random

class Сactus():

    def __init__(self, screen):

        self.screen = screen
        image1 = pygame.image.load('Images/cac2.png').convert_alpha()
        image2 = pygame.image.load('Images/cactus.png').convert_alpha()
        image3 = pygame.image.load('Images/cac1.png').convert_alpha()
        image4 = pygame.image.load('Images/cac3.png').convert_alpha()
        image5 = pygame.image.load('Images/cac4.png').convert_alpha()
        image = [image1, image2, image3, image4, image5]
        self.image = image[random.randrange(0, 5)]
        a = random.randrange(170, 260)
        self.image = pygame.transform.scale(self.image, (a, a))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.bottom = 400 + a / 20
        self.rect.centerx = 1500
        self.mask = pygame.mask.from_surface(self.image)

    def ouput(self):
        self.screen.blit(self.image, self.rect)
