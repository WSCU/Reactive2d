
from java.awt import Color
from java.lang import Math
from pythonfrp.Engine import *
from Globals2D import *
from Shapes import *
from pythonfrp.Numerics import *
from pythonfrp.Color import *
from jarray import array



class ScreenObject(Proxy.Proxy):

 
    def __init__ (self, updater = (lambda self: screenObjects.append(self)), types={}, name='', position = p2(0,0), zLayer = 0, color = red, size = 10, rotation = 0, skew = 1, texture = "None", ** params):
        Proxy.Proxy.__init__(self, name=name, updater=updater, types=types)
        self.position = position
        self.zLayer = zLayer
        self.color = color
        self.size = size
        self.rotation = rotation
        self.skew = skew
        self.texture = texture
        self._updater = updater
#        self.x = self._get("position").x
#        self.y = self._get("position").y
        #print "Hello world!"
        
    def _draw(self, g):
        pass #Every Screenobject should know how to draw itself.  It doesn't need a drawer, that's just weird and unnecessary delegation
        
    def _getCollisionVector(self, object):
        pass #To be dicided by its subclasses
    
    def _applyTexture(self, method):
        pass #A placeholder pass.  I'm not sure if the method could be generizable or if it will have to be handled by each shape individually.
    #A crop won't, but if we want to stretch/compress the image to fit...we may.
    
    def update(self):
        screenObjects.append(self);
        
    def _distance(self,p1, p2):
        return Math.sqrt(Math.pow(p2.x - p1.x,2) + Math.pow(p2.y - p1.y, 2))
        
        
    def _collides(self, obj2):
        r1 = self._getCollisionVector(obj2) 
        r2 = obj2._getCollisionVector(self)
        #we know now where one object is relative to the other and now want to know when these points cross
        return self._distance(self.postion + r1 , obj2.postition + r2) <= 0


