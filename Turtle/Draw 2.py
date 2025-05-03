import turtle
import dpi_awareness

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

# Define colors
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink']

# Draw the shape
for i in range(200):
    pen.color(colors[i % len(colors)])  # Cycle through the colors
    pen.forward(i * 2)                  # Move the turtle forward
    pen.left(119)                       # Turn the turtle left by 119 degrees

# Hide the turtle and keep the window open
pen.hideturtle()
screen.mainloop()