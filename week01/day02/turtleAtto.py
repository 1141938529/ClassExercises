import turtle

turtle.showturtle()
turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.circle(100)
turtle.penup()
turtle.goto(0,-110)
turtle.pensize(20)

turtle.pendown()
turtle.circle(110)

turtle.penup()
turtle.goto(0,0)
turtle.color("red")
turtle.pensize(3)
turtle.write("I tried, at least I tried.",align="center", font=("Arial", 12, "normal"))
turtle.hideturtle()
turtle.done()
