import pygame
from sys import exit #Terminate the program
from constants import *

#Setup pygame for us
pygame.init()
window = pygame.display.set_mode((screen_width, scree_height))
pygame.display.set_caption("FRUIT SLICER - PYTHON VERSION") #Title of the window
clock = pygame.time.Clock() # For the fps

#Game Loop
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Click the x button in window
            pygame.quit()
            exit()
    
    pygame.display.update()
    clock.tick(60) #60 FPS 