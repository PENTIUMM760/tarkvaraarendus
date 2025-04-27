import pygame
import random
from moviepy.editor import VideoFileClip

#Pygame ja helimoodul 
pygame.init()  # Pygame'i alglaadimine
pygame.mixer.init()  # Alglaadime Pygame'i helimooduli et mängida helisid

#Muusika esitlusloend
songs = ['desktop/s1.mp3', 'desktop/s2.mp3', 'desktop/s3.mp3']  # Muusika failid esitlusloendis
song = random.choice(songs)  #Valib suvalise loo esitlusloendist
try:
    pygame.mixer.music.load(song)  #Laeb valitud loo Pygame'i muusikamängijasse
    pygame.mixer.music.play(-1)           # Mängib muusikat lõpmatuseni
    pygame.mixer.music.set_volume(0.2)  # Seadistab helitugevuse 0.2 peale
    print(f"Playing music: {song}")  #Kuvab millist muusikat praegu mängitakse
except Exception as e:
    print("Muusika laadimine ebaõnnestus:", e)  #Kui muusika laadimisel ilmneb viga kuvab vea sõnumi

#Video laadimine MoviePy’ga
video_path = "desktop/smb1.mp4"  #Määrab video faili asukoha
clip = VideoFileClip(video_path)  #Laeb video MoviePy abil
fps = clip.fps or 24  #Kasutab video kaadrisagedust või määrab vaikimisi väärtuseks 24
w, h = clip.size  #Saab video suuruse (laius ja kõrgus)

#Pygame aken sama suurusega
screen = pygame.display.set_mode((w, h))  #Loob Pygame akna mis on sama suur kui video
pygame.display.set_caption("Video taust + muusika")  #Seab akna pealkirja

clock = pygame.time.Clock()  #Loob kella et hallata mängu kiirust
frame_iter = clip.iter_frames(fps=fps, dtype="uint8")  #Loob kaader kaadri iteratsiooni et video raamid lugeda

running = True  #Muutujat mis hoiab mängu tsükli käimas
while running:
    #Töötle sündmused
    for ev in pygame.event.get():  #läbib kõik sündmused mis on Pygame'is toimunud
        if ev.type == pygame.QUIT:  #Kui kasutaja klõpsab akna sulgemiseks
            running = False  #Lõpetab tsükli

    #Loeb järgmise kaadri või alustab uuesti
    try:
        frame = next(frame_iter)  #Loeb järgmise kaadri video kaader iteratsioonist
    except StopIteration:  #Kui video kaadrid on läbi
        frame_iter = clip.iter_frames(fps=fps, dtype="uint8")  #Algatab video kaadrite lugemise uuesti
        frame = next(frame_iter)  #Loe järgmine kaader

    #Teeb Pygame pinnaks ja kuva
    #MoviePy annab kaadri RGB-vormingus (h, w, 3), Pygame vajab (w, h, 3)
    surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))  #Loob Pygame pinnase kaadrist
    screen.blit(surface, (0, 0))  # Kuvame kaadri ekraanil
    pygame.display.flip()  #Uuendab ekraani et uus kaader kuvataks

    #Hoiab õiget FPS'i
    clock.tick(fps)  # Hoiab õiget kaadrisagedust et video ei hakkaks vahelduma liiga kiiresti ega aeglaselt

#Puhasta ja sulge 
clip.reader.close()  #Sulgeb video lugemisprotsessi
pygame.mixer.music.stop()  #Peatab muusika esitamise
pygame.quit()  #Lõpetab Pygame'i et puhastada mälu ja sulgeda kõik aknad
