import turtle

def draw_square(some_turtle):
    for i in range(1, 5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    # Create turtle Brad - draw a square
    brad = turtle.Turtle()
    brad.shape("circle")
    brad.color("yellow")
    brad.speed(2)
    draw_square(brad)
    # Create turtle Angie - draw a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    window.exitonclick()

draw_art()
