
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
#square(paddle[0], scale = 100, skew = 0.2, zLayer = 2, color = black, rotation = 0.2, gradientInfo = [paddleGradStart[0], red, paddleGradEnd[0], blue])
#square(paddle2[0], scale = 100, skew = 0.2, zLayer = 2, color = black, rotation = 0, gradientInfo = [paddleGradStart[0], red, paddleGradEnd[0], blue])
#square(paddle3[0], scale = 100, skew = 0.2, zLayer = 2, color = black, rotation = -0.2)

#circle(integral(mouse-p2(100,100),p2(100,100)), scale = 50, skew  = 2, zLayer = 1)
gp1 = p2(-cos(-localTime)/2 + 0.5, -sin(-localTime)/2+ 0.5)
gp2 = p2(cos(-localTime)/2 + 0.5, sin(-localTime)/2 + 0.5)
trp1 = p2(0, -(cos(localTime) + 1) / 4)
trp2 = p2((sin(localTime*3) + 1) / 4, 1)
trp3 = p2(-(sin(localTime*2) + 1) / 4, 1)

c1 = circle(mouse, height = 20, width = 50, zLayer = 3, zDepth = sin(localTime), color = black, rotation = (localTime), useGrad = True, gradp1 = gp1, gradp2 = gp2, gradc1 = red, gradc2 = blue, center = gp1)
s1 = square(p2(100,100), height = 20, width = 80, zLayer = 3, color = black, rotation = (localTime), useGrad = True, gradp1 = p2(-1,0), gradp2 = p2(1,0), gradc1 = red, gradc2 = blue, duration = 3)
#square(p2(30, 100), scale = 50, skew = 0.5, zLayer = 3, color = black, rotation = 0, useGrad = True, gradp1 = gp1, gradp2 = gp2, gradc1 = red, gradc2 = blue)
c2 = circle(p2(30, 100), scale = 1, height = 20, width = 50, zLayer = 3, color = black, rotation = (localTime), useGrad = True, gradp1 = gp1, gradp2 = gp2, gradc1 = red, gradc2 = blue, duration = 10)

#imgS = square(p2(100,100), height = 50, width = 50, texture = "img.jpg")
t1 = triangle(p2(150,150), height = 50, width = 50, tp1 = trp1, tp2 = trp2, tp3 = trp3)
img1 = image(texture = "C:\\Users\\stu598041\\Desktop\\img.jpg", position = p2(180,50), width = 30, height = 50, rotation = localTime)
#circle(p2(100,100), scale = 50, skew = 1, zLayer = 2, color = black, rotation = (localTime), useGrad = True, gradp1 = gp1, gradp2 = gp2, gradc1 = Color(abs(sin(localTime)), 0, 0), gradc2 = Color(0, abs(cos(localTime)), abs(cos(localTime))))

#react(c1, delay(5), exitScene)
#react(s1, touches(s1, s2), exitScene)
#def makeSquare(m,v):
#    square(p2(localTime*50+v.x,localTime*50+v.y))
hit(c1, s1, exitScene)
    
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