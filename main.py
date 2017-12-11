from init import *
from objects import *
from move import *
from my_threading import *

def main():
    b1.config(state=DISABLED) #zmena stavu tlacidla1 na neaktivne
    pohyb.start()
    thread_p1.start()
    thread_p2.start()

    mainloop() #koniec hlavnej casti programu

b1=Button(master, text='Start game',command=main) #tlacidol1
b1.pack()
b2=Button(master, text='Cancel game',command=quit) #tlacidlo2
b2.pack()
