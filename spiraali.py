from turtle import *
def draw_spiral(line_color, arcs, r, r_growth, pen=1):
    if pen==False:
        pen=1
    up()
    color(line_color)
    pensize(pen)
    down()
    for i in range(arcs):
        circle(r,90)
        r+=r_growth
    up()
  

draw_spiral("black", 20, 10, 3)
draw_spiral("red", 10, 20, 4, 3)
draw_spiral("blue", 10, -20, -4, 3)
done()