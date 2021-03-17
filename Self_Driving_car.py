import pygame
pygame.init()
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('track1.png')
car = pygame.image.load('tesla.png')
while True:
    window.blit(track, (0, 0))
    pygame.display.update()