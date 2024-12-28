import pygame
from os.path import join
from random import randint

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True

# surface
surf = pygame.Surface((100, 200))
surf.fill('orange')
x = 100

# importing an image
player_surface = pygame.image.load(
    join('images', 'player.png')).convert_alpha()

# import stars
star_surface = pygame.image.load(
    join('images', 'star.png')).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT))
                  for i in range(20)]


while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw the game
    display_surface.fill('darkgray')
    for pos in star_positions:
        display_surface.blit(star_surface, pos)

    x += 0.1
    display_surface.blit(player_surface, (x, 150))

    pygame.display.update()
pygame.quit()
