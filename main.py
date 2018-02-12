from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

color = [ 255, 255, 255 ]

# vertical line
draw_line(250, 0, 250, 500, screen, color)

# horizontal line
draw_line(0, 250, 500, 250, screen, color)

draw_line(250, 250, 500, 400, screen, color)

# y = x & y = -x
draw_line(0, 0, 500, 500, screen, color)
draw_line(0, 500, 500, 0, screen, color)


display(screen)
save_extension(screen, 'img.png')
