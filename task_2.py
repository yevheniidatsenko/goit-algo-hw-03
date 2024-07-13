import turtle

def koch_curve(turtle, length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        koch_curve(turtle, length/3, depth-1)
        turtle.left(60)
        koch_curve(turtle, length/3, depth-1)
        turtle.right(120)
        koch_curve(turtle, length/3, depth-1)
        turtle.left(60)
        koch_curve(turtle, length/3, depth-1)

def draw_koch_snowflake(turtle, length, depth):
    for _ in range(3):
        koch_curve(turtle, length, depth)
        turtle.right(120)

def main():
    length = 400
    depth = int(input("Enter the recursion depth: "))

    window = turtle.Screen()
    window.bgcolor("white")

    my_turtle = turtle.Turtle()
    my_turtle.speed(0)

    draw_koch_snowflake(my_turtle, length, depth)

    window.mainloop()

if __name__ == "__main__":
    main()