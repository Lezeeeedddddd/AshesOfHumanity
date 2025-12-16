import pygame
from Games.map.importmap import GameMap
pygame.init()


#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#pygame.display.set_caption("Ashes Of Humanity")


screen_size = (800,600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Ashes Of Humanity")#Nom du jeu
gamemap = GameMap(screen_size)
clock = pygame.time.Clock()
running = True

#boucle du jeu
while running :
    clock.tick(60) #nb fps
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill((0, 0, 0))#ecran sous la map (noir)
        gamemap.render(screen, (1084, 800))#centre de la map
        pygame.display.flip()#rafraichir la map
        #Pour que la fenêtre ne se ferme pas
pygame.quit()
