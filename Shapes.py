 
#from pythonfrp.Numerics import *
#from Globals import *
from Proxy2D import *
import java.awt.Color as JavaColor
#import math.pi as pi
    
def _colorToJava(c):
    jr = int(c.r * 255) 
    jg = int(c.g * 255)
    jb = int(c.b * 255)
    jc = JavaColor(jr, jg, jb)
    return jc

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

def circle(position, size = 1, texture = "None", skew = 1, rotation = 0):
    return Circle(position = position, size = size, rotation = rotation, skew = skew, texture = texture)

#Circle
class Circle(ScreenObject):
    
    def __init__(self,position = p2(0,0), zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None"):
        ScreenObject.__init__(self, types = {}, name = 'Circle', position = position, 
        zLayer = zLayer, color = color, size = size, rotation = rotation, skew = skew, texture = texture)
        #print(str(color.r))

    def _draw(self,g):
        #print(str(self._get("color")))
        c = _colorToJava(self._get("color"))
        g.setColor(c)
        p = self._get("position")
        r = self._get("size")
        g.fillOval(int(p.x-r), int(p.y-r), int(2*r), int(2*r))
    
    def _getCollisionVector(self, obj):
        pon1 = self._get("position")
        pon2 = obj._get("position")
        directionVector = pon2 - pon1
        dist = self._distance(pon1,pon2)
        directionUnit = p2(directionVector.x / dist, directionVector.y / dist)
        collisionVector = directionUnit * self.radius
        return collisionVector




#Square
class Square(ScreenObject):
    
    def __init__(self,position = p2(0,0), zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None"):
        ScreenObject(self, types = {}, name = 'Square',
        position = position, 
        zLayer = zLayer, color = color, size = size, rotation = rotation, skew = skew, texture = texture) 
    
    def _draw(self, g):
        c = _colorToJava(self._get("color"))
        g.setColor(c)
        p = self._get("position")
        w = self._get("size")
        h = self._get("size")
        g.fillRect(int(p.x-(w/2)), int(p.y-(h/2)), w, h)
    
    def getCollisionVector(self, obj):
        pon1 = self._get("position")
        pon2 = obj._get("position")
        directionVector = pon2 - pon1
        dist = _distance(pon1,pon2)
        directionUnit = p2(directionVector.x / dist, directionVector.y / dist)
        collisionVector = directionUnit * Math.max(width, height)
        return collisionVector
    
 
  
  
#Triangle
class Triangle(ScreenObject):
    
    def __int__(self,position = p2(0,0), zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None"):
        ScreenObject(self, types = {},
        name = 'Triangle', position = position, zLayer = zLayer, color = color,
        size = size, rotation = rotation, skew = skew, texture = texture)
    
    def _draw(self,g):
        c = _colorToJava(self._get("color"))
        g.setColor(c)
        r = self._get("size")
        p = self._get("position")
        xs = array([int(p.x), int(p.x-Math.sqrt((r*r)/2)), int(p.x+Math.sqrt((r*r)/2))], 'i')
        ys = array([int(p.y-25), int(p.y+Math.sqrt((r*r)/2)), int(p.y+Math.sqrt((r*r)/2))], 'i')
        g.fillPolygon(xs, ys, 3)

    def getCollisionVector(self, obj):
        pon1 = self._get("position")
        pon2 = obj._get("position")
        directionVector = pon2 - pon1
        dist = _distance(pon1,pon2)
        directionUnit = p2(directionVector.x / dist, directionVector.y / dist)
        collisionVector = directionUnit * 15
        return collisionVector
