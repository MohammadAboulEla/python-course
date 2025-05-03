# استيراد مكتبة السلحفاة
import turtle
import dpi_awareness

# إنشاء نافذة الرسم
screen = turtle.Screen()

# إنشاء كائن السلحفاة
t = turtle.Turtle()

# رسم خط مستقيم
t.forward(100)  # تتحرك السلحفاة للأمام بمقدار 100 وحدة

# إنهاء الرسم وإغلاق النافذة عند النقر
screen.exitonclick()
