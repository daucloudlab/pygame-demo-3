import pygame

pygame.init()

screen_width = 500
screen_height = 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PyGame library demo")

FPS = 60
clock  = pygame.time.Clock()


x, y = screen_width//2, screen_height//2
speed = 5

flLeft = flRight = False
running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                flLeft = True
            elif event.key == pygame.K_RIGHT:
                flRight = True
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                flLeft = flRight = False

    if flLeft:
        x -= speed
    elif flRight:
        x += speed
    
        
    pygame.draw.rect(screen, BLUE, (x, y, 20, 30))
    pygame.display.update()

    clock.tick(FPS)