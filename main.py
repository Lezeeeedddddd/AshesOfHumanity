import pygame
from Games.map.importmap import GameMap
pygame.init()


#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#pygame.display.set_caption("Ashes Of Humanity")

class Game:
    def __init__(self):
        self.screen_size = (800,600)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Ashes Of Humanity")#Nom du jeu
        self.gamemap = GameMap(self.screen_size)
        
        self.running = True
    
    def run(self):
        #boucle du jeu
        while self.running :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill((0, 0, 0))
            self.gamemap.render(self.screen, (1084, 800))#centre de la map
            pygame.display.flip()#rafraichir la map
        #Pour que la fenêtre ne se ferme pas
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()