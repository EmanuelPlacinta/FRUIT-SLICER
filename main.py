#IMPORTS
import pygame
from sys import exit #Terminate the program
import random


#Constants
screen_width = 600
screen_height = 600
white = (255, 255, 255)
gravity = 0.2

#Variables
score = 0
strike = 0

#Fruits
pomme = pygame.Rect(300, 600 ,50 ,50)

#Design & Settings
pygame.init()
font = pygame.font.SysFont("Arial", 32)



#window settings
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("FRUIT SLICER - PYTHON VERSION") #title of the window
clock = pygame.time.Clock() # for the fps

#How the physic work
speed_y = 14
invert_speed_y = 15

#fonction for the display
def draw():
    window.fill((white))
    pygame.draw.rect(window, (0, 0, 0), pomme)
    score_surface = font.render(f"Score : {score}", True, (0, 0, 0))
    window.blit(score_surface, (10, 10))
    strike_surface = font.render(f"Strikes : {strike}", True, (0, 0, 0))
    window.blit(strike_surface,(10, 50))


#Game Loop
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Click the x button in window
            pygame.quit()
            exit()

    pomme.y += speed_y #speed for the apple
    speed_y += gravity #apply the gravity
    if pomme.y >= screen_height:
        pomme.y = 600
        speed_y = -15
        strike += 1
    
    if strike >= 3:
        pass

#recup input info
    mouse_position = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

#condition for touch the apple
    if mouse_click[0] and pomme.collidepoint(mouse_position) :
        score += 1

        pomme.x = random.randint(50, screen_width - 50)
        pomme.y = 600
        speed_y = -15


        
        

    draw()
    clock.tick(60) #60 FPS 
    pygame.display.update() 