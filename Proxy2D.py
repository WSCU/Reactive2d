# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from java.awt import Color
from java.lang import Math

import pythonfrp.Proxy as Proxy
from pythonfrp.Numerics import *
from Globals2D import *

from jarray import array

class ScreenObject(Proxy.Proxy):
    def __init__ (self, updater = None, types = {}, name = '', init = None, **params):
        Proxy.Proxy.__init__(self, name = name, updater = updater, types = types)
        init(self, params)
#        print('Created Object')