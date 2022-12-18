import pygame


class Record():

    def __init__(self, screen):

        self.screen = screen
        self.font = pygame.font.Font(None, 40)
        self.count = 0
        self.text = self.font.render("Record: " + str(self.count), True, "light green")

    def ouput(self):
        self.screen.blit(self.text, (800, 50))
