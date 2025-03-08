from settings import *
from sprites import *

class Game():
    def __init__(self):
        # General Setup
        pygame.init()
        self.screen_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Cookie")
        self.running = True
        self.clock = pygame.time.Clock()
        
        # Draw Cookie Sprite
        self.all_sprite = pygame.sprite.Group()
        self.cookie_sprite = Cookie(self.all_sprite)
         
        
    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000 
            # Event Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
            # Updates the game
            self.cookie_sprite.update(dt)
            
            # Draw the game
            self.screen_display.fill("#2f3036")
            self.all_sprite.draw(self.screen_display)
            pygame.display.update()
        
        pygame.quit()
    
    
if __name__ == "__main__":
    game = Game()
    game.run()