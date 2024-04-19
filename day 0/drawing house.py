from turtle import*

speed(5)
width(5)
shape("circle")

#drawing square

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

#end of drawing square



#drawing door

forward(70)
begin_fill()
color("red")
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()

#end of drawing door



#drawing roof
color("green")
penup()
goto(200,200)
pendown()
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of drawing roof



#drawing windows

#drawing 1st window
penup()
goto(0,110)
pendown()
color("cyan")
begin_fill()
left(120)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()
#end of drawing 1st window

#drawing 2nd window
penup()
goto(200,110)
pendown()
begin_fill()
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()






exitonclick()