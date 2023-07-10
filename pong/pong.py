import pygame 
import time 
from Hard_Code_FTW import *


pygame.init()
pygame.display.set_caption("pong")

font = pygame.font.SysFont(None, 25)

#first message
def message_to_screen (msg,color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [display_width/2.5,display_height/2])


while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #game screen
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, [0,display_height/1.25,display_width,ball_size])
    pygame.display.update()
    
    
    #test button
    if event.type == pygame.KEYDOWN:
        if  event.key == pygame.K_RIGHT:
            message_to_screen('test', WHITE)
            pygame.display.update()



pygame.quit()
quit ()
