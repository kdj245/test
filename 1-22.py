sum = 0
while True:
    x = int(input("정수를 입력하시오: "))
    if x == 0:
        break;
    sum = sum + x
print("합은 ", sum, "입니다. ")



from random import randint

for i in range(3) : 
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    print("첫번째 주사위=", d1, "두번째 주사위=", d2)



import turtle
t = turtle.Turtle()
t.shape("turtle")
t.left(90)

for i in range(1,7) :
    t.forward(100)
    t.forward(-30)
    t.left(60)
    t.forward(30)
    t.forward(-30)
    
    t.right(120)
    t.forward(30)
    t.forward(-30)
    
    t.left(60)
    t.forward(-70)
    t.left(60)
    t.streen.exitonclick()
    
    
import turtle

myPen = turtle.Turtle()
myPen.speed(0)
myPen.coler("#ff0000")

for j in range(1, 10):
    for i in range(1,6):
        myPen.left(144)
        myPen.forward(200)
    myPen._screen.exitonclick()



import turtle
import random

t = turtle.Turtle()
t.shape("turtle")

for j in range(1, 10):
    t.up()
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    r = random.randint(10, 200)
    t.goto(x, y)
    t.down()
    t.circle(r)
t._screen.exitonclick()


