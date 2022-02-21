import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')
michelangelo.speed(speed=1)
leonardo.speed(speed=1)

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here

michelangelo.forward(random.randrange(1,100))
leonardo.forward(random.randrange(1,100))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

for i in range(10):
  michelangelo.forward(random.randrange(0,10))
  leonardo.forward(random.randrange(0,10))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

# Part B - complete part B here
leonardo.goto(0,0)
leonardo.down()
sides= [3,4,6,9,12]

for num_of_sides in sides:
  for i in range(num_of_sides):
    leonardo.right(360/num_of_sides)
    leonardo.forward(40)
  leonardo.clear()
leonardo.up()
leonardo.goto(-100,-20)

window.exitonclick()
