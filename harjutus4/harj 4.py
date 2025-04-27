import pygame, sys, random
pygame.init()
 
# Ekraani seadistused
screenX = 640  # ekraani laius
screenY = 480  # ekraani kõrgus
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Autod")  # aknale pealkiri
clock = pygame.time.Clock()  # ajahaldur

# Siniste autode algkiirused (alguses aeglaselt, et mängijal oleks võimalus mööda sõita)
speedY = 1    # esimese sinise auto kiirus
speedY2 = 1   # teise sinise auto kiirus
speedY3 = 1   # kolmanda sinise auto kiirus

# Autode algpositsioonid
autoX = 295  # punase auto X-koordinaat
autoY = 350  # punase auto Y-koordinaat
# Kolme sinise auto juhuslikud algpositsioonid
sinine_autoX = random.randint(150, 225)
sinine_autoY = random.randint(0, 240)
sinine_autoX2 = random.randint(275, 340)
sinine_autoY2 = random.randint(0, 120)
sinine_autoX3 = random.randint(375, 450)
sinine_autoY3 = random.randint(0, 240)

# Laen taustapildi
taust = pygame.image.load("desktop/bg_rally.jpg")

### PUNANE AUTO ###
# Loob punase auto ristküliku ja laeb sellele pildi
punane_auto = pygame.image.load("desktop/f1_red.png")
punane_auto = pygame.Rect(autoX, autoY, 45, 90)  # auto hitbox
punane_auto_pilt = pygame.image.load("desktop/f1_red.png")
punane_auto_pilt = pygame.transform.scale(punane_auto_pilt, [punane_auto.width, punane_auto.height])

### SINISED AUTOD ###
# Loome kolm sinist autot ja nende pildid

# Esimene sinine auto
sinine_auto = []
for i in range(3):
    sinine_auto.append(pygame.Rect(sinine_autoX, random.randint(0, 240), 45, 90))
sinine_auto_pilt = pygame.image.load('desktop/f1_blue.png')
sinine_auto_pilt = pygame.transform.scale(sinine_auto_pilt, [sinine_auto[0].width, sinine_auto[0].height])

# Teine sinine auto
sinine_auto2 = []
for i in range(3):
    sinine_auto2.append(pygame.Rect(sinine_autoX, random.randint(0, 240), 45, 90))
sinine_auto_pilt2 = pygame.image.load('desktop/f1_blue.png')
sinine_auto_pilt2 = pygame.transform.scale(sinine_auto_pilt2, [sinine_auto2[0].width, sinine_auto2[0].height])

# Kolmas sinine auto
sinine_auto3 = []
for i in range(3):
    sinine_auto3.append(pygame.Rect(sinine_autoX, random.randint(0, 240), 45, 90))
sinine_auto_pilt3 = pygame.image.load('desktop/f1_blue.png')
sinine_auto_pilt3 = pygame.transform.scale(sinine_auto_pilt3, [sinine_auto3[0].width, sinine_auto3[0].height])

# Kuvame taustapildi
screen.blit(taust,[0,0])

# Mängu skoori muutujad
punktid = 0       # praegused punktid
highscore = 0     # parim tulemus

playing = True    # mängu oleku muutuja

# Fondi seadistamine teksti jaoks
font = pygame.font.Font(pygame.font.match_font('sansserif'), 32)

# Mängu läbi teksti ettevalmistamine
gameover = font.render("Mäng läbi! Vajuta Enter, et uuesti proovida", True, [255,255,255])
gameover2 = font.render("Või vajuta Escape, et väljuda.", True, [255,255,255])
finalscore = font.render(f"Sinu skoor: {punktid}", True, [0,0,0])

