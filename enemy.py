# External imports
import pygame

# Internal imports
from utils import load_image
from ientity import IEntity

"""

"""
class Enemy(IEntity) :
    """

    """
    def __init__(self, t_name : str, t_x : float, t_y : float):
        super().__init__(t_name)

        self.speed_pps  = 80.0
        self.position   = pygame.Vector2(t_x, t_y)
        self.velocity   = pygame.Vector2(0.0, 0.0)

        self.tracking_target : pygame.Vector2 = None

    def set_tracking_target(self, t_target_coords : pygame.Vector2) :
        self.tracking_target = t_target_coords

    """
        Basic player tracking behavior. 
    """
    def update(self, t_dt_s : float) :
        if self.tracking_target == None :
            self.speed_pps = 0.0 
        else :
            self.speed_pps = 80.0

        direction = (self.tracking_target - self.position).normalize()
        distance = direction.length_squared()

        self.velocity = direction * self.speed_pps

        if distance < 5 :
            self.speed_pps = 0.0

        self.position += self.velocity * t_dt_s
        super().update(t_dt_s)        

        # TODO : Check collision
