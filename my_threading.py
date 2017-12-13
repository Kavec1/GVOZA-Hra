import threading
from init import *
from move import *
from random import *
from objects import *
from time import *

def pohyb_raketa():
    raketka(0,0)
    c.bind('<Motion>', move_raketa)
    c.bind('<Button-1>', vystrel)

def del_strela():
    while (1):
        sleep(.3)        
        c.delete('strela')

def make_p1():
    a=-1
    tad=''
    while(1):
        tag='p1_'
        x=randint(25,width-25)
        y=randint(25,height-250)
        #c.create_rectangle(x-25,y-20,x+25,y+20,outline='white')
        priserka1(x,y,tag)
        sleep(1)

def make_p2():
    a=-1
    tad=''
    while(1):
        tag='p2_'
        x=randint(25,width-25)
        y=randint(25,height-250)
        #c.create_rectangle(x-20,y-20,x+20,y+20,outline='white')
        priserka2(x,y,tag)
        print(tag+' zije')
        sleep(2.5)

def make_p3():
    a=-1
    tad=''
    while(1):
        tag='p3_'
        x=randint(25,width-25)
        y=randint(25,height-250)
        #c.create_rectangle(x-20,y-20,x+20,y+20,outline='white')
        priserka3(x,y,tag)
        print(tag+' zije')
        sleep(5)
        
#definovanie vlakien programu
pohyb = threading.Thread(target=pohyb_raketa, name='raketka')
thread_p1 = threading.Thread(target=make_p1, name='priserka1')
thread_p2 = threading.Thread(target=make_p2, name='priserka2')
thread_31 = threading.Thread(target=make_p3, name='priserka3')
del_strela = threading.Thread(target=del_strela, name='strela')
