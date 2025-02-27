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
        
    def run(self):
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
        # Updates the game
        self.screen_display.fill("#2f3036")
        pygame.display.update()
        
    pygame.quit()
    
    
if __name__ == "__main__":
    game = Game()
    game.run()