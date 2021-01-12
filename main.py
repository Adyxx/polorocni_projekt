import random
import pygame
import json
import unidecode
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

standing = True
json_test = 0
h_score = 0
try:
    with open('score.json') as json_file:
        h_score = json.load(json_file)
except:
    with open('score.json', 'w') as json_file:
        json.dump(json_test, json_file)

score = 0

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

    def change_color(self, num):
        if num == 1:
            self.surf = pygame.image.load(f"foto/button_bg3.jpg").convert()
        else:
            self.surf = pygame.image.load(f"foto/button_bg2.jpg").convert()

def high(score, h_score):
    if (score > int(h_score)):
        with open('score.json', 'w') as json_file:
            json.dump(str(score), json_file)
        with open('score.json') as json_file:
            h_score = json.load(json_file)
    return h_score

while standing:
    running = True
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    cislo = 1

    rozhodnuti = random.randint(0,7)

    val = ['Opava','Ostrava','Paříž','Praha','Tokyo','Moskva','New York','Kyoto']
    random.shuffle(val)
    misto = ''
    correct = random.randint(0,3)
    x = 0

    def answer_on_button():
        if x > 3:           
            val[x], val[correct] = val[correct], val[x]
        return

    for i in range(8):
        if rozhodnuti == i:
            misto = unidecode.unidecode(val[i].lower().replace(" ", "_"))
            x = val.index(val[i])
            answer_on_button()

    def is_it_right(a, score, h_score):
        if misto != unidecode.unidecode(val[a].lower().replace(" ", "_")):
            score = 0
        else:
            score +=1
        return score
   
    def control(wi, wid, he, hei, l, score, h_score, q, running):
        if width / 2 + wi <= mouse[0] <= width / 2 + wid and height / 2 + he <= mouse[1] <= height / 2 + hei:
            score = is_it_right(l, score, h_score)
            h_score = high(score, h_score)
            if is_it_right(l, score, h_score) > 0:
                q.change_color(1)
                running = False
            else:
                q.change_color(0)
                running = False
        return score, running, h_score

    pygame.init()
    pygame.font.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    all_sprites = pygame.sprite.Group()

    foto = Foto()

    buttons = [(-200, 257), (-200, 182), (200, 257), (200, 182)]
    button1 = Button(-200, 257)
    button2 = Button(-200, 182)
    button3 = Button(200, 257)
    button4 = Button(200, 182)

    all_sprites.add(button1)
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

            if event.type == pygame.MOUSEBUTTONDOWN:
                s = score
                q = button1
                score, running, h_score = control(-390, -10, 222, 292, 0, score, h_score, q, running)
                q = button2
                score, running, h_score = control(-390, -10, 147, 217, 1, score, h_score, q, running)
                q = button3
                score, running, h_score = control(10, 390, 222, 292, 3, score, h_score, q, running)
                q = button4
                score, running, h_score = control(10, 390, 147, 217, 2, score, h_score, q, running)

                if s == score:
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
