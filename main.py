from init import *
from objects import *
from move import *
from my_threading import *

def main():
    b1.config(state=DISABLED) #zmena stavu tlacidla1 na neaktivne
    pohyb.start() #aktivacia pohybu rakety
    thread_p1.start() #vytvaranie priseriek1
    thread_p2.start() #vytvaranie priseriek1
    #thread_p2.start() #vytvaranie priseriek1

    def strela(suradnice):
    x= suradnice.x
    y= suradnice.y
    c.create_line(x,y,x,0, fill='yellow', tags='strela')
   ## sleep(.5)
    ###c.delete('strela')'''
c.bind('<Button-1>', strela)
    
    mainloop() #koniec hlavnej casti programu

b1=Button(text='Start game',command=main) #tlacidol1
b1.pack()
b2=Button(text='Cancel game',command=quit) #tlacidlo2
b2.pack()
