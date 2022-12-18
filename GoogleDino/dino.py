import pygame


class Dino():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('Images/dino.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.bottom = 400
        self.rect.left = 200
        self.mask = pygame.mask.from_surface(self.image)

    def ouput(self):
        self.screen.blit(self.image, self.rect)
