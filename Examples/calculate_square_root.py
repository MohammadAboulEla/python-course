import math

def great(text):
    result = "Hello " + text
    return result


def ask(text):
    result = text + " What is your name?"
    return result


def calculate_square_root(number):
    if number < 0:
        return "Error: لا يمكن حساب الجذر التربيعي لعدد سالب"
    return math.sqrt(number)


sr = calculate_square_root(-5)
print(sr)