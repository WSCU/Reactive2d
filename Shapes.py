# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#from pythonfrp.Numerics import *
#from Globals import *
from Proxy2D import *
    
def circle(position, radius = 20):
    return ScreenObject(updater = circleUpdate, types = {"position": p2Type,
        "radius": numType}, name = 'Circle', init = circleInit, position = position,
        radius = radius)

def square(position, height = 20, width = 40):
    return ScreenObject(updater = squareUpdater, types = {"position": p2Type,
        "width": numType, "height": numType}, name = 'Square', init = squareInit,
        position = position, width = width, height = height)

def triangle(position):
    return ScreenObject(updater = triangleUpdater, types = {"position": p2Type},
        name = 'Triangle', init = triangleInit, position = position)