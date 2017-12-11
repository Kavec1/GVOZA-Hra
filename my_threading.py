import threading
from move import *

def pohyb_raketa():
    c.bind('<Motion>', move_raketa)
    
def make_p1():
    a=-1
    tad=''
    while(1):
        a+=1
        tag='p1_'+str(a)
        priserka1(randint(0,800),randint(0,1000),tag)
        print(tag+' zije')
        sleep(5)

def make_p2():
    a=-1
    tad=''
    while(1):
        a+=1
        tag='p2_'+str(a)
        priserka2(randint(0,800),randint(0,1000),tag)
        print(tag+' zije')
        sleep(7.5)

def make_p3():
    a=-1
    tad=''
    while(1):
        a+=1
        tag='p3_'+str(a)
        priserka3(randint(0,800),randint(0,1000),tag)
        print(tag+' zije')
        sleep(10)
        
#definovanie vlakien programu
pohyb = threading.Thread(target=pohyb_raketa)
thread_p1 = threading.Thread(target=make_p1)
thread_p2 = threading.Thread(target=make_p2)
thread_31 = threading.Thread(target=make_p3)
