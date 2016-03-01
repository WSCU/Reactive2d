
from Reactive2D  import *
from pythonfrp import *
from pythonfrp.Numerics import *
 

square(p2(25,25))
#circle(integral(mouse-p2(100,100),p2(100,100)),time*10)
#circle(p2(10,time*20), 10)

paddle = [p2(150,50)]
#triangle(integral(mouse-p2(100,100),p2(100,100)))
square(paddle[0], size = 50, skew = 0.2)

triangle(integral(mouse-p2(100,100),p2(100,100)))


#def makeSquare(m,v):
#    square(p2(localTime*50+v.x,localTime*50+v.y))
    
#react(lbp(), makeSquare)

def keyPressed(self, k):
    if (k == "Left"):
        #print "Going left!"
        if (paddle[0].x > 20):
            paddle[0].x -= 5
            #print str(paddle[0].x)
    if (k == "Right"):
        if (paddle[0].x < 265):
            paddle[0].x += 5
 
 #react(kT,typeKey)
 
react(kT(), keyPressed)

start()