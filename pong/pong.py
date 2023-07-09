import pygame 
import time 
from Hard_Code_FTW import *

pygame.init()
pygame.display.set_caption("pong")


while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill(BLACK)
    pygame.display.update()


#game goes here




pygame.quit()
quit ()
