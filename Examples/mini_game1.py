# استيراد مكتبة السلحفاة
import turtle

# إنشاء نافذة الرسم
win = turtle.Screen()
win.bgcolor("black")

# إنشاء كائن السلحفاة
t = turtle.Turtle()
# turtle.colormode(255)  # Enable RGB mode (0-255)
t.shape("circle")
t.shape("turtle")
t.color("red")
t.speed(0)
t.width(2)
t.penup()

# إنشاء كائن السلحفاة
t2 = turtle.Turtle()
# turtle.colormode(255)  # Enable RGB mode (0-255)
t2.shape("circle")
t2.shape("turtle")
t2.color("blue")
t2.penup()
t2.goto(0, 100)
t2.speed(0)
t2.width(2)


def go_left(t):
    t.setheading(180)
    t.forward(10)


def go_right(t):
    t.setheading(0)
    t.forward(10)


def go_up(t):
    t.setheading(90)
    t.forward(10)


def go_down(t):
    t.setheading(-90)
    t.forward(10)


def set_pen_down(t):
    t.pendown()


def set_pen_up(t):
    t.setheading(0)
    t.penup()


# Keyboard bindings
win.listen()
win.onkeypress(lambda: go_up(t), "Up")
win.onkeypress(lambda: go_down(t), "Down")
win.onkeypress(lambda: go_left(t), "Left")
win.onkeypress(lambda: go_right(t), "Right")
win.onkeypress(lambda: set_pen_down(t), "space")
win.onkeyrelease(lambda: set_pen_up(t), "space")

# Keyboard bindings
win.listen()
win.onkeypress(lambda: go_up(t2), "w")
win.onkeypress(lambda: go_down(t2), "s")
win.onkeypress(lambda: go_left(t2), "a")
win.onkeypress(lambda: go_right(t2), "d")
win.onkeypress(lambda: set_pen_down(t2), "x")
win.onkeyrelease(lambda: set_pen_up(t2), "x")

# إنهاء الرسم وإغلاق النافذة عند النقر
win.exitonclick()
