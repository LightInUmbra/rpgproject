import pickle, sys, os
import pygame
import pygame_gui
from pygame_gui import *
from pygame.locals import *

class GameMenu():

    def __init__(self):
        super(GameMenu, self).__init__()
        mainClock = pygame.time.Clock()
        
        screen =  pygame.display.set_mode((720, 480))
        font = pygame.font.SysFont(None, 32)

        def draw_text(self, text, font, color, surface, x, y):
            textobject = font.render(text, 1, color)
            textbox = textobject.get_rect()
            textbox.topleft = (x, y)
            surface.blit(textobject, textbox)

        clock = pygame.time.Clock()

        def game_menu(self):
            while True:
                time_delta = clock.tick(60)/1000.0
                screen.fill((0, 0, 0))
                draw_text(self, 'Game Menu', font, (255, 255, 255), screen, 20, 20)


                events = pygame.event.get()
                for event in events:
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_z:
                            pass           
                pygame.display.update()
                mainClock.tick(60)
            
        game_menu(self)
