password = 12345


def hello_someone(name):
    print("Hello " + name)


def add(x, y):
    convert_x = int(x)
    convert_y = int(y)
    text = "x + y = "
    print(text, convert_x + convert_y)


def multi(x, y):
    return x * y


def sub(x, y):
    return x-y

def draw_rect(w, t):
    t.forward(w)  # تحرك للأمام بمقدار 100 وحدة
    t.right(90)  # الدوران بزاوية 90 درجة

    t.forward(w)  # تحرك للأمام بمقدار 100 وحدة
    t.right(90)  # الدوران بزاوية 90 درجة

    t.forward(w)  # تحرك للأمام بمقدار 100 وحدة
    t.right(90)  # الدوران بزاوية 90 درجة

    t.forward(w)  # تحرك للأمام بمقدار 100 وحدة
    t.right(90)  # الدوران بزاوية 90 درجة


def print_hello_twice():
    print("hello")
    print("hello")

def draw_shape(edge, w, t):
    for i in range(edge):
        t.forward(w)
        t.right(360 / edge)

