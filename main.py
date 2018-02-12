from display import *
from draw import *

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


display(screen)
save_extension(screen, 'img.png')
