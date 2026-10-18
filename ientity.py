# External imports
import pygame

# Internal imports
from animations import *

class IEntity :
    def __init__(self, t_name : str):
        self.name = t_name

        self.speed_pps  = 0.0
        self.position   = pygame.Vector2(0.0, 0.0)
        self.velocity   = pygame.Vector2(0.0, 0.0)

        self.animation_manager  = EntityAnimationManager(t_name)

    def render(self, t_raw_window) :
        t_raw_window.blit(
            self.animation_manager.get_curr_frame(),
            (round(self.position.x), round(self.position.y))
        )

    # ATTENTION : there's an implication that children must call this
    def update(self, t_dt_s: float) :
        self.animation_manager.update(t_dt_s)