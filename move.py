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

def vystrel(suradnice): #funkcia, ktora vykresli strelu (zltu ciaru)
	a=suradnice.x
	b=suradnice.y
	global hitbox
	i=b-20
	while hitbox[i][a+5]==0:
		if i==0:
			break
		i-=1
	print('strela:'+str(i))
	print(str(hitbox[i][a+5]))
	c.delete('p'+str(hitbox[i][a+5]))
	c.create_line(a+5,b-20,a+5,i-10, fill='yellow', tag='strela', width=5)
	#del_strela.start()
	for j in range(a-20,a+20):
		hitbox[i][j]=int(0)

from my_threading import *
