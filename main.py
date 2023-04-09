import time 
import pygame


######
# vars
###### 

focus = 25
short = 5
long  = 12
timer = 0
sesh = []

pygame.mixer.init()

def jump():
    for i in range(100):
        print("")

def update(now, end):
    # Convertir en minutes
    time_remaining = end - now
    min_remaining = int(time_remaining // 60)
    sec_remaining = int(time_remaining % 60)
    print("%d:%02d" % (min_remaining, sec_remaining)) # Utilisation de % pour formater la chaîne de caractères avec des zéros devant les secondes si nécessaire

# hide pygame message 
jump()

###########
# main menu
###########
while True:
    # display 3 options 
    jump()
    print("current session : ", sesh)
    print("1: focus ", focus , "min")
    print("2: short break ", short, "min")
    print("3: long break ", long, "min")
    print("")
    # await for user input 
    choice = int(input())

    match choice:
        case 1: 
            print("focus timer started")
            sesh.append("long")
            now = time.time()
            # calculate "arrival time"
            end = now + 60*focus
            pygame.mixer.music.load("rsc/xpSound.mp3")
            pygame.mixer.music.play()

            while (end - now >= 0):
                now = time.time()
                update(now,end)
                time.sleep(1)
            pygame.mixer.music.load("rsc/tterm.mp3")
            pygame.mixer.music.play()
        case 2: 
            sesh.append("short break")
            print("short break timer started")
            pygame.mixer.music.load("rsc/pause.mp3")
            pygame.mixer.music.play()
            now = time.time()
            end = now + 60*short
            while (end - now >= 0):
                now = time.time()
                update(now,end)
                time.sleep(1) 
            pygame.mixer.music.load("rsc/encoreT.mp3")
            pygame.mixer.music.play()
        case 3: 
            sesh.append("long break")
            print("long break timer started")

            pygame.mixer.music.load("rsc/pause.mp3")
            pygame.mixer.music.play()
            now = time.time()
            end = now + 60*long 
            while (end - now >= 0):
                now = time.time()
                update(now,end)
                time.sleep(1) 
            pygame.mixer.music.load("rsc/encoreT.mp3")
            pygame.mixer.music.play()

