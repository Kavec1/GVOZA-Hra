import threading
from init import *
from move import *
from random import *
from objects import *
from time import *

hitbox=[]
for i in range(height):
    temp=[]
    for j in range(width):
        temp.append(0)
    hitbox.append(temp)
    #hitbox[y][x]
#vlakno programu starajuce sa o pohyb rakety
def pohyb_raketa():
    raketka(0,0)
    c.bind('<Motion>', move_raketa)
    c.bind('<Button-1>', vystrel)

#vlakno programu starajuce sa o zmazanie strely (zlta ciara)
def del_strela():
    sleep(.5)        
    c.delete('strela')
    '''print(str(del_strela._is_stopped()))
    del_strela._stop()
    print(str(del_strela._is_stopped()))
    treba opraviť'''
#vlakna programu starajuce sa o vykreslenie priseriek p1, p2 a p3
def make_p1():
    a=0
    tag=''
    global hitbox
    while(1):
        tag='1'+str(a)
        x=randint(25,width-25)
        y=randint(25,height-250)
        #c.create_rectangle(x-25,y-20,x+25,y+20,outline='white')
        priserka1(x,y,tag)
        for i in range(x-20,x+20):
            hitbox[y+25][i]=int(tag)        
        print(tag+' zije')
        a+=1
        sleep(1)

def make_p2():
    a=0
    tag=''
    global hitbox
    while(1):
        tag='2'+str(a)
        x=randint(25,width-25)
        y=randint(25,height-250)
        #c.create_rectangle(x-20,y-20,x+20,y+20,outline='white')
        priserka2(x,y,tag)
        for i in range(x-20,x+20):
            hitbox[y+20][i]=int(tag)
        print(tag+' zije')
        a+=1
        sleep(2.5)

def make_p3():
    a=0
    tag=''
    global hitbox
    while(1):
        tag='3'+str(a)
        x=randint(25,width-25)
        y=randint(25,height-250)
        #c.create_rectangle(x-20,y-20,x+20,y+20,outline='white')
        priserka3(x,y,tag)
        for i in range(x-20,x+20):
            hitbox[y+20][i]=int(tag)
        print(tag+' zije')
        a+=1
        sleep(5)
        
#definovanie vlakien programu
pohyb = threading.Thread(target=pohyb_raketa, name='raketka')
thread_p1 = threading.Thread(target=make_p1, name='priserka1')
thread_p2 = threading.Thread(target=make_p2, name='priserka2')
thread_p3 = threading.Thread(target=make_p3, name='priserka3')
del_strela = threading.Thread(target=del_strela, name='strela')
