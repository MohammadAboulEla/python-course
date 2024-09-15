import turtle

# إعداد النافذة
screen = turtle.Screen()
t = turtle.Turtle()

# تغيير سرعة السلحفاة ولون القلم
t.speed(3)  # ضبط السرعة (1 بطيء، 10 سريع)
t.color("blue")  # تغيير لون القلم إلى أزرق

# رسم مثلث
for _ in range(3):
    t.forward(100)
    t.right(120)

screen.exitonclick()
