 
#from pythonfrp.Numerics import *
#from Globals import *
from Proxy2D import *
import java.awt.Color as JavaColor
#import math.pi as pi
    


#Circle
#This user level
<<<<<<< HEAD
def circle(position = p2(0,0), zDepth = 0, zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None"):
    return ScreenObject(types = {}, name = 'Circle',  drawer = drawCircle, position = position, 
        zDepth = zDepth, zLayer = zLayer, color = color, size = size, rotation = rotation, skew = skew, texture = texture)
<<<<<<< HEAD

=======
=======
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
 
>>>>>>> cb742e697533f3b10b53fe786730188aa6a7b525
#Reactive Stuff
def circleInit(so, params):
    so.position = params["position"]
    so.radius = params["radius"]

<<<<<<< HEAD
#Gets the things that are requried to draw a circle
def circleUpdate(self):
 
    screenObjects.append(self)
=======


#Gets the things that are requried to draw a circle
def circleUpdate(self):
#    positionNow = self._get("position")
#    radiusNow = self._get("radius")
#    print('Positiong Now:' + str(positionNow))
# This is what makes the circle visible.  The draw code (a function that takes a graphics object) is placed
# in the screenObjects list
    #screenObjects.append(lambda g: drawCircle(g, positionNow, radiusNow))
    screenObjects.append(self)
>>>>>>> origin/PseudoMaster
>>>>>>> cb742e697533f3b10b53fe786730188aa6a7b525
    


#Circle Drawing code
 
def drawCircle(self, g):
    g.setColor(JavaColor(255,0,0))
    p = self._get("position")
    r = self._get("size")
    g.fillOval(int(p.x-r), int(p.y-r), int(2*r), int(2*r))

#Square
class Square(ScreenObject):
    def getCollisionVector(self, obj):
        directionVector = obj.position - self.position
        dist = _distance(self,obj)
        directionUnit = (directionVector.x / dist, directionVector.y / dist)
        collisionVector = directionUnit * width
        return collisionVector
    
    
    
    

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> cb742e697533f3b10b53fe786730188aa6a7b525
def square(position = p2(0,0), zDepth = 0, zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None"):
=======
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
    
>>>>>>> origin/PseudoMaster
    
    return ScreenObject(types = {}, name = 'Square', 
        drawer = drawSquare, position = position, 
        zDepth = zDepth, zLayer = zLayer, color = color, size = size, rotation = rotation, skew = skew, texture = texture) 

 

 
def squareInit(so, params):
    so.position = params["position"]
    so.width = params["width"]
    so.height = params["height"]
   
 
def squareUpdater(self):
    screenObjects.append(self)
    
     
def drawSquare(self, g):
    #print("Inside drawSquare")
    g.setColor(JavaColor(0,255,0))
    p = self._get("position")
    w = self._get("size")
    h = self._get("size")
    g.fillRect(int(p.x-(w/2)), int(p.y-(h/2)), w, h) 
 
    
#Triangle
<<<<<<< HEAD
def triangle(position = p2(0,0), zDepth = 0, zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None"):
    return ScreenObject(types = {},
        name = 'Triangle', drawer = drawTriangle, position = position, zDepth = zDepth, 
        zLayer = zLayer, color = color, size = size, rotation = rotation, skew = skew, texture = texture)
        

def triangleInit(so, params):
    so.position = params["position"]

def triangleUpdater(self):
    screenObjects.append(self)
 
=======
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
>>>>>>> origin/PseudoMaster
def drawTriangle(self, g):
    #print("Inside drawTriangle")
    g.setColor(JavaColor(0,0,255))
    r = self._get("size");
    p = self._get("position")
    xs = array([int(p.x), int(p.x-Math.sqrt((r*r)/2)), int(p.x+Math.sqrt((r*r)/2))], 'i')
    ys = array([int(p.y-25), int(p.y+Math.sqrt((r*r)/2)), int(p.y+Math.sqrt((r*r)/2))], 'i')
    g.fillPolygon(xs, ys, 3)