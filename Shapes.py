 
#from pythonfrp.Numerics import *
#from Globals import *
from Proxy2D import *
import java.awt.Color as JavaColor
#import math.pi as pi
    


#Circle
#This user level

#J
def circle(position = p2(0,0), zDepth = 0, zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None"):
    return ScreenObject(types = {}, name = 'Circle',  drawer = drawCircle, position = position, 
        zDepth = zDepth, zLayer = zLayer, color = color, size = size, rotation = rotation, skew = skew, texture = texture)

def drawCircle(self, g):
    g.setColor(JavaColor(255,0,0))
    p = self._get("position")
    r = self._get("size")
    g.fillOval(int(p.x-r), int(p.y-r), int(2*r), int(2*r))
#A
class Circle(ScreenObject):
    def getCollisionVector(self, obj):
        directionVector = obj.position - self.position
        dist = _distance(self,obj)
        directionUnit = (directionVector.x / dist, directionVector.y / dist)
        collisionVector = directionUnit * radius
        return collisionVector




#Square

#J
def square(position = p2(0,0), zDepth = 0, zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None"):

    return ScreenObject(types = {}, name = 'Square', 
        drawer = drawSquare, position = position, 
        zDepth = zDepth, zLayer = zLayer, color = color, size = size, rotation = rotation, skew = skew, texture = texture) 

def drawSquare(self, g):
    #print("Inside drawSquare")
    g.setColor(JavaColor(0,255,0))
    p = self._get("position")
    w = self._get("size")
    h = self._get("size")
    g.fillRect(int(p.x-(w/2)), int(p.y-(h/2)), w, h)
#A
class Square(ScreenObject):
    def getCollisionVector(self, obj):
        directionVector = obj.position - self.position
        dist = _distance(self,obj)
        directionUnit = (directionVector.x / dist, directionVector.y / dist)
        collisionVector = directionUnit * width
        return collisionVector
    
 
  
  
#Triangle

#J
def triangle(position = p2(0,0), zDepth = 0, zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None"):
    return ScreenObject(types = {},
        name = 'Triangle', drawer = drawTriangle, position = position, zDepth = zDepth, 
        zLayer = zLayer, color = color, size = size, rotation = rotation, skew = skew, texture = texture)
        
def drawTriangle(self, g):
    #print("Inside drawTriangle")
    g.setColor(JavaColor(0,0,255))
    r = self._get("size");
    p = self._get("position")
    xs = array([int(p.x), int(p.x-Math.sqrt((r*r)/2)), int(p.x+Math.sqrt((r*r)/2))], 'i')
    ys = array([int(p.y-25), int(p.y+Math.sqrt((r*r)/2)), int(p.y+Math.sqrt((r*r)/2))], 'i')
    g.fillPolygon(xs, ys, 3)
 
#A
class Triangle(ScreenObject):
    def getCollisionVector(self, obj):
        directionVector = obj.position - self.position
        dist = _distance(self,obj)
        directionUnit = (directionVector.x / dist, directionVector.y / dist)
        collisionVector = directionUnit * 15
        return collisionVector
