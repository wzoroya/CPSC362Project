import pygame, sys
import button
from pygame.locals import *
from pygame import mixer
import data
from map import Map

pygame.init()
FINAL_ENCOUNTER = 11
SCREEN_SIZE = (800, 400)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Main Menu")
clock = pygame.time.Clock()

#Background image
background_image = pygame.image.load("images/background.png").convert_alpha()

#Draw background
def draw_background():
    screen.blit(background_image, (0, 0))

#Draw text
def draw_text(text, font, color, x, y):
    title = font.render(text, True, color)
    screen.blit(title, (x, y))

def map():
    map = Map(0, FINAL_ENCOUNTER, screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill('black')
        map.run()

        pygame.display.update()
        clock.tick(60)

#Font
font_1 = pygame.font.SysFont("cambria", 65)
font_2 = pygame.font.SysFont("cambria", 25)

#Color
white = (255, 255, 255)

#Button images
start_image = pygame.image.load("images/start.png").convert_alpha()
settings_image = pygame.image.load("images/settings.png").convert_alpha()
quit_image = pygame.image.load("images/quit.png").convert_alpha()
info_image = pygame.image.load("images/info.png").convert_alpha()
audio_image = pygame.image.load('images/audio.png').convert_alpha()
back1_image = pygame.image.load('images/back1.png').convert_alpha()
back2_image = pygame.image.load('images/back2.png').convert_alpha()

#Button instances
start_button = button.Button(start_image, 340, 70)
settings_button = button.Button(settings_image, 340, 165)
quit_button = button.Button(quit_image, 340, 260)
info_button = button.Button(info_image, 380, 60)
audio_button = button.Button(audio_image, 380, 160)
back1_button = button.Button(back1_image, 345, 260)
back2_button = button.Button(back2_image, 345, 260)

mixer.init()
mixer.music.load('music/bg_music.mp3')
pygame.mixer.music.play(-1)

#Variables
next_step = False
menu_state = "main"

#Game loop
run = True
while run:

    #draw background
    draw_background()

    if next_step == True:
        #check main
        if menu_state == "main":
            if start_button.draw(screen):
                map()    #connect to map
            if settings_button.draw(screen):
                menu_state = "settings"
            if quit_button.draw(screen):
                run = False

        #check settings
        if menu_state == "settings":
            if info_button.draw(screen):
                menu_state = "info"
            if audio_button.draw(screen):
                menu_state = "audio"
            if back1_button.draw(screen):
                menu_state = "main"
        
        if menu_state == "info":
            draw_text("Press RETURN To Fullscreen", font_2, white, 260, 100)
            draw_text("Press ESC To Window", font_2, white, 280, 180)
            if back1_button.draw(screen):
                menu_state = "settings"

        if menu_state == "audio":
            if back1_button.draw(screen):
                menu_state = "settings"
     
    else:
        #draw text
        draw_text("LONE ADVENTURER", font_1, white, 85, 100)
        draw_text("Press SPACE To MAIN MENU", font_2, white, 230, 250)


    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            #press RETURN to go to the next step
            if event.key == pygame.K_SPACE:
                next_step = True

            #press SPACE to fullscreen
            elif event.key == pygame.K_RETURN:
                screen = pygame.display.set_mode(SCREEN_SIZE, pygame.FULLSCREEN|HWSURFACE)
                pygame.display.flip()
                
            #press ESC to window
            elif event.key == pygame.K_ESCAPE:
                screen = pygame.display.set_mode(SCREEN_SIZE)

    #update display
    pygame.display.update()

#quit game
pygame.quit()

























