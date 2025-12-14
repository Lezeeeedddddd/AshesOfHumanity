import pygame
from Games.map.importmap import GameMap

pygame.init()

screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Ashes Of Humanity")

game_map = GameMap(screen_size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    center = (screen_size[0] // 2, screen_size[1] // 2)
    game_map.render(screen, center)

    pygame.display.flip()

pygame.quit()