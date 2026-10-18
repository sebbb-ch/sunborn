# External imports
import pygame, glob, json

# Internal imports
from utils import load_image

"""
The /assets/animations/ folder will contain subfolders whose names are entities.
These subfolders must also contain a json file of the same entity name.

The entity animation manager should just take the entity name then
"""

class Animation :
    def __init__(self, 
            t_frames : list[pygame.Surface], 
            t_frame_time_s : float,
            t_loop : bool
        ) :

        self.curr_frame     = None
         
        self.frames         = t_frames
        self.frame_time_s   = t_frame_time_s

        self.loop           = t_loop
        # self.finished       = False

        self.duration_s     = len(t_frames) * t_frame_time_s
        self.elapsed_s      = 0.0

    def update(self, t_dt_s):
        self.elapsed_s += t_dt_s
        if self.loop:
            self.elapsed_s %= self.duration_s
        else:
            self.elapsed_s = min(self.elapsed_s, self.duration_s)

    def reset(self):
        self.elapsed_s = 0.0

    @property
    def finished(self):
        return not self.loop and self.elapsed_s >= self.duration_s

    @property
    def frame(self):
        return self.frames[min(
            int(self.elapsed_s / self.frame_time_s), 
            len(self.frames) - 1)
            ]


class EntityAnimationManager : 
    """
        @param : t_entity_name
    """
    def __init__(self, t_entity_name):
        self.entity_name = t_entity_name

        self.animations : dict      =  {}
        # ATTENTION : this sets a hard requirement that all entities have an idle
        self.curr_animation : str   = "idle"

        animations_dir = "./assets/animations/"
        entity_animations_path = animations_dir+t_entity_name+"/"
        self._load_animations(entity_animations_path)

    """

    """
    def _load_animations(self, t_entity_anim_dir) :
        # ATTENTION : this sets a hard requirement on the name of the json file
        json_config_path = t_entity_anim_dir + self.entity_name + ".json"
        with open(json_config_path, "r") as config_file:
            config = json.load(config_file)
            for anim_name in config  :
                animation_dir : str             = t_entity_anim_dir+anim_name
                frame_names : list[str]         = sorted(glob.glob(animation_dir+"/*.png"))
                frames : list[pygame.Surface]   = [load_image(f) for f in frame_names]

                anim = Animation(
                    frames,
                    config[anim_name]["frame_time_s"],
                    config[anim_name]["loop"]
                )
                print(anim_name)
                anim.curr_frame = frames[0]
                self.animations[anim_name] = anim

    """
    This function changes the current "animation state" so that the curr_frame 
    property returns the correct one to the renderer
    """
    def play(self, t_animation_name : str, t_restart : bool = False) :
        if t_animation_name != self.curr_animation or t_restart:
            self.curr_animation = t_animation_name
            self.animations[t_animation_name].reset()

    def update(self, t_dt_s: float):
        if self.curr_animation != None :
            self.animations[self.curr_animation].update(t_dt_s)

    def get_curr_frame(self):
        return self.animations[self.curr_animation].frame

    def restart(self, t_animation_name: str):
        self.animations[t_animation_name].reset()

    @property
    def finished(self) -> bool:
        return self.animations[self.curr_animation].finished