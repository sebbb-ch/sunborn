# External imports
import pygame, json, random, glob, ast, sys, os
from pygame.locals import *

# Internal imports
from utils import *
from player import *
from enemy import *

# =============================================================================

init_pygame()

renderer = Renderer(160, 144, 3)

# Declare entities - TODO : make this a manager probably
player = Player("player")
enemy = Enemy("cryogonal", 100, 100)

renderer.register_entity(player)
renderer.register_entity(enemy)

# =============================================================================
# Main game loop
# =============================================================================

playing = True
while playing:
    dt_s = renderer.tick_clock()
    renderer.clear_frame()

    # Check events for player/world actions
    for event in pygame.event.get() :
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN : 
            if event.key == K_SPACE :
                player.attack()

    # Player updates
    player.handle_key_presses()
    player.update(dt_s)

    # Enemy updates
    enemy.set_tracking_target(player.position)
    enemy.update(dt_s)

    renderer.render()

pygame.quit()
sys.exit()