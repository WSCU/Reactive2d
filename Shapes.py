# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
 
#from pythonfrp.Numerics import *
#from Globals import *
from Proxy2D import *
#import math.pi as pi
    


#Circle
#This user level
class Circle(ScreenObject):
    def getCollisionVector(self, obj):
        directionVector = obj.position - self.position
        dist = _distance(self,obj)
        directionUnit = (directionVector.x / dist, directionVector.y / dist)
        collisionVector = directionUnit * radius
        return collisionVector




def circle(position, radius = 20):
    return ScreenObject(updater = circleUpdate, types = {"position": p2Type,
        "radius": numType}, name = 'Circle', init = circleInit, drawer = drawCircle, position = position,  
        radius = radius)
 
#Reactive Stuff
def circleInit(so, params):
    so.position = params["position"]
    so.radius = params["radius"]



#Gets the things that are requried to draw a circle
def circleUpdate(self):
#    positionNow = self._get("position")
#    radiusNow = self._get("radius")
#    print('Positiong Now:' + str(positionNow))
# This is what makes the circle visible.  The draw code (a function that takes a graphics object) is placed
# in the screenObjects list
    #screenObjects.append(lambda g: drawCircle(g, positionNow, radiusNow))
    screenObjects.append(self)
    


#Circle Drawing code
#def drawCircle(g, p, r):
#    g.setColor(Color(255,0,0))
#    g.fillOval(int(p.x-r), int(p.y-r), int(2*r), int(2*r))
def drawCircle(self, g):
    g.setColor(Color(255,0,0))
    p = self._get("position")
    r = self._get("radius")
    g.fillOval(int(p.x-r), int(p.y-r), int(2*r), int(2*r))

#Square
class Square(ScreenObject):
    def getCollisionVector(self, obj):
        directionVector = obj.position - self.position
        dist = _distance(self,obj)
        directionUnit = (directionVector.x / dist, directionVector.y / dist)
        collisionVector = directionUnit * width
        return collisionVector
    
    
    
    

def square(position, height = 20, width = 40):
    
#    return ScreenObject(updater = squareUpdater, types = {"position": p2Type,
#        "width": numType, "height": numType}, name = 'Square', init = squareInit,
#        position = position, width = width, height = height
    return ScreenObject(updater = squareUpdater, types = {"position": p2Type,
        "width": numType, "height": numType}, name = 'Square', init = squareInit,
        drawer = drawSquare, position = position, width = width, height = height) 

#----------------------------------------------------------------------------------------------------------#       
def bounding_box(self):
    print "start bounding box"
    
    
    bottomLeft = SP2(self._get("position")-self._get("width")/2, self._get("position")-self._get("height")/2)
    bottomRight = SP2(self._get("position")+self._get("width")/2, self._get("position")-self._get("height")/2)
    topRight = SP2(self._get("position")+self._get("width")/2, self._get("position")+self._get("height")/2)
    topLeft = SP2(self._get("position")-self._get("width")/2, self._get("position")+self._get("height")/2)
    
    
#    so.bottomLeft = p2(params["position"]-params["width"]/2, params["position"]-params["height"]/2)
#    so.bottomRight = p2(params["position"]+params["width"]/2, params["position"]-params["height"]/2)
#    so.topRight = p2(params["position"]+params["width"]/2, params["position"]+params["height"]/2)
#    so.topLeft = p2(params["position"]-params["width"]/2, params["position"]-params["height"]/2)
#    print "end bounding box"
    print "bottom left:  " + str(bottomLeft)  + "     bottom right:  " + str(bottomRight) + "     top left:  " + str(topLeft) + "top right:  " + str(topRight)
#----------------------------------------------------------------------------------------------------------#

def squareInit(so, params):
    so.position = params["position"]
    so.width = params["width"]
    so.height = params["height"]

   

#def squareUpdater(self): 
#    positionNow = self._get("position")
#    heightNow = self._get("height")
#    widthNow = self._get("width") 
#    screenObjects.append(lambda g: drawSquare(g, positionNow, heightNow, widthNow))
def squareUpdater(self):
    screenObjects.append(self)
    
    

#def drawSquare(g, p, h, w):
#    g.setColor(Color(0,255,0))
#    g.fillRect(int(p.x-(h/2)), int(p.y-(w/2)), w, h) #Why were we subtracting height from x and width from y?
def drawSquare(self, g):
    #print("Inside drawSquare")
    g.setColor(Color(0,255,0))
    p = self._get("position")
    w = self._get("width")
    h = self._get("height")
    g.fillRect(int(p.x-(w/2)), int(p.y-(h/2)), w, h) 
#    g.fillRect(int(self._get("position").x - (self._get("width") / 2)), int(self._get("position").y - (self._get("height") / 2)), int(self._get("width")), int(self._get("height")))
#    Long and dumb!
    
#Triangle
class Triangle(ScreenObject):
    def getCollisionVector(self, obj):
        directionVector = obj.position - self.position
        dist = _distance(self,obj)
        directionUnit = (directionVector.x / dist, directionVector.y / dist)
        collisionVector = directionUnit * 15
        return collisionVector






def triangle(position):
    return ScreenObject(updater = triangleUpdater, types = {"position": p2Type},
        name = 'Triangle', init = triangleInit, drawer = drawTriangle, position = position)
def triangleInit(so, params):
    so.position = params["position"]
    
def triangleUpdater(self):
    screenObjects.append(self)
#def drawTriangle(g, p):
#    r = 15;
#    g.setColor(Color(0,0,255))
#    xs = array([int(p.x), int(p.x-Math.sqrt((r*r)/2)), int(p.x+Math.sqrt((r*r)/2))], 'i')
#    ys = array([int(p.y-25), int(p.y+Math.sqrt((r*r)/2)), int(p.y+Math.sqrt((r*r)/2))], 'i')
##    print("P1" + str(xs[0]) + ", " + str(ys[0]))
##    print("P2" + str(xs[1]) + ", " + str(ys[1]))
##    print("P3" + str(xs[2]) + ", " + str(ys[2]))
#    g.fillPolygon(xs, ys, 3)
def drawTriangle(self, g):
    #print("Inside drawTriangle")
    g.setColor(Color(0,0,255))
    r = 15;
    p = self._get("position")
    xs = array([int(p.x), int(p.x-Math.sqrt((r*r)/2)), int(p.x+Math.sqrt((r*r)/2))], 'i')
    ys = array([int(p.y-25), int(p.y+Math.sqrt((r*r)/2)), int(p.y+Math.sqrt((r*r)/2))], 'i')
    g.fillPolygon(xs, ys, 3)