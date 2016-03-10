 
#from pythonfrp.Numerics import *
#from Globals import *
from Proxy2D import *
import java.awt.Color as JavaColor
#import math.pi as pi
    

#On the user level, they need a consistent way to say "this is a shape"
#When making a shape, the user NEEDS to give it a position, size, and a texture (solid color is an option)
#shape(position, size, texture, (opt) stretch(es), (opt) rotation)
#zDepth, zLayer, and anything else that isn't handled by the user is handled automatically (obviously)

#To make it easier on the user, we want our coordinates to be Quadrant I of the
#   Cartesian Plane, the origin being at the bottom left of the screen.  So all
#   we have to do when the user inputs coordinates is invert the Y axis and set
#   the draw point to the height of the object.  The grab point, or position 
#   reference, will always be centered in the object.We also want them to input 
#   their rotation in degrees, so we'll need to convert those to radians if we
#   want to use them.


#Circle
class Circle(ScreenObject):
    
    def __init__(self,position = p2(0,0), zDepth = 0, zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None"):
        ScreenObject(self, types = {}, name = 'Circle', position = position, 
        zDepth = zDepth, zLayer = zLayer, color = color, size = size, rotation = rotation, skew = skew, texture = texture)

    def _draw(self,g):
        g.setColor(self.color)
        p = self._get("position")
        r = self._get("size")
        g.fillOval(int(p.x-r), int(p.y-r), int(2*r), int(2*r))
    
    def getCollisionVector(self, obj):
        directionVector = obj.position - self.position
        dist = _distance(obj)
        directionUnit = (directionVector.x / dist, directionVector.y / dist)
        collisionVector = directionUnit * radius
        return collisionVector




#Square
class Square(ScreenObject):
    
    def __init__(self,position = p2(0,0), zDepth = 0, zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None"):
        ScreenObject(self, types = {}, name = 'Square',
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
    
    def __int__(self,position = p2(0,0), zDepth = 0, zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None"):
        ScreenObject(self, types = {},
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
