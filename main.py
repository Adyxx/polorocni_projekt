import pygame
import random
import time


from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Foto(pygame.sprite.Sprite):
    def __init__(self):
        super(Foto, self).__init__()

        # 800x468 rozměry všech fotek
        self.surf = pygame.image.load("foto/opava1.jpg").convert()

        self.rect = self.surf.get_rect(
            center=((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2 - 90),
            )
        )
    # pohyb hráče
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)

        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
    # objekt zůstane na obrazovce
        '''
        if self.rect.left < 0:
            self.rect.left =0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top =0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
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
    for event in pygame.event.get():
        if event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False



    pressed_keys = pygame.key.get_pressed()

    foto.update(pressed_keys)



    screen.fill((10, 10, 10))

    surf = pygame.Surface((50, 50))

    rect = surf.get_rect()

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()

clock.tick(45)

pygame.mixer.quit()