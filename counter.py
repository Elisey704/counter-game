import random
import pygame
import time

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([600,600])
runed = True
mainFant = pygame.font.Font('gameres/build.ttf',30)
buttonFont = pygame.font.Font('gameres/btn.ttf',10)
cursor_args = pygame.cursors.load_xbm('gameres/base.xbm', 'gameres/mask.xbm')
bg = pygame.image.load('gameres/bg.png')
icon = pygame.image.load('icon.ico')
pygame.display.set_caption('Counter')
sound = pygame.mixer.Sound('gameres/bg_sound.ogg')
sound.play(loops=-1)
pygame.display.set_icon(icon)
bg = pygame.transform.scale(bg,(600,600))
pygame.mouse.set_cursor(*cursor_args)
button_surface = pygame.Surface((150, 50))
buttonQuiteText = buttonFont.render('выход',True,(255,0,0))
coins = []
items = 0
plyer = pygame.Rect(300,300,25,25)
cd = 750
tCd = 0

with open('logs/errors.log','w') as f:
    f.write(pygame.get_error())

with open('logs/display_ww_info.json','w') as f:
    f.write(str(pygame.display.get_wm_info()))
with open('logs/displayinfo.log','w') as f:
    f.write(str(pygame.display.get_surface()))
    f.write(str(pygame.display.get_caption()))

def spawn():
    global  cd,tCd,coins
    current = pygame.time.get_ticks()
    if (current - tCd) > cd and len(coins) <= 10:
        coins.append(pygame.Rect(random.randint(0,590),random.randint(0,590),20,20))
        tCd = current
def collision():
    global coins,plyer,items,text_rect
    for c in coins:
        if plyer.colliderect(c):
            items += 1
            coins.remove(c)
        if c.colliderect(buttonQuiteText.get_rect(topleft=(0,550))):
            coins.remove(c)


def update():
    global plyer,coins,runed
    key = pygame.key.get_pressed()
    if key[pygame.K_d] and plyer.x < 575:
        plyer.x += 0.8
    if key[pygame.K_a] and plyer.x > 0:
        plyer.x -= 0.8
    if key[pygame.K_w] and plyer.y > 0:
        plyer.y -= 0.8
    if key[pygame.K_s] and plyer.y < 575:
        plyer.y += 0.8
    if key[pygame.K_F11] :
        pygame.display.toggle_fullscreen()

    if key[pygame.K_F12] :
        pygame.display.toggle_fullscreen()

    if buttonQuiteText.get_rect(topleft=(550,0)).collidepoint(pygame.mouse.get_pos()) and  pygame.mouse.get_pressed()[0]:
        runed = False
        print(coins)
        coins.clear()

    spawn()
    collision()


def draw():
    global items,bg
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen,(200,20,0),plyer)
    items_render = mainFant.render(f'coins:{items}', False, (80, 0, 250))
    screen.blit(items_render,(0,0))
    screen.blit(buttonQuiteText, (550, 0))
    for c in coins:
        pygame.draw.rect(screen,(255,0,0),c)
    pygame.display.flip()

while runed:
    draw()
    update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            runed = False