import pygame

pygame.init()

screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("pygame.mouse.get_pressed()")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen.fill(WHITE)
pygame.display.update()

sp = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    pressed = pygame.mouse.get_pressed()
    
    if pressed[0]:
        pos = pygame.mouse.get_pos()
        if sp is None:
            sp = pos
        width = pos[0] - sp[0]
        height = pos[1] - sp[1]

        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, (sp[0], sp[1], width, height), 2)
        pygame.display.update()
    else:
        sp = None

