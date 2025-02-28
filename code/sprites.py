from settings import *

class Cookie(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        
        # Get Images
        self.image =pygame.image.load(join("img", "0.png")).convert_alpha() # resize the image files
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        