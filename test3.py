import pygame

pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mouse event Demo")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen.fill(WHITE)
pygame.display.update()

FPS = 60
clock = pygame.time.Clock()
sp = ep = None

flStartDraw = False
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            flStartDraw = True
            sp = event.pos
        elif event.type == pygame.MOUSEMOTION:
            if flStartDraw:
                ep = event.pos
                width = ep[0] - sp[0]
                height = ep[1] - sp[1]
                pygame.draw.rect(screen, BLUE, (sp[0], sp[1], width, height), 2)

                pygame.display.update()
                screen.fill(WHITE)
                
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            flStartDraw = False

    
    # pygame.display.update()
    clock.tick(FPS)