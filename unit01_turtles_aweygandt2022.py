############################################################################
#     Aidan Weygandt                        2.11.2021                      #
#     Unit 2 Problems                                                      #
#.    Age calculator, sum of digits, initial deposit, current time.        #
############################################################################
import turtle
turtle.pendown()
turtle.forward(50) #starts star
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(50)
turtle.penup() #end of star

turtle.forward(125) #lines up for rectanguliod
turtle.pendown() 
turtle.forward(100) #starts rectanguliod
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(45)
turtle.forward(25)
turtle.right(45)
turtle.forward(100)
turtle.right(135)
turtle.forward(25)
turtle.penup()
turtle.left(45)
turtle.forward(50)
turtle.left(135)
turtle.pendown()
turtle.forward(25)
turtle.left(45)
turtle.forward(50)
turtle.penup()
turtle.right(180)
turtle.forward(50)
turtle.right(90)
turtle.pendown()
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.penup()
turtle.right(180)
turtle.forward(50)
turtle.pendown()
turtle.right(45)
turtle.forward(25)
turtle.right(45)
turtle.penup() #end of rectanguliod

turtle.forward(250) #moves to more empty canvas
turtle.pendown()
turtle.forward(350) #draws x axis
turtle.penup()
turtle.right(180)
turtle.forward(175)
turtle.pendown()
turtle.right(90)
turtle.forward(175) #draws bottom of y axis
turtle.right(180)
turtle.penup()
turtle.forward(175)
turtle.pendown()
turtle.forward(175) #draws bottom of y axis
turtle.penup() #end of cartesian grid

turtle.left(90)
turtle.forward(88)
turtle.left(90)
turtle.forward(88) #moves to quadrant II
turtle.color("#FF0000") #changes pen color to red
turtle.pendown()
turtle.left(90) #starts triangle
turtle.forward(60)
turtle.right(120)
turtle.forward(60)
turtle.right(120)
turtle.forward(60) #end of triangle
turtle.write("Triangle", 0)
turtle.right(120)
turtle.penup()

turtle.color("#00FF00") #changes pen color to green
turtle.forward(120) #moves to quadrant I
turtle.pendown()
turtle.forward(60) #starts square
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(60)
turtle.right(90)
turtle.forward(60) #end of square
turtle.write("Square", 0)
turtle.penup()

turtle.right(180)
turtle.forward(156) #moves to quadrant IV
turtle.pendown()
turtle.color("#ee00ee") #changes color to pink
x = 0
while x < 45: # creates a "circle" by reapeating small straght lines 45 times
  turtle.forward(5)
  turtle.left(8)
  x = x + 1
turtle.right(180) #end of circle
turtle.penup()
turtle.forward(30)
turtle.write("Circle", 0)
turtle.penup()

turtle.left(90)
turtle.forward(70)
turtle.pendown()
turtle.color("#0000FF") #changes color to blue
turtle.forward(40) #start of pentagon
turtle.left(72)
turtle.forward(40)
turtle.left(72)
turtle.forward(40)
turtle.left(72)
turtle.forward(40)
turtle.left(72)
turtle.forward(40) #end of pentagon
turtle.penup()
turtle.left(72)
turtle.forward(40)
turtle.right(180)
turtle.write("Pentagon", 0)
while x == x: #so you can close out when you want
    turtle.right(1) #was kinda only for testing purposes though
#yes i know i could use while loops for my other shapes and it might've saved time if only i had thought
#of it when i wasnt already on the circle (╯°□°)╯︵ ┻━┻