# Põhimängu tsükkel
running = True
while running:
    clock.tick(60)  # 60 kaadrit sekundis
    
    # Sündmuste töötlemine
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Kui kasutaja sulgeb akna
            running = False

    # Mängu lõppu tingimused
    if playing == False:
        # Uuendame parimat skoori kui vaja
        if punktid > highscore:
            highscore = punktid

        # Kuvame mängu lõpu ekraani
        lBlue = [153, 204, 255]
        screen.fill(lBlue)
        
        # Kuvame kõik mängu lõpu tekstid
        screen.blit(gameover, [100,100])
        screen.blit(gameover2, [100,130])
        finalscore = font.render(f"Sinu skoor: {punktid}", True, [0,0,0])
        screen.blit(finalscore, [100,190])
        highscoretext = font.render(f"Sinu kõrgeim skoor: {highscore}", True, [0,0,0])
        screen.blit(highscoretext, [100,220])

        # Klaviatuuri sisendi töötlemine
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_ESCAPE]:  # ESC - väljub mängust
            running = False

        if pressed[pygame.K_RETURN]:  # ENTER - alustab uut mängu
            # Lähtestame kõik vajalikud muutujad
            punktid = 0
            sinine_autoX = random.randint(150, 225)
            sinine_autoY = random.randint(0, 240)
            sinine_autoX2 = random.randint(275, 340)
            sinine_autoY2 = random.randint(0, 120)
            sinine_autoX3 = random.randint(375, 450)
            sinine_autoY3 = random.randint(0, 240)
            autoX = 295
            punane_auto = pygame.Rect(autoX, autoY, 45, 90)
            playing = True
            
    elif playing == True:  # Kui mäng käib
        ### Punase auto liigutamine ###
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:  # Vasak nool - liigub vasakule
            autoX -= 4
            punane_auto = pygame.Rect(autoX, autoY, 45, 90)
        if pressed[pygame.K_RIGHT]:  # Parem nool - liigub paremale
            autoX += 4
            punane_auto = pygame.Rect(autoX, autoY, 45, 90)

        # Piirangud, et auto jääks teele
        if autoX < 150:
            autoX = 150
        if autoX > 450:
            autoX = 450

        # Kuvame skoori
        text = font.render(f"Skoor:{punktid}", True, [0,0,0])
        screen.blit(text, [0,0])

        ### Siniste autode liigutamine ja töötlemine ###

        # Esimene sinine auto
        for auto in sinine_auto[:]:
            sinine_autoY += speedY
            auto.update(sinine_autoX, sinine_autoY, 45,90)
            if sinine_autoY > 480:  # Kui auto jõuab ekraani alla
                # Lähtestame auto positsiooni ja kiiruse
                sinine_autoY = 0
                sinine_autoX = random.randint(150, 225)
                speedY = random.randint(1, 2)
                punktid += 1  # Lisame punkti

            # Kokkupõrke kontroll punase autoga
            if punane_auto.colliderect(auto): 
                playing = False
        
        # Teine sinine auto
        for auto2 in sinine_auto2[:]:
            sinine_autoY2 += speedY2
            auto2.update(sinine_autoX2, sinine_autoY2, 45,90)
            if sinine_autoY2 > 480:
                sinine_autoY2 = 0
                sinine_autoX2 = random.randint(275, 340)
                speedY2 = random.randint(1, 2)
                punktid += 1

            if punane_auto.colliderect(auto2): 
                playing = False
        
        # Kolmas sinine auto
        for auto3 in sinine_auto3[:]:
            sinine_autoY3 += speedY3
            auto3.update(sinine_autoX3, sinine_autoY3, 45,90)
            if sinine_autoY3 > 480:
                sinine_autoY3 = 0
                sinine_autoX3 = random.randint(375, 450)
                speedY3 = random.randint(1, 2)
                punktid += 1

            if punane_auto.colliderect(auto3): 
                playing = False

        # Kuvame kõik autod ekraanile
        for auto in sinine_auto:
            screen.blit(sinine_auto_pilt, auto)
        for auto2 in sinine_auto2:
            screen.blit(sinine_auto_pilt2, auto2)
        for auto3 in sinine_auto3:
            screen.blit(sinine_auto_pilt3, auto3)

    # Graafika uuendamine
    pygame.display.flip()
    screen.blit(taust,[0,0])  # Tausta uuendamine
    screen.blit(punane_auto_pilt, punane_auto)  # Punase auto uuendamine

pygame.quit()