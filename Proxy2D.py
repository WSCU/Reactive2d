
from java.awt import Color
from java.lang import Math
from pythonfrp.Engine import *
from Globals2D import *
from Shapes import *
from pythonfrp.Numerics import *
from pythonfrp.Color import *
from jarray import array

class ScreenObject(Proxy.Proxy):
 
    def __init__ (self, updater = (lambda self: screenObjects.append(self)), types={}, name='', position = p2(0,0), zDepth = 0, zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None", ** params):
        Proxy.Proxy.__init__(self, name=name, updater=updater, types=types)
        self.position = position
        self._zDepth = zDepth
        self._zLayer = zLayer
        self.color = color
        self.size = size
        self.rotation = rotation
        self.skew = skew
        self.texture = texture
        #print "Hello world!"
        
    def _draw(self, g):
        pass #Every Screenobject should know how to draw itself.  It doesn't need a drawer, that's just weird and unnecessary delegation
        
    def getCollisionVector(self, object):
        pass #To be dicided by its subclasses
    
    def _applyTexture(self, method):
        pass #A placeholder pass.  I'm not sure if the method could be generizable or if it will have to be handled by each shape individually.
    #A crop won't, but if we want to stretch/compress the image to fit...we may.
    
    def update(self):
        screenObjects.append(self);

def _distance(o1, o2):
        return Math.sqrt(Math.pow(o2.x - o1.x,2) + Math.pow(o2.y - o1.y, 2))
        
        
def _collides(obj1, obj2):
    r1 = obj1.getCollisionVector(obj2) 
    r2 = obj2.getCollisionVector(obj1)
    #we know now where one object is relative to the other and now want to know when these points cross
    return distance(obj1.postion + r1 , obj2.postition + r2) <= 0