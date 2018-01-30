from init import *
from objects import *
from move import *
from my_threading import *

def main():
    c.create_text(width/2, height-150, text='SAVE ZONE', font='Arial 25 bold', fill='red')
    c.create_line(0,height-230,width,height-230, fill='red')
    for i in range(0,width,50):
    	c.create_line(i,height,i+50,height-230, fill='red')
    b1.config(state=DISABLED) #zmena stavu tlacidla1 na neaktivne
    pohyb.start() #aktivacia pohybu rakety
    del_strela.start()
    thread_p1.start() #vytvaranie priseriek1
    thread_p2.start() #vytvaranie priseriek1
    #thread_p3.start() #vytvaranie priseriek1

    mainloop() #koniec hlavnej casti programu

b1=Button(text='Start game',command=main) #tlacidol1
b1.pack()
b2=Button(text='Cancel game',command=quit) #tlacidlo2
b2.pack()
v = StringVar()
Label(textvariable=v).pack() 
v.set('Score: ')
