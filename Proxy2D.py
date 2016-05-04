# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from java.awt import Color
from java.lang import Math

from pythonfrp.Engine import *
from Globals2D import *
from Shapes import *
from pythonfrp.Numerics import *
from pythonfrp.Color import *
from java.awt import Graphics
from java.awt import Graphics2D
from java.awt.geom import Area
from java.awt.geom import Ellipse2D
from java.awt.geom import Rectangle2D
from java.awt.geom import AffineTransform

from jarray import array

def squarea(self, offset): #This is the default area generator. It will be overridden by certain shapes.
        return Area(Rectangle2D.Double(-offset.x, -offset.y, 1, 1))

class ScreenObject(Proxy.Proxy):
#    def __init__ (self, updater=None, types={}, name='', init=None, ** params):
#        Proxy.Proxy.__init__(self, name=name, updater=updater, types=types)
#        init(self, params)
        
    #Jay's part  
    def __init__ (self, updater = (lambda self: screenObjects.append(self)), types={}, name='', area = squarea,
    drawer = None, position = p2(0,0), zDepth = 0, zLayer = 0, color = red, gradient = None, scale = 1, height = 10, 
    width = 10, rotation = 0, texture = "None", duration = 0, center = p2(0.5,0.5),
    tp1 = p2(0, -1), tp2 = p2(1,1), tp3 = p2(-1, 1), ** params):
        Proxy.Proxy.__init__(self, name=name, updater=updater, types=types)
        self._area = area
        self._drawer = drawer
        self.position = position
        self._zLayer = zLayer
        self.zDepth = zDepth
        self.color = color
        self._gradient = gradient
        self.scale = scale
        self.height = height
        self.width = width
        self.rotation = rotation
        self.texture = texture
        self.duration = duration
        self.center = center
        self.tp1 = tp1
        self.tp2 = tp2
        self.tp3 = tp3
        if duration > 0:
            react(self, delay(duration), exitScene)
        #self.gradientInfo = gradientInfo
        #print "Hello world!"
        
    def _draw(self, g):
        self._drawer(self, g)
        
    def getCollisionVector(self, object):
        pass #To be dicided by its subclasses
    
    def _applyTexture(self, method):
        pass #A placeholder pass.  I'm not sure if the method could be generizable or if it will have to be handled by each shape individually.
    #A crop won't, but if we want to stretch/compress the image to fit...we may.
    
    def update(self):
        print("UPDOOT") # I don't think this is ever called. Ever.
        screenObjects.append(self);
        if self.duration > 0:
            print("REMOFE")
            react(self, delay(duration), exitScene)
            
    def _getArea(self):
        h = int((self._get("scale") * self._get("height")))
        w = int((self._get("scale") * self._get("width")))
        p = self._get("position")
        center = self._get("center")
        theta = self._get("rotation")
        #ar = Area(Rectangle2D.Double(-center.x, -center.y, 1, 1))
        ar = self._area(self, center)
        g = AffineTransform()
        g.translate(p.x, p.y)
        g.rotate(theta)
        g.scale(w, h)
        ar.transform(g)
        return ar
    def _touches(self, testObj, trace = False):
        if(trace):
            print("pos = " + self._get("position"))
        if(self._alive and testObj._alive):
            ar1 = self._getArea()
            ar2 = testObj._getArea()
            return ar1.intersects(ar2.getBounds2D())
        return False;
    
def _distance(o1, o2):
        return Math.sqrt(Math.pow(o2.x - o1.x,2) + Math.pow(o2.y - o1.y, 2))
        
        
def _collides(obj1, obj2):
    r1 = obj1.getCollisionVector(obj2) 
    r2 = obj2.getCollisionVector(obj1)
    #we know now where one object is relative to the other and now want to know when these points cross
    return distance(obj1.postion + r1 , obj2.postition + r2) <= 0


  
