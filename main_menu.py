import pickle, sys, os
import pygame
import pygame_gui
import main
from pygame_gui import *
from main import start_game
from pygame.locals import *

class MainMenu():

    def __init__(self):
        super(MainMenu, self).__init__()
        mainClock = pygame.time.Clock()
        pygame.display.set_caption('RPG')
        screen =  pygame.display.set_mode((720, 480))

        font = pygame.font.SysFont(None, 32)

        def draw_text(self, text, font, color, surface, x, y):
            textobject = font.render(text, 1, color)
            textbox = textobject.get_rect()
            textbox.topleft = (x, y)
            surface.blit(textobject, textbox)

        manager = UIManager((800, 600), str('UIButton.json'))
        play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((70, 275), (157, 86)),
                                                text='', manager=manager, object_id=f"#button")

        load_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 275), (157, 86)),
                                                text='', manager=manager, object_id=f"#loadbutton")

        quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((530, 275), (157, 86)),
                                                text='', manager=manager, object_id=f"#quitbutton")

        clock = pygame.time.Clock()
        

        def main_menu(self):
            while True:
                time_delta = clock.tick(60)/1000.0
                screen.fill((0, 0, 0))
                draw_text(self, 'Main Menu', font, (255, 255, 255), screen, 20, 20)


                events = pygame.event.get()
                for event in events:
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                    if event.type == pygame.USEREVENT:
                        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                            if event.ui_element == play_button:
                                start_game()
                    if event.type == pygame.USEREVENT:
                        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                            if event.ui_element == load_button:
                                start_game()
                    if event.type == pygame.USEREVENT:
                        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                            if event.ui_element == quit_button:
                                sys.exit()
                    manager.process_events(event)
                manager.update(time_delta)
                manager.draw_ui(screen)
                pygame.display.update()
                mainClock.tick(60)


        main_menu(self)