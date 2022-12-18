import pygame
import sys
import random
from dino import Dino
from cactus import Сactus
from counter import Counter
from game_over import GameOver
from record import Record
from floor import Floor
from cloud import Cloud


FPS = 200

def run():
    pygame.init()
    screen = pygame.display.set_mode((1000, 500))
    pygame.display.set_caption("Google Dino")
    bg_color = 'white'
    dino = Dino(screen)
    cactus = Сactus(screen)
    counter = Counter(screen)
    game_over = GameOver(screen)
    record = Record(screen)
    clock = pygame.time.Clock()
    air = 0
    v = 0
    tick = 0
    speed = 5
    a = 0.0003
    g = 0.1
    death = 0
    floor = Floor(screen)
    cloud = Cloud(screen)
    sound_up = pygame.mixer.Sound('Sounds/Step.mp3')
    sound_death = pygame.mixer.Sound('Sounds/Death.mp3')
    ds = 0

    while True:

        clock.tick(FPS)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if g != 0:
                    if air == 0:
                        if event.key == pygame.K_UP:
                            sound_up.play()
                            v = 7
                            air = 1
                            dino.image = pygame.image.load('images/dino.png')
                            dino.mask = pygame.mask.from_surface(dino.image)
                    if air == 1:
                        if event.key == pygame.K_DOWN:
                            v = - 7
                else:
                    if event.key == pygame.K_SPACE:
                        speed = 5
                        g = 0.1
                        dino.rect.bottom = 500
                        cactus.rect.left = 1500
                        counter.count = 0
                        a = 0.0003
                        dino.image = pygame.image.load('images/dino.png')
                        dino.mask = pygame.mask.from_surface(dino.image)
                        death = 0
                        ds = 0




        dino.rect.centery -= v
        if air == 1:
            v -= g

        if dino.rect.bottom - v > 400:
            dino.rect.bottom = 400
            v = 0
            air = 0


        if death == 0:
            tick += 1

        if air == 0:
            if tick == 15:
                dino.image = pygame.image.load('images/dino2.png')
                dino.mask = pygame.mask.from_surface(dino.image)
            if tick == 30:
                dino.image = pygame.image.load('images/dino1.png')
                dino.mask = pygame.mask.from_surface(dino.image)

        if tick == 30:
            tick = 0

        cactus.rect.centerx -= speed
        floor.rect.centerx -= speed
        cloud.rect.centerx -= speed * 0.6

        if cactus.rect.centerx < -200:
            cactus = Сactus(screen)
            cactus.rect.centerx = speed * random.randrange(200, 350)

        if floor.rect.centerx < 0:
            floor.rect.centerx += 1000

        if cloud.rect.centerx < 0:
            cloud.rect.centerx += 1000


        if g != 0:
            counter.count += 1
            if record.count < counter.count:
                record.count += 1
        counter.text = counter.font.render(str(counter.count // 10), True, (80, 80, 80))
        record.text = counter.font.render("Record: " + str(record.count // 10), True, (80, 80, 80))

        offset = (cactus.rect.left - dino.rect.left - speed, cactus.rect.top - dino.rect.top)
        if dino.mask.overlap_area(cactus.mask, offset) > 0:
            offset = (cactus.rect.left - dino.rect.left, cactus.rect.top - dino.rect.top)
            while not(dino.mask.overlap_area(cactus.mask, offset) > 0):
                offset = (cactus.rect.left - dino.rect.left, cactus.rect.top - dino.rect.top)
                cactus.rect.left -= 1
                floor.rect.right -= 1
            speed = 0
            a = 0
            g = 0
            v = 0
            dino.image = pygame.image.load('images/dino_death.png')
            dino.mask = pygame.mask.from_surface(dino.image)
            death = 1
            if ds == 0:
                sound_death.play()
                ds = 1
        speed += a




        screen.fill(bg_color)
        floor.ouput()
        cloud.ouput()
        dino.ouput()
        cactus.ouput()
        counter.ouput()
        record.ouput()
        if death == 1:
            game_over.ouput()
        pygame.display.flip()


run()

