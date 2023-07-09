import pygame 
import time 
from Hard_Code_FTW import *

pygame.init()
pygame.display.set_caption("pong")


while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #game screen
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, [0,display_height/1.25,display_width,ball_size])
    pygame.display.update()


#game goes here



pygame.quit()
quit ()
