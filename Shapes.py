# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
 
#from pythonfrp.Numerics import *
#from Globals import *
from Proxy2D import *
#import math.pi as pi
    


#Circle
#This user level
def circle(position, radius = 20):
    return ScreenObject(updater = circleUpdate, types = {"position": p2Type,
        "radius": numType}, name = 'Circle', init = circleInit, position = position,
<<<<<<< Updated upstream
        radius = radius)    #ScreenObject class in Reactive2D Proxy2D.py && Types-variables in pythonfrp Types.py
=======
<<<<<<< HEAD
        radius = radius)

=======
        radius = radius)    #ScreenObject class in Reactive2D Proxy2D.py && Types-variables in pythonfrp Types.py
>>>>>>> 16b3d35c35e5e93a522da9ed93bcd79ef2685acf
>>>>>>> Stashed changes
#Reactive Stuff
def circleInit(so, params):
    so.position = params["position"]
    so.radius = params["radius"]

#Gets the things that are requried to draw a circle
def circleUpdate(self):
    positionNow = self._get("position")
    radiusNow = self._get("radius")
#    print('Positiong Now:' + str(positionNow))
# This is what makes the circle visible.  The draw code (a function that takes a graphics object) is placed
# in the screenObjects list
    screenObjects.append(lambda g: drawCircle(g, positionNow, radiusNow))
    


#Circle Drawing code
def drawCircle(g, p, r):
    g.setColor(Color(255,0,0))
    g.fillOval(int(p.x-r), int(p.y-r), 2*r, 2*r)


#Square
def square(position, height = 20, width = 40):
    return ScreenObject(updater = squareUpdater, types = {"position": p2Type,
        "width": numType, "height": numType}, name = 'Square', init = squareInit,
        position = position, width = width, height = height)

def squareInit(so, params):
    so.position = params["position"]
    so.width = params["width"]
    so.height = params["height"]

def squareUpdater(self):
    positionNow = self._get("position")
    heightNow = self._get("height")
    widthNow = self._get("width")
    screenObjects.append(lambda g: drawSquare(g, positionNow, heightNow, widthNow))

def drawSquare(g, p, h, w):
    g.setColor(Color(0,255,0))
    g.fillRect(int(p.x-(h/2)), int(p.y-(w/2)), w, h) 
    
#Triangle
def triangle(position):
    return ScreenObject(updater = triangleUpdater, types = {"position": p2Type},
        name = 'Triangle', init = triangleInit, position = position)
def triangleInit(so, params):
    so.position = params["position"]
def triangleUpdater(self):
    positionNow = self._get("position")
    screenObjects.append(lambda g: drawTriangle(g, positionNow))
def drawTriangle(g, p):
    r = 15;
    g.setColor(Color(0,0,255))
    xs = array([int(p.x), int(p.x-Math.sqrt((r*r)/2)), int(p.x+Math.sqrt((r*r)/2))], 'i')
    ys = array([int(p.y-25), int(p.y+Math.sqrt((r*r)/2)), int(p.y+Math.sqrt((r*r)/2))], 'i')
#    print("P1" + str(xs[0]) + ", " + str(ys[0]))
#    print("P2" + str(xs[1]) + ", " + str(ys[1]))
#    print("P3" + str(xs[2]) + ", " + str(ys[2]))
    g.fillPolygon(xs, ys, 3)