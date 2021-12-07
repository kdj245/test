import turtle

t = turtle. Turtle()
t.shape("turtle")

for i in range (5):
    t.fd(200);
    t.rt(90)
    t.fd(20);
    t.rt(90)
    t.fd(200);
    t.rt(90)
    t.fd(20);
    t.rt(90)
t._screen.exitonclick()



import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color('red', 'yellow')
t.begin_fill()
while True:
    t.fd(200)
    t.lt(170)
    if abs(t.pos()) < 1:
        break
t.end_fill()
t._screen.exitonclick()



import turtle
import math

t = turtle.Turtle()
t.shape("turtle")
t.color('red', 'yellow')

for x in range(0, 360):
    t.goto(x, 200 * math.sin(x*3.14/180))
    t.screen.exitonclick()
    