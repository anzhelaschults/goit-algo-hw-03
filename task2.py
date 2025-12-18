import turtle

def koch_curve(t, order, size):
    if order == 0:
        # draw a straight line
        t.forward(size)
    else:
        # divide into 4 segments
        for angle in [60, -120, 60, 0]: 
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def koch_snowflake(order, size=300):
    # Setup the window
    window = turtle.Screen()
    window.bgcolor("white")
    window.title(f"Koch Snowflake - Level {order}")
    
    # Setup the turtle
    t = turtle. Turtle()
    t.speed(0)  
    t.color("blue")
    t.pensize(1)
    
    # Move turtle to starting position
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()
    
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)
    
    t.hideturtle()
    window.mainloop()

def main():

    print("Koch Snowflake Fractal Generator")
    print("=" * 40)
    
    while True:
        try:
            order = int(input("Enter recursion level (0-5 recommended): "))
            if order < 0:
                print("Please enter a non-negative number.")
                continue
            if order > 7:
                print("Warning: High recursion levels may take a long time to draw!")
                confirm = input("Continue? (y/n): ")
                if confirm.lower() != 'y':
                    continue
            break
        except ValueError: 
            print("Please enter a valid integer.")
    
    print(f"\nDrawing Koch Snowflake with recursion level {order}...")
    print("Close the graphics window to exit.")
    
    koch_snowflake(order)

if __name__ == "__main__":
    main()