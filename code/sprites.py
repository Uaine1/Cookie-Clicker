from settings import *

class Cookie(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)

        self.load_images()
        self.cookie_frames = 0
        
        # Get Images
        self.image =pygame.image.load(join("img", "0.png")).convert_alpha() # resize the image files
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        # Bite Timer
        self.can_bite = True
        self.bite_time = 0
        self.bite_cd = 100


    def load_images(self):
        self.frames = []
        
        for folder_path, _, file_names in walk("img"):
            if file_names:
                for file_name in sorted(file_names, key= lambda name: int(name.split(".")[0])):
                    full_path = join(folder_path, file_name)
                    self.frames.append(pygame.image.load(full_path).convert_alpha())


    def input(self):
        if pygame.mouse.get_pressed()[0] and self.can_bite:
            self.animate()
            self.can_bite = False
            self.bite_time = pygame.time.get_ticks()
            
        self.bite_timer()


    def bite_timer(self):
        if not self.can_bite:
            current_time = pygame.time.get_ticks()
            if current_time - self.bite_time > self.bite_cd:
                self.can_bite = True
        

    def animate(self):
        if self.frames:
            self.cookie_frames = (self.cookie_frames +  1) % len(self.frames)
            self.image = self.frames[self.cookie_frames] 


    def update(self, _):
        self.input()