import turtle

screen = turtle.Screen()
t = turtle.Turtle()

# تغيير لون القلم وسمك الخط
t.color("red")
t.pensize(2)

# رسم نجمة
for _ in range(5):
    t.forward(100)
    t.right(144)  # الدوران بزاوية 144 درجة

screen.exitonclick()
