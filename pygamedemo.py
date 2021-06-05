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


clock = pygame.time.Clock()
running = True
flLeft = flRight = False

while running:

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
            if event.key == pygame.K_LEFT:
                flLeft = False
            elif event.key == pygame.K_RIGHT:
                flRight = False
    
    if flLeft:
        x -= speed
    elif flRight:
        x += speed

    screen.fill(WHITE) 
    pygame.draw.rect(screen, BLUE, (x, y, 10, 20))
    pygame.display.update()          
    
    clock.tick(FPS)
