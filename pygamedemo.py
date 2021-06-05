import pygame


print("PyGame Demo")

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

x = screen_width // 2
y = screen_height // 2
speed = 5

screen.fill(WHITE)
pygame.display.update()

clock = pygame.time.Clock()
running = True

flStartDraw = False
sp = se = 0 
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
                height = event.pos[1] - sp[1]
                width = event.pos[0] - sp[0]

                screen.fill(WHITE)
                pygame.draw.rect(screen, RED, (sp[0], sp[1], width, height))
                pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            flStartDraw = False
        
    clock.tick(FPS)
