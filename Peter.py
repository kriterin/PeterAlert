
from tkinter import *
import ctypes
import pygame
from time import sleep
from random import randint
import random
import jumpscare
import winsound
from jumpscare import *


window = Tk()


pygame.init()

def init_sound():
    pygame.mixer.init()

def playGiggle():
    soundGiggle = pygame.mixer.Sound("giggle.wav")
    soundGiggle.play()

def playAnger():
    soundAngry = pygame.mixer.Sound("peter_angry.wav")
    soundAngry.play()

def Moan():
    soundMoan = pygame.mixer.Sound("cum.wav")
    soundMoan.play()

def Ambatukam():
    soundAmbatukam = pygame.mixer.Sound("holy_fuck.wav")
    soundAmbatukam.play()

def play_sound():
    sound = pygame.mixer.Sound("stalker.wav")
    sound.play(loops=1)

def Ooze():
    soundOoze = pygame.mixer.Sound("splash.wav")
    soundOoze.set_volume(1.0)
    soundOoze.play()



ValueX = 0
ValueOK = 0
SPI_SETDESKWALLPAPER = 20




#if the user tries to exit via the X button, it instead add points and triggers Peter to become angry
# Then it supposed to jumpscare the user and change the background
def AddPointsToX():
    global ValueX
    print(ValueX)
    ValueX += 1
    if ValueX == 3:
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "scary_peter.jpg", 0)
        LaunchAttack()


def AddPointsToOK():
    global ValueOK
    print(ValueOK)
    ValueOK += 1
    if ValueOK == 10:
        playGiggle()
    if ValueOK == 30:
        Ambatukam()
    if ValueOK == 45:
        Moan()
        sleep(1.5)
        Ooze()






#----- Properties of the Window---------#
peter = PhotoImage(file='Peter.png')
window.geometry("400x100+732+450")
window.title("Peter Alert")
label = Label(window, image=peter)
winsound.PlaySound("SystemExit", winsound.SND_ASYNC)
window.protocol("WM_DELETE_WINDOW", AddPointsToX)

ButtonOk = Button(window,
                  text="OK",
                  padx=25,
                  pady=5,
                  command=AddPointsToOK)
#---------------------------------------#
ButtonOk.pack()
ButtonOk.place(x=163, y=50)
init_sound()
label.pack()
window.mainloop()

