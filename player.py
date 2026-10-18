# External imports
import pygame

# Internal imports
from utils import load_image
from ientity import IEntity

"""

"""
class Player(IEntity) :
    """

    """
    def __init__(self, t_name):
        super().__init__(t_name)

        self.speed_pps  = 100.0
        self.position   = pygame.Vector2(0.0, 0.0)
        self.velocity   = pygame.Vector2(0.0, 0.0)

        self.attacking = False

    """

    """
    def handle_key_presses(self) :
        keys : list = pygame.key.get_pressed()

        # Handle movement related keys
        direction = pygame.Vector2(
            float(keys[pygame.K_d] - keys[pygame.K_a]),
            float(keys[pygame.K_s] - keys[pygame.K_w])
        )

        if direction.length_squared() : 
            direction.normalize_ip()

        self.velocity = direction * self.speed_pps

    """
        TODO : play an animation
    """
    def attack(self) :
        if not self.attacking:
            self.attacking = True
            self.animation_manager.animations["swing"].reset()  # rewind the clip only

    def update(self, t_dt_s: float):
        self.position += self.velocity * t_dt_s

        if self.attacking:
            self.animation_manager.play("swing")
            if self.animation_manager.finished:
                self.attacking = False
        if not self.attacking:
            moving = self.velocity.length_squared() > 0
            # self.animation_manager.play("walk" if moving else "idle")
            self.animation_manager.play("idle")

        super().update(t_dt_s)
