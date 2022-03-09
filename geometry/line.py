def distance(x1,y1,x2,y2):
    x = ((x2-x1**2+(y2-y1)**2))**0.5 
    return x

def slope(x1,y1,x2,y2):
    n = (y2-y1)/(x2-x1) 
    return n