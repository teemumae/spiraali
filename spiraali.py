from turtle import *
def draw_spiral(color, arcs, r, r_growth, pen):
    if pen==False:
        pen=1
    up()
    color(color)
    pensize(pen)
    down()
    for i in arcs:
        circle(r,90)
        r+=r_growth
    up()
  

#draw_spiral("black", 20, 10, 3)
draw_spiral("red", 10, 20, 4, 3)
draw_spiral("blue", 10, -20, -4, 3)
done()