import random
import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
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
    def __init__(self, x, y):
        super(Button, self).__init__()

        self.surf = pygame.image.load(f"foto/button_bg1.jpg").convert()

        self.rect = self.surf.get_rect(
            center=((SCREEN_WIDTH / 2 + x), (SCREEN_HEIGHT / 2 + y),
                    )
        )

    def yes_yes(self):
        self.surf = pygame.image.load(f"foto/button_bg3.jpg").convert()

    
    def no_no(self):
        self.surf = pygame.image.load(f"foto/button_bg2.jpg").convert()


while standing:
    running = True
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    cislo = 1
    # random rozhodnutí, jaké město se bude hádat
    while rozhodnuti == rozhodnuti1:
        rozhodnuti = random.randint(1,8)
    rozhodnuti1 = rozhodnuti

    pole = []
    val = ['Opava','Ostrava','Paříž','Praha','Tokyo','Moskva','New York','Kyoto']
    random.shuffle(pole)
    random.shuffle(val)
    misto = ''
    swap = ''
    correct = random.randint(0,3)
    x = 0

    def answer_on_button():
        if x > 3:
            swap = val[x]           
            val[x] = val[correct]
            val[correct] = swap
        return

    if rozhodnuti == 1:
        misto = "opava"
        x = val.index('Opava')
    elif rozhodnuti == 2:
        misto = "ostrava"
        x = val.index('Ostrava')
    elif rozhodnuti == 3:
        misto = "paris"
    elif rozhodnuti == 4:
        misto = "praha"
        x = val.index('Praha')
    elif rozhodnuti == 5:
        misto = "tokyo"
        x = val.index('Tokyo')
    elif rozhodnuti == 6:
        misto = "moskva"
        x = val.index('Moskva')
    elif rozhodnuti == 7:
        misto = "new_york"
        x = val.index('New York')
    elif rozhodnuti == 8:
        misto = "kyoto"
        x = val.index('Kyoto')
    answer_on_button()

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
            return True

        elif misto == 'ostrava' and val[a] == 'Ostrava':
            score +=1
            if (score > int(f.read())):
                f.close()
                f = open("score.txt", "w")
                f.write(str(score))
                f.close()
                h_score = score
            return True

        elif misto == 'paris' and val[a] == 'Paříž':
            score +=1
         
            if (score > int(f.read())):
                f.close()
                f = open("score.txt", "w")
                f.write(str(score))
                f.close()
                h_score = score
            return True

        elif misto == 'praha' and val[a] == 'Praha':
            score +=1
            if (score > int(f.read())):
                f.close()
                f = open("score.txt", "w")
                f.write(str(score))
                f.close()
                h_score = score
            return True

        elif misto == 'moskva' and val[a] == 'Moskva':
            score +=1
            if (score > int(f.read())):
                f.close()
                f = open("score.txt", "w")
                f.write(str(score))
                f.close()
                h_score = score
            return True

        elif misto == 'new_york' and val[a] == 'New York':
            score +=1
            if (score > int(f.read())):
                f.close()
                f = open("score.txt", "w")
                f.write(str(score))
                f.close()
                h_score = score
            return True

        elif misto == 'tokyo' and val[a] == 'Tokyo':
            score +=1
            if (score > int(f.read())):
                f.close()
                f = open("score.txt", "w")
                f.write(str(score))
                f.close()
                h_score = score
            return True
        elif misto == 'kyoto' and val[a] == 'Kyoto':
            score +=1
            if (score > int(f.read())):
                f.close()
                f = open("score.txt", "w")
                f.write(str(score))
                f.close()
                h_score = score
            return True        
        else:
            score = 0
            return False
        
    pygame.mixer.init()

    pygame.init()
    pygame.font.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    all_sprites = pygame.sprite.Group()

    foto = Foto()
    button = Button(-200, 257)
    button2 = Button(-200, 182)
    button3 = Button(200, 257)
    button4 = Button(200, 182)

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

                    if is_it_right(0,f) == True:
                        button.yes_yes()
                    else:
                        button.no_no()

                    running = False

                elif width/2 - 390 <= mouse[0] <= width/2 - 10 and height/2 + 147 <= mouse[1] <= height/2 + 217:

                    if is_it_right(1,f) == True:
                        button2.yes_yes()
                    else:
                        button2.no_no()

                    running = False

                elif width/2 + 10 <= mouse[0] <= width/2 + 390 and height/2 + 147 <= mouse[1] <= height/2 + 217:

                    if is_it_right(2,f) == True:
                        button4.yes_yes()
                    else:
                        button4.no_no()

                    running = False

                elif width/2 + 10 <= mouse[0] <= width/2 + 390 and height/2 + 222 <= mouse[1] <= height/2 + 292:

                    if is_it_right(3, f) == True:
                        button3.yes_yes()
                    else:
                        button3.no_no()

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
        scoreRect = (width / 2 - 390, height / 2 - 260)

        h_text_score = h_score_text.render(f'High score: {h_score}', False, (0, 0, 0))
        h_scoreRect = h_text_score.get_rect()
        h_scoreRect = (width / 2 - 390, height / 2 - 290)
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

        clock.tick(45)

    pygame.mixer.quit()

f.close()
