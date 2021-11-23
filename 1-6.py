# 1번
print("환영합니다.")
print("파이썬의 세계에 오신 것을 환영합니다.")
print("파이썬은 강력합니다.")


# 2번
print("반갑습니다. 파이썬!")
print("2*3/10")
print("Hello", "world", "!!!")


# 3번
print(7*24)


# 4번
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.forward(100);
t.left(90)
t.forward(100);
t.right(90)
t.forward(100);
t.right(90)
t.forward(100);
t.left(90)
t.forward(100);
t._screen.exitonclick()  # 화면을 마우스로 클릭해야 종료되게 하는 부분
#4번의 2번째 방법 – 함수를 전역으로 사용할수 있도록 선언
from turtle import *
shape("turtle")
forward(100)
left(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
left(90)
forward(100)
write("종료하려면 화면클릭")
exitonclick() # 화면을 마우스로 클릭해야 종료되게 하는 부분



# 5번
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.width(10)
t.forward(100)
t.left(90)
t.forward(100)
t._screen.exitonclick() # 화면을 마우스로 클릭해야 종료되게 하는 부분


# 6번
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.forward(100)
t._screen.exitonclick() # 화면을 마우스로 클릭해야 종료되게 하는 부분


# 7번
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.shape("square")
t.forward(100)
t._screen.exitonclick() # 화면을 마우스로 클릭해야 종료되게 하는 부분


# 8번
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.up()
t.goto(0, 0)
t.down()
t.forward(100);
t.up()
t.goto(0, 100)
t.down()
t.forward(100);
t._screen.exitonclick() # 화면을 마우스로 클릭해야 종료되게 하는 부분


# 9번
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.up(); t.goto(-150, 0); t.down(); t.circle(80)
t.up(); t.goto(0, 0); t.down(); t.circle(80)
t.up(); t.goto(150, 0); t.down(); t.circle(80)
t.up(); t.goto(-80, -100); t.down(); t.circle(80)
t.up(); t.goto(80, -100); t.down(); t.circle(80)
t._screen.exitonclick() # 화면을 마우스로 클릭해야 종료되게 하는 부분



