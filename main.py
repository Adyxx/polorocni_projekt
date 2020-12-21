import pygame
import random
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
cislo = 1
# random rozhodnutí, jaké město se bude hádat
rozhodnuti = random.randint(1,4)
misto = ""
if rozhodnuti == 1:
    misto = "opava"
elif rozhodnuti == 2:
    misto = "ostrava"
elif rozhodnuti == 3:
    misto = "paris"
elif rozhodnuti == 4:
    misto = "praha"

class Foto(pygame.sprite.Sprite):
    def __init__(self):
        super(Foto, self).__init__()

        # 800x468 rozměry všech fotek
        self.surf = pygame.image.load(f"foto/{misto}{cislo}.jpg").convert()

        self.rect = self.surf.get_rect(
            center=((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2 - 90),
            )
        )
    # znovunačítání obrázků při kliknutí
    def update(self, pressed_keys, cislo):
        self.surf = pygame.image.load(f"foto/{misto}{cislo}.jpg").convert()
        pygame.time.delay(200)



pygame.mixer.init()

pygame.init()
pygame.font.init()



clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

foto = Foto()

all_sprites = pygame.sprite.Group()
all_sprites.add(foto)



running = True

while running:
    pressed_keys = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False
        # při kliknutí update foto
        if event.type == pygame.MOUSEBUTTONDOWN:
            cislo = cislo + 1
            if cislo == 5:
                cislo = 1
            foto.update(pressed_keys, cislo)

    screen.fill((10, 10, 10))

    surf = pygame.Surface((50, 50))

    rect = surf.get_rect()

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()
    #kolik snímků za vteřinu, dosova by mohlo být tak 2, moc se to tam nehýbe :)
    clock.tick(45)

pygame.mixer.quit()