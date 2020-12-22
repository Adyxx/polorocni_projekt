import pygame
import random
import os
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
try:
    f = open("score.txt", "r")
except:
    f = open("score.txt", "w")
    f.write("0")
    f.close()
    f = open("score.txt", "r")

print()
score = 0
h_score = f.read()
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

    correct = random.randint(0,3)
    swap = ''
    x = 0
    def answer_on_button():
        if x > 3:
            swap = val[x]           
            val[x] = val[correct]
            val[correct] = swap
        return


    def is_it_right(a, f):
        f = open("score.txt", "r")
        global score
        global h_score
        if misto == 'opava' and val[a] == 'Opava':
            score +=1
            if (score > int(f.read())):
                f.close()
                f = open("score.txt", "w")
                f.write(str(score))
                f.close()
                h_score = score
        elif misto == 'ostrava' and val[a] == 'Ostrava':
            score +=1
            if (score > int(f.read())):
                f.close()
                f = open("score.txt", "w")
                f.write(str(score))
                f.close()
                h_score = score
        elif misto == 'paris' and val[a] == 'Paříž':
            score +=1
            if (score > int(f.read())):
                f.close()
                f = open("score.txt", "w")
                f.write(str(score))
                f.close()
                h_score = score
        elif misto == 'praha' and val[a] == 'Praha':
            score +=1
            if (score > int(f.read())):
                f.close()
                f = open("score.txt", "w")
                f.write(str(score))
                f.close()
                h_score = score
        else:
            score = 0

        return 


    # zjistí index správné odpovědi a nahradí jej pokud neexistuje tlačítko se správnou odpovědí

    if misto == 'opava':
        x = val.index('Opava')
        answer_on_button()
    elif misto == 'paris':
        x = val.index('Paříž')
        answer_on_button()
    elif misto == 'praha':
        x = val.index('Praha')
        answer_on_button()
    elif misto == 'ostrava':
        x = val.index('Ostrava')
        answer_on_button()



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


                    is_it_right(0, f)

                    running = False
                elif width/2 - 390 <= mouse[0] <= width/2 - 10 and height/2 + 147 <= mouse[1] <= height/2 + 217:


                    is_it_right(1, f)
                    
                    running = False
                elif width/2 + 10 <= mouse[0] <= width/2 + 390 and height/2 + 147 <= mouse[1] <= height/2 + 217:

                    is_it_right(2, f)

                    running = False
                elif width/2 + 10 <= mouse[0] <= width/2 + 390 and height/2 + 222 <= mouse[1] <= height/2 + 292:

                    is_it_right(3, f)

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
        score_text = pygame.font.SysFont('Comic Sans', 40)
        h_score_text = pygame.font.SysFont('Comic Sans', 40)
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

        text_score = score_text.render(f'Score: {score}', False, (0,0,0))
        scoreRect = text_score.get_rect()
        scoreRect.center = (width / 2 - 340, height / 2 - 250)

        h_text_score = h_score_text.render(f'High score: {h_score}', False, (0, 0, 0))
        h_scoreRect = h_text_score.get_rect()
        h_scoreRect.center = (width / 2 - 308, height / 2 - 280)
        ###################################################

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
            screen.blit(text_b1, textRect)
            screen.blit(text_b2, textRect2)
            screen.blit(text_b3, textRect3)
            screen.blit(text_b4, textRect4)
            screen.blit(text_score, scoreRect)
            screen.blit(h_text_score, h_scoreRect)
        pygame.display.flip()
        #kolik snímků za vteřinu, dosova by mohlo být tak 2, moc se to tam nehýbe :)
        clock.tick(45)

    pygame.mixer.quit()

f.close()