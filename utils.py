# External imports
import pygame, json, random, glob, ast, sys, os
from pygame.locals import *

class Renderer :
    """

    """
    def __init__(self, t_win_width, t_win_height, t_win_scale):
        self.frame_start    = 0
        self.frame_end      = 0

        # TODO: I feel like this should go somewhere else
        self.clock = pygame.time.Clock()

        self.raw_window     = pygame.Surface((t_win_width, t_win_height))
        self.display_window = pygame.display.set_mode(
            (t_win_width * t_win_scale, t_win_height * t_win_scale), 
            0, 32
        )

        self.entities = []

    """
        Render a new frame. Render all registered entites
        
        Called at the end of each game tick.
    """
    def render(self) :
        for e in self.entities :
            e.render(self.raw_window)
    
        scaled_window  = pygame.transform.scale(
            self.raw_window, 
            self.display_window.get_size()
        )

        self.display_window.blit(scaled_window, (0,0))
        pygame.display.update()

    def tick_clock(self) -> float :
        return self.clock.tick(60) / 1000.0

    def register_entity(self, t_e) :
        # TODO : Some type checking here so that this won't break
        self.entities.append(t_e)

    def clear_frame(self) :
        self.raw_window.fill((0,0,0))

# =============================================================================
# Homeless helper functions
# =============================================================================

def init_pygame() :
    pygame.init()

    # https://stackoverflow.com/questions/13356752/pygame-has-huge-delay-with-playing-sounds
    pygame.mixer.pre_init(44100, -16, 2, 256)
    pygame.mixer.init()
    pygame.init()


BASE_PATH = './'
def load_image(path):
    img = pygame.image.load(BASE_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img
