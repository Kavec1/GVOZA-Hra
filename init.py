from tkinter import *
import ctypes

user32 = ctypes.windll.user32
width=user32.GetSystemMetrics(0) #funkcia, ktora si pyta sirku obrazovky
height=user32.GetSystemMetrics(1) #funkcia, ktora si pyta vysku obrazovky
print('Width: '+str(width))
print('Height: '+str(height))
ml = Tk()
ml.attributes("-fullscreen",True) #vec ktora nastavuje okna na celu obrazovku
c=Canvas(width=width, height=(height-100), bg='black') #nastavenie rozmerov okna
c.pack()
