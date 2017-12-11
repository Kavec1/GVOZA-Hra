import threading
from move import *
def pohyb_raketa():
    c.bind('<Motion>', move_raketa)
def make_p1():
    while(1):
        priserka1(randint(0,800),randint(0,1000))
        print('priserka1 zije')
        sleep(5)

def make_p2():
    while(1):
        priserka2(randint(0,800),randint(0,1000))
        print('priserka2 zije')
        sleep(7.5)

def make_p3():
    while(1):
        priserka3(randint(0,800),randint(0,1000))
        print('priserka3 zije')
        sleep(10)
        
pohyb = threading.Thread(target=pohyb_raketa)
thread_p1 = threading.Thread(target=make_p1)
thread_p2 = threading.Thread(target=make_p2)
thread_31 = threading.Thread(target=make_p3)
