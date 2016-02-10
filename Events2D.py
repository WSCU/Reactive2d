from pythonfrp.Factory import eventObserver

#left mouse button event observer
def lbp():
    return eventObserver('LeftMouseButton')

#---  key typed event observer  ---#
def kT():
    return eventObserver('KeyTyped')