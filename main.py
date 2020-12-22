import pygame
import random
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    RLEACCEL
)
standing = True

rozhodnuti1 = 0
rozhodnuti = 0
class Foto(pygame.sprite.Sprite):
    def __init__(self):
        super(Foto, self).__init__()

        # 800x468 rozměry všech fotek
        self.surf = pygame.image.load(f"foto/{misto}{cislo}.jpg").convert()

        self.rect = self.surf.get_rect(
            center=((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2 - 90),
                    )
        )

    # znovunačítání obrázků při kliknutí
    def update(self, pressed_keys, cislo):
        self.surf = pygame.image.load(f"foto/{misto}{cislo}.jpg").convert()
        pygame.time.delay(200)


class Button(pygame.sprite.Sprite):
    def __init__(self):
        super(Button, self).__init__()

        self.surf = pygame.image.load(f"foto/button_bg.jpg").convert()

        self.rect = self.surf.get_rect(
            center=((SCREEN_WIDTH / 2 - 200), (SCREEN_HEIGHT / 2 + 257),
                    )
        )


class Button2(pygame.sprite.Sprite):
    def __init__(self):
        super(Button2, self).__init__()

        self.surf = pygame.image.load(f"foto/button_bg.jpg").convert()

        self.rect = self.surf.get_rect(
            center=((SCREEN_WIDTH / 2 - 200), (SCREEN_HEIGHT / 2 + 182),
                    )
        )


class Button3(pygame.sprite.Sprite):
    def __init__(self):
        super(Button3, self).__init__()

        self.surf = pygame.image.load(f"foto/button_bg.jpg").convert()

        self.rect = self.surf.get_rect(
            center=((SCREEN_WIDTH / 2 + 200), (SCREEN_HEIGHT / 2 + 257),
                    )
        )


class Button4(pygame.sprite.Sprite):
    def __init__(self):
        super(Button4, self).__init__()

        self.surf = pygame.image.load(f"foto/button_bg.jpg").convert()

        self.rect = self.surf.get_rect(
            center=((SCREEN_WIDTH / 2 + 200), (SCREEN_HEIGHT / 2 + 182),
                    )
        )
while standing:
    running = True
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    cislo = 1
    # random rozhodnutí, jaké město se bude hádat
    while rozhodnuti == rozhodnuti1:
        rozhodnuti = random.randint(1,4)
    rozhodnuti1 = rozhodnuti
    misto = ""
    if rozhodnuti == 1:
        misto = "opava"
    elif rozhodnuti == 2:
        misto = "ostrava"
    elif rozhodnuti == 3:
        misto = "paris"
    elif rozhodnuti == 4:
        misto = "praha"

    
    pole = [0,1,2,3,4,5]
    val = [0,0,0,0,0,0]
    random.shuffle(pole)
    word = ''
    correct = random.randint(0,3)
    
    for i in pole:
        if i == 0:
            word = 'Praha'
        elif i == 1:
            word = 'Paříž'
        elif i == 2:
            word = 'Ostrava'
        elif i == 3:
            word = 'Opava'
        elif i == 4:
            word = 'Kyoto'
        else:
            word = 'New York'
        val[i] = word
    random.shuffle(val)
    
    x = 0
    # zjistí index správné odpovědi
    if misto == 'opava':
        x = val.index('Opava')
        print(x)
    elif misto == 'paris':
        x = val.index('Paříž')
        print(x)
    elif misto == 'praha':
        x = val.index('Praha')
        print(x)
    elif misto == 'ostrava':
        x = val.index('Ostrava')
        print(x)



    pygame.mixer.init()

    pygame.init()
    pygame.font.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    all_sprites = pygame.sprite.Group()

    foto = Foto()
    button = Button()
    button2 = Button2()
    button3 = Button3()
    button4 = Button4()
    all_sprites.add(button)
    all_sprites.add(button2)
    all_sprites.add(button3)
    all_sprites.add(button4)

    all_sprites.add(foto)


    while running:
        pressed_keys = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    standing = False
                    running = False

            elif event.type == QUIT:
                standing = False
                running = False
            # při kliknutí update foto
            if event.type == pygame.MOUSEBUTTONDOWN:
                if width/2 - 390 <= mouse[0] <= width/2 - 10 and height/2 + 222 <= mouse[1] <= height/2 + 292:
                    print('hey')
                    running = False
                elif width/2 - 390 <= mouse[0] <= width/2 - 10 and height/2 + 147 <= mouse[1] <= height/2 + 217:
                    print('heyo')
                    running = False
                elif width/2 + 10 <= mouse[0] <= width/2 + 390 and height/2 + 222 <= mouse[1] <= height/2 + 292:
                    print('heya')
                    running = False
                elif width/2 + 10 <= mouse[0] <= width/2 + 390 and height/2 + 147 <= mouse[1] <= height/2 + 217:
                    print('heye')
                    running = False
                else:
                    cislo = cislo + 1
                    if cislo == 5:
                        cislo = 1
                foto.update(pressed_keys, cislo)

        screen.fill((0, 0, 0))

        surf = pygame.Surface((50, 50))

        rect = surf.get_rect()
        width = screen.get_width()
        height = screen.get_height()
        mouse = pygame.mouse.get_pos()

        ###################################################
        text = pygame.font.SysFont('Arial Black', 50)

        text_b1 = text.render(f'{val[0]}', True, (255, 255, 255))
        textRect = text_b1.get_rect()
        textRect.center = (width / 2 - 200, height / 2 + 252)

        text_b2 = text.render(f'{val[1]}', True, (255, 255, 255))
        textRect2 = text_b2.get_rect()
        textRect2.center = (width / 2 - 200, height / 2 + 177)

        text_b3 = text.render(f'{val[2]}', True, (255, 255, 255))
        textRect3 = text_b3.get_rect()
        textRect3.center = (width / 2 + 200, height / 2 + 177)

        text_b4 = text.render(f'{val[3]}', True, (255, 255, 255))
        textRect4 = text_b4.get_rect()
        textRect4.center = (width / 2 + 200, height / 2 + 252)
        ###################################################

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
            screen.blit(text_b1, textRect)
            screen.blit(text_b2, textRect2)
            screen.blit(text_b3, textRect3)
            screen.blit(text_b4, textRect4)

        pygame.display.flip()
        #kolik snímků za vteřinu, dosova by mohlo být tak 2, moc se to tam nehýbe :)
        clock.tick(45)

    pygame.mixer.quit()