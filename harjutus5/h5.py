import pygame, random

#Alustame pygame'iga
pygame.init()

#MUUTUJAD JA VÄRVID
bg_color = [200, 255, 200]  # taustavärv
red = [255, 0, 0]           # punane (halb tabamus)
green = [0, 200, 0]         # roheline (hea tabamus)
textcolor = [0, 0, 0]       # algne tekstivärv (must)

punktid = 0  # algne skoor

#Palli algne asukoht ja kiirus
ball_width, ball_height = 20, 20
posX, posY = 0, 0
speedX, speedY = 3, 4

#Aluse algne asukoht ja kiirus
pad_width, pad_height = 120, 20
posX2 = random.randint(0, 640 - pad_width)
speedX2 = 3

#Teksti font ja suurus
font = pygame.font.Font(pygame.font.match_font('sansserif'), 32)

#EKRAAN

screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Ping-pong")
clock = pygame.time.Clock()

#OBJEKTIDE LOOMINE

# Palli ja aluse pildid
ball_img = pygame.image.load("desktop/img/ball.png")
ball_img = pygame.transform.scale(ball_img, [ball_width, ball_height])

pad_img = pygame.image.load("desktop/img/pad.png")
pad_img = pygame.transform.scale(pad_img, [pad_width, pad_height])

#MÄNGU TSÜKKEL 

running = True
while running:
    clock.tick(180)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #PALLI LIIKUMINE 
    posX += speedX
    posY += speedY

    # Kui pall põrkab vasaku või parema ääre vastu
    if posX <= 0:
        posX = 0
        speedX = -speedX
    elif posX + ball_width >= screenX:
        posX = screenX - ball_width
        speedX = -speedX

    #Kui pall põrkab ülemise ääre vastu
    if posY <= 0:
        posY = 0
        speedY = -speedY

    #Kui pall puudutab alumist äärt ehk mängija ei saanud pihta
    if posY + ball_height >= screenY:
        posY = screenY - ball_height
        speedY = -speedY
        textcolor = red  #visuaalne vihje, et mööda läks

    ball = pygame.Rect(posX, posY, ball_width, ball_height)

    #ALUSE LIIKUMINE
    posX2 += speedX2
    if posX2 <= 0:
        posX2 = 0
        speedX2 = -speedX2
    elif posX2 + pad_width >= screenX:
        posX2 = screenX - pad_width
        speedX2 = -speedX2

    pad = pygame.Rect(posX2, screenY / 1.5, pad_width, pad_height)

    #Kui pall tabab alust
    if ball.colliderect(pad) and speedY > 0:
        speedY = -speedY
        punktid += 1
        textcolor = green

    #JOONISTAMINE 

    screen.fill(bg_color)
    screen.blit(ball_img, ball)
    screen.blit(pad_img, pad)

    text = font.render(f"Skoor: {punktid}", True, textcolor)
    screen.blit(text, [10, 10])

    pygame.display.flip()
