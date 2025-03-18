import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Valgusfoor, Mäks Švaiko")
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
RED = (254, 0, 0)
YELLOW = (255, 255, 1)
GREEN = (0, 255, 1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (150, 150, 150), (100, 30, 100, 240), 1)
    pygame.draw.circle(screen, (254, 0, 0), (150, 72),    38)
    pygame.draw.circle(screen, (255, 255, 1), (150, 151), 38)
    pygame.draw.circle(screen, (0, 255, 1), (150, 229), 38)
    pygame.display.flip()

pygame.quit()


