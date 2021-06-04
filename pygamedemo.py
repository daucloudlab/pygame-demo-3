import pygame
import sys

print("PyGame Demo")

pygame.init()

screen_width = 500
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PyGame Demo App")

clock = pygame.time.Clock()
running = True

while running:

    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
