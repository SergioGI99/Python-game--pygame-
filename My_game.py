import pygame, sys
from pygame.locals import *
from pygame import key

pygame.init()

#SCREEN
W,H = 1000,800
SCREEN = pygame.display.set_mode((W,H))
pygame.display.set_caption("Destruction")
window_icon=pygame.image.load("images/tarifa_icon.png")
pygame.display.set_icon(window_icon)
FPS = 60
CLOCK = pygame.time.Clock()

# MY_COLORS
WHITE = (255,255,255)
GREY = (135,135,135)
BLACK =(0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

MAIN_COLOR = (0,180,160)

# BACKGROUND
backgroud=pygame.image.load("images/street_Background.png")

# PLAYER
standing = pygame.image.load("images/player_standing_down.png")

walking_down = [pygame.image.load("images/player_standing_down.png"),
                pygame.image.load("images/player_step_down.png"),
                pygame.image.load("images/player_standing_down.png"),
                pygame.image.load("images/player_step_down_two.png")]

looking_left = pygame.image.load("images/player_standing_left.png")

looking_right = pygame.image.load("images/player_standing_right.png")

walking_up = [pygame.image.load("images/player_standing_up.png"),
              pygame.image.load("images/player_step_up.png"),
              pygame.image.load("images/player_standing_up.png"),
              pygame.image.load("images/player_step_up_two.png")]

# DIRECTION VARIABLES
up = False
down = True
left = False
right = False
run = False

y = 0
px = 50
py = 200
ancho = 40
p_speed = 5
steps = 0

def update_screen():
	
    global p_speed
    global steps
    global y
    pos = int(px), int(py)

    y_relative = y % backgroud.get_rect().height
    SCREEN.blit(backgroud, (0,y_relative - backgroud.get_rect().height))
    if y_relative < H:
        SCREEN.blit(backgroud,(0,y_relative))
    
    if steps + 1 >= 5:
        steps = 0

	# Movimiento a la izquierda
    if left:
        SCREEN.blit(looking_left, pos)

	# Movimiento a la derecha
    elif right:
        SCREEN.blit(looking_right, pos)

    elif up:
        SCREEN.blit(walking_up[steps // 1], pos)
        steps += 1
        y += p_speed

    elif down:
        SCREEN.blit(walking_down[steps // 1], pos)
        steps += 1
        y -= p_speed
    else:
       SCREEN.blit(standing, pos)

    p_speed = 5

execute = True

# LOOP
while execute:

    CLOCK.tick(18)

    for event in pygame.event.get():
        if event.type == QUIT:
            execute = False

    keys = pygame.key.get_pressed()

    # Tecla ShifL - correr
    if keys[pygame.K_LSHIFT]:
        p_speed = 10

    # Tecla A - Moviemiento a la izquierda
    if keys[pygame.K_a] and px > 5:
        px -= p_speed
        left = True
        right = False
        up = False
        down = False


	# Tecla D - Moviemiento a la derecha
    elif keys[pygame.K_d]:
        px += p_speed
        left = False
        right = True
        up = False
        down = False

    # Tecla W - Moviemiento arriba
    elif keys[pygame.K_w] and py > 5:
        py -= p_speed
        left = False
        right = False
        up = True
        down = False

    # Tecla S - Moviemiento abajo
    elif keys[pygame.K_s] and py < 770:
        py += p_speed
        left = False
        right = False
        up = False
        down = True

	# Personaje quieto
    else:
        left = False
        right = False
        up = False
        down = False
           

    pygame.display.update()
    update_screen()
    CLOCK.tick(FPS)