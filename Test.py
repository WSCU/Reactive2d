
from Reactive2D  import *
from pythonfrp import *
from pythonfrp.Numerics import *
 


#Square(p2(25,25))
#circle(integral(mouse-p2(100,100),p2(100,100)),time*10)

pant = circle(position = p2(10,10 + time),size = 10)
bant = circle(position = p2(10,50 - time),size = 10)
#if pant._collides(bant):
#    print "yoshi"

#paddle = [p2(150,50)]
#triangle(integral(mouse-p2(100,100),p2(100,100)))
#Square(paddle[0], size = 50, skew = 0.2)

#Triangle(integral(mouse-p2(100,100),p2(100,100)))

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
 

#react(kT(), keyPressed)

start()
