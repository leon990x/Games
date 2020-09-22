#Simple name game by Leon.

#After running the program, enter any name and see their accuracy :)

#Please note: In "Alpha" stage.

import turtle
import random
from time import sleep


n = random.randint(50, 150)
blastoise = turtle.Turtle()
turtle.ht()
turtle.bgcolor("grey")

#square up
def square_up(ct):
  blastoise.fillcolor("blue")
  blastoise.penup()
  blastoise.forward(n)
  blastoise.right(n)
  blastoise.pendown()
  for b in range(4):
    blastoise.speed(50)
    blastoise.forward(90)
    blastoise.right(90)
  ct += 1
  if ct == 15:
    return True
  square_up(ct)

def target():
  turtle.ht()
  turtle.pendown()
  turtle.speed(100)
  turtle.fillcolor("red")
  turtle.begin_fill()
  turtle.circle(100)
  turtle.end_fill()

  turtle.penup()
  turtle.speed(100)
  turtle.fillcolor("white")
  
  turtle.left(90)
  turtle.forward(30)
  turtle.right(90)
  
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle(70)
  turtle.end_fill()

  turtle.penup()
  turtle.speed(100)
  turtle.fillcolor("red")
  
  turtle.left(90)
  turtle.forward(30)
  turtle.right(90)
  
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle(40)
  turtle.end_fill()

  turtle.penup()
  turtle.speed(100)
  turtle.fillcolor("pink")
  
  turtle.left(90)
  turtle.forward(30)
  turtle.right(90)
  
  turtle.pendown()
  turtle.begin_fill()
  turtle.circle(10)
  turtle.end_fill()

  turtle.penup()
  turtle.ht()




def draw_circle(radius, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def phase(ct):

  turtle.ht()
  
  colors = ["orange", "yellow", "blue"]
  c = colors[random.randint(0,2)]
  for s in range(ct):
    sleep(1)
    turtle.speed(100)
    turtle.penup()
    turtle.forward(random.randint(160, 165))
    turtle.right(random.randint(0, 30))
    turtle.backward(random.randint(0, 50))
    turtle.pendown()
    draw_circle(5, c)
  turtle.penup()
  #turtle.right(90)
  #turtle.forward(1000)

def angle(ct):

  turtle.ht()
  
  colors = ["orange", "yellow", "blue"]
  c = colors[random.randint(0,2)]
  for s in range(ct):
    sleep(2)
    turtle.speed(100)
    turtle.penup()
    turtle.forward(random.randint(-40, 90))
    turtle.right(random.randint(-40, 90))
    turtle.left(random.randint(-50, 50))
    turtle.pendown()
    draw_circle(5, c)
  turtle.penup()

def error_check(ct):

  turtle.ht()
  
  colors = ["orange", "yellow", "blue"]
  c = colors[random.randint(0,2)]
  for s in range(ct):
    sleep(2)
    turtle.speed(100)
    turtle.penup()
    turtle.forward(random.randint(-100, 100))
    turtle.right(random.randint(-100, 90))
    turtle.left(random.randint(-100, 150))
    turtle.pendown()
    draw_circle(5, c)
  turtle.penup()

#Execute

def main():


	target()
	node = input()

	if (node[2] == "o"):
	angle(3)

	elif (node[1] == "i"):
	phase(3)

	elif (node[2] != "o"):
	error_check(3)

	turtle.done()

main()