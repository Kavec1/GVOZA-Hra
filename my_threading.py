import threading
from move import *
def pohyb_raketa():
    c.bind('<Motion>', move)
pohyb = threading.Thread(target=pohyb_raketa)
