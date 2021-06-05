import pygame


print("PyGame Demo")

pygame.init()

screen_width = 500
screen_height = 500
FPS = 60

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PyGame Demo App")


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

x = screen_width // 2
y = screen_height // 2
speed = 5

screen.fill(WHITE)
pygame.display.update()

clock = pygame.time.Clock()
running = True
sp = None 

pygame.mouse.set_visible(False)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    screen.fill(WHITE)

    pos = pygame.mouse.get_pos()

    if pygame.mouse.get_focused():
        pygame.draw.circle(screen, BLUE, pos, 7)
        
    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        if sp is None:
            sp = pos

        width = pos[0] - sp[0]
        height = pos[1] - sp[1]

        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, (sp[0], sp[1], width, height))
        
    else:
        sp = None

    pygame.display.update()

    clock.tick(FPS)
