import threading
from move import *
from random import *
from objects import *
from time import *

def pohyb_raketa():
    raketka(0,0)
    c.bind('<Motion>', move_raketa)
    
def make_p1():
    a=-1
    tad=''
    while(1):
        a+=1
        tag='p1_'+str(a)
        priserka1(randint(25,width-25),randint(25,height-250),tag)
        print(tag+' zije')
        sleep(1)

def make_p2():
    a=-1
    tad=''
    while(1):
        a+=1
        tag='p2_'+str(a)
        priserka2(randint(25,width-25),randint(25,height-250),tag)
        print(tag+' zije')
        sleep(2.5)

def make_p3():
    a=-1
    tad=''
    while(1):
        a+=1
        tag='p3_'+str(a)
        priserka3(randint(25,width-25),randint(25,height-250),tag)
        print(tag+' zije')
        sleep(5)
        
#definovanie vlakien programu
pohyb = threading.Thread(target=pohyb_raketa, name='raketka')
thread_p1 = threading.Thread(target=make_p1, name='priserka1')
thread_p2 = threading.Thread(target=make_p2, name='priserka2')
thread_31 = threading.Thread(target=make_p3, name='priserka3')
