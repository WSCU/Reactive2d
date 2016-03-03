 
#from pythonfrp.Numerics import *
#from Globals import *
from Proxy2D import *
import java.awt.Color as JavaColor
#import math.pi as pi
    

#This user level
#Circle
class Circle(ScreenObject):
    
    def __init__(position = p2(0,0), zDepth = 0, zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None"):
        ScreenObject(types = {}, name = 'Circle', position = position, 
        zDepth = zDepth, zLayer = zLayer, color = color, size = size, rotation = rotation, skew = skew, texture = texture)

    def _draw(self,g):
        g.setColor(self.color)
        p = self._get("position")
        r = self._get("size")
        g.fillOval(int(p.x-r), int(p.y-r), int(2*r), int(2*r))
    
    def getCollisionVector(self, obj):
        directionVector = obj.position - self.position
        dist = _distance(self,obj)
        directionUnit = (directionVector.x / dist, directionVector.y / dist)
        collisionVector = directionUnit * radius
        return collisionVector




#Square
class Square(ScreenObject):
    
    def __init__(position = p2(0,0), zDepth = 0, zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None"):
        ScreenObject(types = {}, name = 'Square',
        position = position, 
        zDepth = zDepth, zLayer = zLayer, color = color, size = size, rotation = rotation, skew = skew, texture = texture) 
    
    def _draw(self, g):
        #print("Inside drawSquare")
        g.setColor(self.color)
        p = self._get("position")
        w = self._get("size")
        h = self._get("size")
        g.fillRect(int(p.x-(w/2)), int(p.y-(h/2)), w, h)
    
    def getCollisionVector(self, obj):
        directionVector = obj.position - self.position
        dist = _distance(self,obj)
        directionUnit = (directionVector.x / dist, directionVector.y / dist)
        collisionVector = directionUnit * width
        return collisionVector
    
 
  
  
#Triangle
class Triangle(ScreenObject):
    
    def __int__(position = p2(0,0), zDepth = 0, zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None"):
        ScreenObject(types = {},
        name = 'Triangle', position = position, zDepth = zDepth, 
        zLayer = zLayer, color = color, size = size, rotation = rotation, skew = skew, texture = texture)
    
    def _draw(self,g):
        #print("Inside drawTriangle")
        g.setColor(self.color)
        r = self._get("size");
        p = self._get("position")
        xs = array([int(p.x), int(p.x-Math.sqrt((r*r)/2)), int(p.x+Math.sqrt((r*r)/2))], 'i')
        ys = array([int(p.y-25), int(p.y+Math.sqrt((r*r)/2)), int(p.y+Math.sqrt((r*r)/2))], 'i')
        g.fillPolygon(xs, ys, 3)
    
    def getCollisionVector(self, obj):
        directionVector = obj.position - self.position
        dist = _distance(self,obj)
        directionUnit = (directionVector.x / dist, directionVector.y / dist)
        collisionVector = directionUnit * 15
        return collisionVector
