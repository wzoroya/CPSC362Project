import pygame
import button

from pygame.locals import *
from pygame import mixer

pygame.init()

SCREEN_SIZE = (800, 400)
screen_event = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Event")

#Draw text
def draw_text(text, font, color, x, y):
    title = font.render(text, True, color)
    screen_event.blit(title, (x, y))

#Font
font_1 = pygame.font.SysFont("cambria", 40)
font_2 = pygame.font.SysFont("cambria", 20)

#Color
white = (255, 255, 255)

options_image = pygame.image.load("images/options.png").convert_alpha()


options_button = button.Button(options_image, 340, 70)

#next_step = False
event_state = False #"event"

run = True
while run:

    screen_event.fill((0, 0, 0))

    if event_state == True:
        #check main
        #if event_state == "event":
        #if options_button.draw(screen_event):
            event_state = "options"
    #else:
        #draw text
        draw_text("Event", font_1, white, 80, 70)
        draw_text("info:", font_2, white, 80, 125)


    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            #press RETURN to go to the next step
            if event.key == pygame.K_SPACE:
                next_step = True

    #update display
    pygame.display.update()

#quit game
pygame.quit()
