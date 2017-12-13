from init import *

x=[0,0]
y=[0,0]
def move_raketa(udalost): #funkcia, ktora pohybuje objektom na zaklade pozicie mysi
    x[0]=udalost.x
    y[0]=udalost.y
    print(str(x),str(y))    
    print(str(x[1]-x[0]),str(y[1]-y[0]))
    c.move('raketa', -(x[1]-x[0]), -(y[1]-y[0]))
    x[1]=x[0]
    y[1]=y[0]

def vystrel(suradnice):
    a= suradnice.x
    b= suradnice.y
    c.create_line(a+5,b-20,a+5,0, fill='yellow', tags='strela', width=5)
