from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    
    
    #find out which of the 4 quadrants it falls under
    dx = x1 - x0
    dy = y1 - y0

    if (dx < 0):
        #limits us to quadrants 1 - 4
        draw_line( x1, y1, x0, y0, screen, color)
        return

    if (dx == 0):
        #vertical line
        draw_vertical( x0, y0, y1, screen, color)
        return

    if (dy == 0):
        #horizontal line
        draw_horizontal( y0, x0, x1, screen, color)
        return

    if (dy > 0):
        if (dx > dy):
            quadrant = 1
        else:
            quadrant = 2
    else:
        if (dy*-1 < dx):
            quadrant = 8
        else:
            quadrant = 7

    draw(x1, y1, x0, y0, screen, color, quadrant)


def draw ( x0, y0, x1, y1, octant, screen, color):
    A = y1 - y0
    B = -1*(x1 - x0)
    #Octant 1 and 5, slope is less than 1 but greater than 0
    if (octant == 1):
        x = x0
        y = y0
        d = 2*A + B
        while (x <= x1):
            plot(x,y)
            if (d > 0):
                y += 1
                d += 2*B
            x += 1
            d += 2*A
        return
    
    #Octant 2 and 6, slope is greater than 1
    if (octant == 2):
        pass
    #Octant 3 and 7, slope is less than -1
    if (octant == 7):
        pass
    #Octant 4 and 8, slope is less than 0 but greater than -1
    if (octant == 8):
        pass

def draw_vertical( x, y0, y1, screen, color):
    for i in range( y1 - y0 ):
        plot(screen, color, x, y0 + i)

def draw_horizontal( y, x0, x1, screen, color):
    for i in range( x1 - x0 ):
        plot(screen, color, x0 + i, y)
