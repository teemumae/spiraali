from turtle import *
def draw_spiral(color, arcs, r, r_growth, pen):
    up()
    color(color)
    pensize(pen)
    down()
    for i in arcs:

    up()

draw_spiral("black", 20, 10, 3)
draw_spiral("red", 10, 20, 4, 3)
draw_spiral("blue", 10, -20, -4, 3)