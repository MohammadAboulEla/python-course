import turtle
import dpi_awareness
import colorsys


def draw_amazing_shape():
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.bgcolor("black")
    t.speed(0)
    t.width(2)

    n = 36
    hue = 0
    for i in range(360):
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        t.pencolor(color)
        t.forward(i * 3 / n + i)
        t.left(59)
        t.forward(i * 3 / n + i)
        t.left(59)
        hue += 0.005

    t.hideturtle()
    turtle.done()

draw_amazing_shape()
