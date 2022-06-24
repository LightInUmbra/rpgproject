import pickle, sys, os
import pygame
import pygame_gui
from pygame_gui import *
from main import start_game
from main_menu import *
from pygame.locals import *

class LoadMenu(MainMenu):

    def __init__(self):
        super(LoadMenu, MainMenu, self).__init__()
        
        manager = MainMenu()