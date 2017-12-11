import threading
from move import *
def pohyb_raketa():
    c.bind('<Motion>', move_raketa)
pohyb = threading.Thread(target=pohyb_raketa)
