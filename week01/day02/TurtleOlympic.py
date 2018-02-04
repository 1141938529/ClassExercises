import turtle

turtle.showturtle()
turtle.pensize(5)
turtle.color("black")
turtle.circle(45)

turtle.penup()
turtle.color("blue")
turtle.goto(-110, 0)
turtle.pendown()
turtle.circle(45)

turtle.penup()
turtle.color("red")
turtle.goto(110, 0)
turtle.pendown()
turtle.circle(45)

turtle.penup()
turtle.color("yellow")
turtle.goto(-55, -45)
turtle.pendown()
turtle.circle(45)

turtle.penup()
turtle.color("green")
turtle.goto(55, -45)
turtle.pendown()
turtle.circle(45)

turtle.penup()
turtle.color("blue")
turtle.goto(-110, -80)
turtle.pendown()
# turtle.write("同一个世界，同一个梦想", font=("新宋体", 20, "italic"))
turtle.write("同一个世界，同一个梦想", font=("新宋体", 15, "italic"))


turtle.done()
