from pythonfrp.Factory import eventObserver

#left mouse even observer
def lbp():
    return eventObserver('LeftMouseButton')

def kT():
    return eventObserver('KeyTyped')