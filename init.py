from tkinter import *
import ctypes

user32 = ctypes.windll.user32
width=user32.GetSystemMetrics(0)
height=user32.GetSystemMetrics(1)
print('Width: '+str(width))
print('Height: '+str(height))
ml = Tk()
ml.attributes("-fullscreen",True)
c=Canvas(width=width, height=(height-100), bg='black')
c.pack()
