from turtle import*

speed(0)
width(5)

bgcolor("lightblue")

penup()
goto(-1000,-200)
pendown()

color("green")
begin_fill()

forward(2000)
right(90)
forward(500)
right(90)
forward(2000)
right(90)
forward(500)
right(90)
end_fill()
penup()
goto(0,0)
pendown()


#drawing castle

begin_fill()
color("grey")

penup()

goto(-450,-300)
pendown()

goto(100,-300)
left(90)

forward(300)
left(90)

forward(550)
left(90)

forward(300)
left(180)

end_fill()

forward(300)
color("red")
begin_fill()
right(22.5)

forward(275)
right(135)

forward(275)
left(67.5)

penup()

forward(130)
left(67.5)

pendown()

forward(275)
right(135)

forward(275)
left(180)


end_fill()


forward(275)


right(22.5)
color("green")
begin_fill()

forward(50)
right(90)

forward(100)
right(90)

forward(50)
right(90)

forward(100)
right(90)


end_fill()

forward(20)
right(90)

forward(20)
left(90)

color("black")
forward(25)
right(90)

forward(14)
left(180)

forward(14)
left(90)

forward(35)
left(90)

forward(14)
left(90)

forward(14)
left(90)

forward(3)
left(180)

forward(15)
left(90)

forward(21)
right(90)

forward(20)
right(90)

forward(35)
right(90)

forward(20)
right(90)

forward(35)
right(90)

forward(20)
right(90)

forward(35)
left(157.5)

forward(40)
right(135)

forward(40)
left(180)

forward(20)
right(112.5)

forward(5)
left(180)

forward(25)
left(180)

penup()
goto(-10,-200)


color("cyan")
begin_fill()

forward(50)
left(90)

forward(100)
left(90)

forward(50)
left(90)

forward(100)
left(90)

end_fill()


penup()
goto(-400,-200)

begin_fill()

forward(50)
left(90)

forward(100)
left(90)

forward(50)
left(90)

forward(100)
left(90)

end_fill()

penup()
goto(-75,-300)
left(180)
pendown()


begin_fill()
color("saddlebrown")
forward(175)
right(90)

forward(120)
right(90)

forward(175)
right(90)

forward(120)
right(90)
end_fill()



left(180)

penup()
goto(150,-300)
pendown()


#end of drawing castle



#drawing king

color("black")
width(8)

forward(6)
left(90)

forward(40)
right(90)

forward(20)
right(90)

forward(40)
right(90)

forward(6)
left(180)

forward(6)
left(90)

forward(40)

color("blue")
begin_fill()

forward(40)
right(157.5)

forward(40)
left(180)

forward(40)
left(67.5)

forward(20)
left(22.5)

forward(40)
left(180)

forward(40)
right(112.5)

forward(40)
left(90)

forward(20)
left(90)

forward(40)
left(90)

end_fill()

forward(8)
right(90)

color("tan")

forward(7)
left(90)

width(0)

begin_fill()

forward(12)
right(90)

forward(20)
right(90)

forward(20)
right(90)

forward(20)
right(180)

end_fill()


forward(10)
left(90)

forward(4)
color("black")

width(7)

forward(1)

width(0)

color("tan")
forward(10)

color("black")

width(7)

forward(1)

width(0)

color("tan")
forward(4)
right(90)

forward(10)
color("gold")

begin_fill()

forward(3)
right(90)

forward(20)
right(90)

forward(3)
right(90)

forward(20)
right(90)

end_fill()

begin_fill()

forward(3)
right(22.5)

forward(15)
right(135)

forward(15)
end_fill()


begin_fill()
left(135)
forward(15)

right(135)
forward(15)

end_fill()


#end of drawing king

#drawing queen


penup()
goto(250,-300)
left(67.5)
pendown()

color("black")
width(8)

forward(6)
left(90)

forward(40)
right(90)

forward(20)
right(90)

forward(40)
right(90)

forward(6)
left(180)

forward(6)
left(90)

