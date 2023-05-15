import tkinter as tk
import random
import time
import pygame
from PIL import Image, ImageTk

pygame.init()


def init_sound():
    pygame.mixer.init()


def play_sound():
    sound = pygame.mixer.Sound("stalker.wav")
    sound.play()


def LaunchAttack():
    root = tk.Tk()
    root.withdraw()

    image = Image.open("peteralert.png")
    image = image.resize((500, 500), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)

    def spawn_window():
        x = random.randint(0, 1920 - 500)
        y = random.randint(0, 1080 - 500)
        win = tk.Toplevel(root)
        win.geometry(f"500x500+{x}+{y}")
        labelScare = tk.Label(win, image=image)
        labelScare.pack()
        play_sound()
        play_sound()

    # the i * X determines the rate in miliseconds of how many windows are spawned
    for i in range(50):
        root.after(i * 10, spawn_window)

    root.mainloop()
    init_sound()
LaunchAttack()
