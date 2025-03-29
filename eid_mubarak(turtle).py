import turtle

t = turtle.Turtle()
t.speed(3)
turtle.bgcolor("black")
t.pencolor("yellow")

t.penup()
t.goto(-100, 0)
t.pendown()
t.write("Eid Mubarak!", font=("Arial", 30, "bold"))
t.hideturtle()

turtle.done()
