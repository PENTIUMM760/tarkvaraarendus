import pygame, random
import sys  # Lisatud süsteemimoodul

# Alustame pygame'iga
pygame.init()

# MUUTUJAD JA VÄRVID
bg_color = [200, 255, 200]  # taustavärv
red = [255, 0, 0]           # punane (halb tabamus)
green = [0, 200, 0]         # roheline (hea tabamus)
textcolor = [0, 0, 0]       # algne tekstivärv (must)

punktid = 0  # algne skoor

# Palli algne asukoht ja kiirus
ball_width, ball_height = 20, 20
posX, posY = 0, 0
speedX, speedY = 3, 4

# Aluse algne asukoht ja kiirus
pad_width, pad_height = 120, 20
posX2 = random.randint(0, 640 - pad_width)
posY2 = 480 / 1.5  # Aluse Y-positsioon on nüüd konstantne
speedX2 = 0  # Ei liigu automaatselt, liigub klaviatuuriga

# Teksti font ja suurus
font = pygame.font.Font(pygame.font.match_font('sansserif'), 32)

# EKRAAN
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Ping-pong")
clock = pygame.time.Clock()

# TAUSTAMUUSIKA
try:
    pygame.mixer.music.load("desktop/sound/bg_music.mp3")  # Asenda oma muusikafailiga
    pygame.mixer.music.set_volume(0.5)  # Helitugevus 50%
    pygame.mixer.music.play(-1)  # Mängib lõputult
except:
    print("Muusikafaili ei leitud või ei saanud laadida")

# OBJEKTIDE LOOMINE
# Palli ja aluse pildid
try:
    ball_img = pygame.image.load("desktop/img/ball.png")
    ball_img = pygame.transform.scale(ball_img, [ball_width, ball_height])
    
    pad_img = pygame.image.load("desktop/img/pad.png")
    pad_img = pygame.transform.scale(pad_img, [pad_width, pad_height])
except:
    # Kui pildid puuduvad, kasutame lihtsaid ristkülikuid
    ball_img = pygame.Surface((ball_width, ball_height))
    ball_img.fill((255, 0, 0))
    pad_img = pygame.Surface((pad_width, pad_height))
    pad_img.fill((0, 0, 255))

# MÄNGU TSÜKKEL 
running = True
game_over = False

while running:
    clock.tick(60)  # FPS 60 on piisav
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:  # R klahv restartib mängu
                game_over = False
                punktid = 0
                posX, posY = 0, 0
                posX2 = random.randint(0, 640 - pad_width)
                textcolor = [0, 0, 0]
    
    if not game_over:
        # PALLI LIIKUMINE 
        posX += speedX
        posY += speedY

        # Kui pall põrkab vasaku või parema ääre vastu
        if posX <= 0:
            posX = 0
            speedX = -speedX
        elif posX + ball_width >= screenX:
            posX = screenX - ball_width
            speedX = -speedX

        # Kui pall põrkab ülemise ääre vastu
        if posY <= 0:
            posY = 0
            speedY = -speedY

        # Kui pall puudutab alumist äärt - mäng läbi
        if posY + ball_height >= screenY:
            game_over = True
            textcolor = red

        ball = pygame.Rect(posX, posY, ball_width, ball_height)

        # ALUSE LIIKUMINE KLAVIATUURIGA
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            posX2 -= 5
        if keys[pygame.K_RIGHT]:
            posX2 += 5
            
        # Kontrollime, et alus ei väljuks ekraanist
        if posX2 < 0:
            posX2 = 0
        elif posX2 + pad_width > screenX:
            posX2 = screenX - pad_width

        pad = pygame.Rect(posX2, posY2, pad_width, pad_height)

        # Kui pall tabab alust
        if ball.colliderect(pad) and speedY > 0:
            speedY = -speedY
            punktid += 1
            textcolor = green

    # Joonistamine
    screen.fill(bg_color)
    screen.blit(ball_img, ball)
    screen.blit(pad_img, pad)

    text = font.render(f"Skoor: {punktid}", True, textcolor)
    screen.blit(text, [10, 10])
    
    if game_over:
        game_over_text = font.render("MÄNG LÄBI! Vajuta R uuesti alustamiseks", True, red)
        screen.blit(game_over_text, [screenX//2 - game_over_text.get_width()//2, screenY//2])

    pygame.display.flip()

pygame.quit()
sys.exit()
#sain 75 score xD