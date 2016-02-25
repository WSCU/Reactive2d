
from Reactive2D  import *
from pythonfrp import *
from pythonfrp.Numerics import *
 
#circle(integral(mouse-p2(100,100),p2(100,100)),time*10)
#circle(p2(10,time*20), 10)
<<<<<<< HEAD
paddle = [p2(150,0)]
#triangle(integral(mouse-p2(100,100),p2(100,100)))
square(paddle[0])
=======
triangle(integral(mouse-p2(100,100),p2(100,100)))

>>>>>>> champstank
#def makeSquare(m,v):
#    square(p2(localTime*50+v.x,localTime*50+v.y))
    
#react(lbp(), makeSquare)
<<<<<<< HEAD

def keyPressed(self, k):
    if (k == "Left"):
        if (paddle[0].x > 20):
            paddle[0].x -= 5
    if (k == "Right"):
        if (paddle[0].x < 265):
            paddle[0].x += 5
=======
 
 #react(kT,typeKey)
>>>>>>> champstank
 
react(kT(), keyPressed)

start()