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
    pygame.draw.rect(screen, (150, 150, 150), (100, 5, 100, 255), 1)
    pygame.draw.circle(screen, (254, 0, 0), (150, 50),    38)
    pygame.draw.circle(screen, (255, 255, 1), (150, 132), 38)
    pygame.draw.circle(screen, (0, 255, 1), (150, 215), 38)
    pygame.draw.line(screen, [150, 150, 150], [150, 260], [150, 268], 1)
    pygame.draw.polygon(screen, [150, 150, 150], [[100,268],[200,268],[232,300],[68,300]], 1)


    pygame.draw.polygon(screen, [0, 140, 255], [[100, 268], [200, 268], [211, 278], [89, 278]], 0) 
    pygame.draw.polygon(screen, [255, 255, 255], [[79, 290], [221, 290], [232, 300], [68, 300]], 0) 
    pygame.display.flip()

pygame.quit()


