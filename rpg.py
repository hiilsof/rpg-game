import pygame, sys
from sys import exit

#initializing pygame
pygame.init()

#creating display surface
#screen = pygame.display.set_mode((800,400), pygame.RESIZABLE)
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption('RPG')

#controlling the framerate
clock = pygame.time.Clock()

#game active or not
game_active = True


menu_page = pygame.image.load('graphics/welcome.png').convert_alpha()
pygame.surface

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(menu_page,(0,0))

    #update everything
    pygame.display.update()
    clock.tick(60)