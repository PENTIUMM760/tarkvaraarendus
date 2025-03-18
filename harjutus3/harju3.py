import pygame

pygame.init()

width, height = 640, 480
square_size = 20
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("Ülesanne 3")

def draw_grid():
    screen.fill((153, 255, 153))
    for i in range(0, width, square_size):
        pygame.draw.line(screen, (255, 0, 0), (i, 0), (i, height))  
    for j in range(0, height, square_size):
        pygame.draw.line(screen, (255, 0, 0), (0, j), (width, j))   

running = True
while running:
    draw_grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

pygame.quit()
