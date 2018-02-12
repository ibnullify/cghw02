from display import *
from draw import *
import random
screen = new_screen()
#color = [ 0, 255, 0 ]

color = [ 255, 255, 255 ] #white

# vertical line
draw_line(250, 0, 250, 500, screen, color)

# horizontal line
draw_line(0, 250, 500, 250, screen, color)

# y = x
draw_line(0, 0, 500, 500, screen, color)

# y = -x
draw_line(0, 500, 500, 0, screen, color)



color = [ 0, 255, 0 ] #green

# quadrant 1 & quadrant 5
draw_line(250, 250, 500, 400, screen, color)

draw_line(250, 250, 0, 100, screen, color)



color = [ 225, 0, 0 ] #red

# quadrant 2 & quadrant 6
draw_line(250, 250, 400, 500, screen, color)

draw_line(250, 250, 100, 0, screen, color)


color = [ 0, 0, 255 ] #blue

# quadrant 3 & quadrant 7
draw_line(250, 250, 100, 500, screen, color)

draw_line(250, 250, 400, 0, screen, color)


color = [ 255, 0, 255 ] #purple

# quadrant 4 & quadrant 8
draw_line(250, 250, 500, 100, screen, color)

draw_line(250, 250, 0, 400, screen, color)



def draw_from(xcor,ycor,density):
    x = 0
    y = 0
    while (x <= 500):
        while (y <= 500):
            #print x,y
            color = [ random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
            draw_line(xcor, ycor, x, y, screen, color)
            y += density
        x += density
        y = 0;

draw_from(0,0,50);
draw_from(0,500,50);
draw_from(500,0,50);
draw_from(500,500,50);
    

'''
for x in range(1,501):
    for y in range(1,501):
        print x,y
        color = [ random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        draw_line(250, 250, x, y, screen, color)
'''

display(screen)
save_extension(screen, 'img.png')
