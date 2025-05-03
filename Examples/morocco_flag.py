import turtle

def draw_rectangle():
    pen.begin_fill()
    pen.color("red")
    for _ in range(2):
        pen.forward(600)
        pen.right(90)
        pen.forward(400)
        pen.right(90)
    pen.end_fill()

def draw_star(size):
    pen.color("green")
    pen.pensize(5)
    pen.penup()
    pen.goto(-size / 2, size / 3)
    pen.pendown()
    for _ in range(5):
        pen.forward(size)
        pen.right(144)

# Set up the screen
screen = turtle.Screen()
screen.title("Moroccan Flag")
screen.bgcolor("white")

# Set up the turtle
pen = turtle.Turtle()
pen.speed(5)

# Draw the flag's red background
pen.penup()
pen.goto(-300, 200)
pen.pendown()
draw_rectangle()

# Draw the green pentagram in the center
pen.penup()
pen.goto(0, 0)
pen.pendown()
draw_star(200)

# Hide the turtle and display the flag
pen.hideturtle()
screen.mainloop()
