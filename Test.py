
from Reactive2D  import *
from pythonfrp import *
from pythonfrp.Numerics import *
from pythonfrp.Color import *
 

square(p2(25,25))
#circle(integral(mouse-p2(100,100),p2(100,100)),time*10)
#circle(p2(10,time*20), 10)

paddle = [p2(150,50)]
paddle2 = [p2(150,100)]
paddle3 = [p2(150,150)]
paddleGradStart = [p2(100,50)]
paddleGradEnd = [p2(200,50)]
#triangle(integral(mouse-p2(100,100),p2(100,100)))
#square(paddle[0], size = 100, skew = 0.2, zLayer = 2, color = black, rotation = 0.2, gradientInfo = [paddleGradStart[0], red, paddleGradEnd[0], blue])
#square(paddle2[0], size = 100, skew = 0.2, zLayer = 2, color = black, rotation = 0, gradientInfo = [paddleGradStart[0], red, paddleGradEnd[0], blue])
#square(paddle3[0], size = 100, skew = 0.2, zLayer = 2, color = black, rotation = -0.2)

#circle(integral(mouse-p2(100,100),p2(100,100)), size = 50, skew  = 2, zLayer = 1)
gp1 = p2(-cos(-localTime), -sin(-localTime))
gp2 = p2(cos(-localTime), sin(-localTime))

square(mouse, size = 50, skew = 0.5, zLayer = 3, zDepth = sin(localTime), color = black, rotation = (localTime), useGrad = True, gradp1 = gp1, gradp2 = gp2, gradc1 = red, gradc2 = blue)
square(p2(100,100), size = 50, skew = 0.5, zLayer = 3, color = black, rotation = (localTime), useGrad = True, gradp1 = p2(-1,0), gradp2 = p2(1,0), gradc1 = red, gradc2 = blue)
#square(p2(30, 100), size = 50, skew = 0.5, zLayer = 3, color = black, rotation = 0, useGrad = True, gradp1 = gp1, gradp2 = gp2, gradc1 = red, gradc2 = blue)
circle(p2(30, 100), size = 50, skew = 0.5, zLayer = 3, color = black, rotation = (localTime), useGrad = True, gradp1 = gp1, gradp2 = gp2, gradc1 = red, gradc2 = blue)

#circle(p2(100,100), size = 50, skew = 1, zLayer = 2, color = black, rotation = (localTime), useGrad = True, gradp1 = gp1, gradp2 = gp2, gradc1 = Color(abs(sin(localTime)), 0, 0), gradc2 = Color(0, abs(cos(localTime)), abs(cos(localTime))))


#def makeSquare(m,v):
#    square(p2(localTime*50+v.x,localTime*50+v.y))
    
#react(lbp(), makeSquare)

def keyPressed(self, k):
    if (k == "Left"):
        #print "Going left!"
        if (paddle[0].x > 20):
            paddle[0].x -= 5
            paddleGradStart[0].x -= 5
            paddleGradEnd[0].x -= 5
            #print str(paddle[0].x)
    if (k == "Right"):
        if (paddle[0].x < 265):
            paddle[0].x += 5
            paddleGradStart[0].x += 5
            paddleGradEnd[0].x += 5
 
 #react(kT,typeKey)
 
react(kT(), keyPressed)

start()