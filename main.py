import pygame

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
cislo = 1
class Foto(pygame.sprite.Sprite):
    def __init__(self):
        super(Foto, self).__init__();

        # 800x468 rozměry všech fotek
        self.surf = pygame.image.load(f"foto/opava{cislo}.jpg").convert()

        self.rect = self.surf.get_rect(
            center=((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2 - 90),
            )
        )
    # pohyb hráče
    def update(self, pressed_keys, cislo):
        self.surf = pygame.image.load(f"foto/opava{cislo}.jpg").convert()
        pygame.time.delay(200)



        ''' if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)

        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
    # objekt zůstane na obrazovce
        '''


pygame.mixer.init()

pygame.init()
pygame.font.init()



clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

score_count = 0
survival_time = 0

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

        if event.type == pygame.MOUSEBUTTONDOWN:
            cislo = cislo + 1
            if cislo == 3:
                cislo = 1
            foto.update(pressed_keys, cislo)










    screen.fill((10, 10, 10))

    surf = pygame.Surface((50, 50))

    rect = surf.get_rect()

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()

    clock.tick(45)

pygame.mixer.quit()