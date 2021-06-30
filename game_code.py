import turtle
import math
import random
scr = turtle.Screen()
scr.bgcolor('white')
scr.register_shape('chicken.gif')
scr.register_shape('egg.gif')
scr.register_shape('wolf.gif')
scr.setup(600, 600)
egg = turtle.Turtle(shape='egg.gif')
egg.penup()
egg.speed(0)
chicken = turtle.Turtle(shape='chicken.gif')
chicken.penup()
chicken.speed(0)
chicken.goto(random.randint(-278, 278), 200)
egg.goto(chicken.pos())
wolf = turtle.Turtle(shape='wolf.gif')
wolf.speed(0)
wolf.penup()
wolf.goto(0, -250)
egg.setheading(270)
scr.tracer(0)
def right():
    wolf.setheading(0)
    wolf.forward(10)
def left():
    wolf.setheading(180)
    wolf.forward(10)
def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 78:
        return True
    else:
        return False
scr.listen()
scr.onkey(right, 'Right')
scr.onkey(left, 'Left')
while True:
    scr.update()
    egg.forward(6)
    if egg.ycor() <= -300:
        chicken.setx(wolf.xcor())
        egg.goto(chicken.pos())
    if isCollision(wolf, egg):
        chicken.speed(2)
        chicken.sety((wolf.ycor() + 10))
        scr.exitonclick()