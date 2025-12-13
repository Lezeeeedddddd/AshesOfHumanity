import pygame
pygame.init()

#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#pygame.display.set_caption("Ashes Of Humanity")


pygame.display.set_mode((800,600))#taille de la fenêtre
pygame.display.set_caption("Ashes Of Humanity")#Nom du jeu

#boucle du jeu
running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
#Pour que la fenêtre ne se ferme pas
pygame.quit()