forward(40)

color("pink")
begin_fill()

forward(40)
right(157.5)

forward(40)
left(180)

forward(40)
left(67.5)

forward(20)
left(22.5)

forward(40)
left(180)

forward(40)
right(112.5)

forward(40)
left(90)

forward(20)
left(90)

forward(40)
left(90)

end_fill()

forward(8)
right(90)

color("tan")

forward(7)
left(90)

width(0)

begin_fill()

forward(12)
right(90)

forward(20)
right(90)

forward(20)
right(90)

forward(20)
right(180)

end_fill()


forward(10)
left(90)

forward(4)
color("black")

width(7)

forward(1)

width(0)

color("tan")
forward(10)

color("black")

width(7)

forward(1)

width(0)

color("tan")
forward(4)
right(90)

forward(10)
color("gold")

begin_fill()

forward(3)
right(90)

forward(20)
right(90)

forward(3)
right(90)

forward(20)
right(90)

end_fill()

begin_fill()

forward(3)
right(22.5)

forward(15)
right(135)

forward(15)
end_fill()


begin_fill()
left(135)
forward(15)

right(135)
forward(15)

end_fill()


#end of drawing queen


#drawing clouds

penup()
goto(300,300)
pendown()
color("white")
begin_fill()
circle(50)
end_fill()

goto(350,320)
begin_fill()
circle(50)
end_fill()

goto(270,320)
begin_fill()
circle(50)
end_fill()

goto(230,290)
begin_fill()
circle(50)
end_fill()

goto(330,280)
begin_fill()
circle(50)
end_fill()

penup()
goto(-300,300)
pendown()

begin_fill()
circle(50)
end_fill()

goto(-350,320)
begin_fill()
circle(50)
end_fill()

goto(-270,320)
begin_fill()
circle(50)
end_fill()

goto(-230,290)
begin_fill()
circle(50)
end_fill()

goto(-330,280)
begin_fill()
circle(50)
end_fill()

#end of drawing clouds

#drawing tree

penup()
goto(350,-300)
pendown()

color("saddlebrown")
begin_fill()
left(67.5)
forward(10)
left(90)

forward(100)
left(90)

forward(10)
left(90)

forward(100)
left(90)

end_fill()

forward(10)
left(90)

forward(100)
right(90)

color("lightgreen")
begin_fill()
circle(50)
end_fill()

goto(330,-190)
begin_fill()
circle(50)
end_fill()

goto(390,-190)
begin_fill()
circle(50)
end_fill()

goto(360,-170)
begin_fill()
circle(50)
end_fill()

#end of drawing tree


#drawing apples

penup()
color("red")
goto(330,-190)
pendown()
begin_fill()
circle(10)
end_fill()

penup()
color("red")
goto(360,-170)
pendown()
begin_fill()
circle(10)
end_fill()

penup()
color("red")
goto(420,-170)
pendown()
begin_fill()
circle(10)
end_fill()

penup()
color("red")
goto(390,-190)
pendown()
begin_fill()
circle(10)
end_fill()

penup()
color("red")
goto(360,-170)
pendown()
begin_fill()
circle(10)
end_fill()

penup()
color("red")
goto(330,-190)
pendown()
begin_fill()
circle(10)
end_fill()

penup()
color("red")
goto(330,-150)
pendown()
begin_fill()
circle(10)
end_fill()

penup()
color("red")
goto(370,-120)
pendown()
begin_fill()
circle(10)
end_fill()

penup()
color("red")
goto(390,-160)
pendown()
begin_fill()
circle(10)
end_fill()

penup()
color("red")
goto(310,-120)
pendown()
begin_fill()
circle(10)
end_fill()

penup()
color("red")
goto(400,-120)
pendown()
begin_fill()
circle(10)
end_fill()

penup()
color("red")
goto(300,-160)
pendown()
begin_fill()
circle(10)
end_fill()

#end of drawing apples


penup()
goto(100,-300)



color("black")



exitonclick()