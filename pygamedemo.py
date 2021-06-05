import pygame


pygame.init()

screen_width = 500
screen_height = 500
FPS = 60

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PyGame Demo App")
pygame.display.set_icon(pygame.image.load('logo.bmp'))

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.draw.rect(screen, WHITE, (10, 10, 50, 100), 2)

pygame.draw.line(screen, GREEN, (200, 20), (350, 50), 5)
pygame.draw.aaline(screen, GREEN, (200, 40), (350, 70), 5)

pygame.draw.lines(screen, RED, True, [(200, 80), (250, 80), (300, 200)], 2)
pygame.draw.aalines(screen, RED, True, [(300, 80), (350, 80), (400, 200)], 2)

pygame.draw.polygon(screen, WHITE, [(150, 210), (180, 250), (90, 290), (30, 230)])
pygame.draw.polygon(screen, WHITE, [(150, 310), (180, 350), (90, 390), (30, 330)], 1)

pygame.draw.circle(screen, BLUE, (300, 250), 40)
pygame.draw.ellipse(screen, BLUE, (300, 300, 100, 50), 1)

pi = 3.14
pygame.draw.arc(screen, RED, (450,30,50,150), pi, 2*pi, 5)

pygame.display.update()

clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    
    clock.tick(FPS)
