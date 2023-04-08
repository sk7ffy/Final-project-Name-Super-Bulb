import pygame

main_win = pygame.display.set_mode((700,500))
pygame.display.set_caption('Super Bulb')
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False