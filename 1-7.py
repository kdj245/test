# 1번
name = input("이름을 입력하시오: ")
age = int(input("나이를 입력하시오: "))
year = 2021-age+100
print(name + "씨는 " + str(year) + "년에 100살이시네요!")


# 2번
n1 = int(input("첫 번째 숫자를 입력하시오: "))
n2 = int(input("두 번째 숫자를 입력하시오: "))
n3 = int(input("세 번째 숫자를 입력하시오: "))
average = (n1 + n2 + n3) / 3
print(n1, n2, n3,"의 평균은", average, "입니다.")


# 3번
radius = int(input("반지름을 입력하시오: "))
area = 3.141592 * radius * radius
print("반지름이", radius, "인 원의 넓이 =", area, "입니다.")



# 4번
import turtle
t = turtle.Turtle()
t.shape("turtle")
radius=50
t.up()
t.goto(0, 0)
t.down()
t.circle(radius)
radius = radius + 20
t.up()
t.goto(100, 0)
t.down()
t.circle(radius)
radius = radius + 20
t.up()
t.goto(200, 0)
t.down()
t.circle(radius)
t._screen.exitonclick()



# 5번
import turtle
t = turtle.Turtle()
t.shape("turtle")
side=50
t.forward(side)
t.left(120)
t.forward(side)
t.left(120)
t.forward(side)
t.left(120)
t._screen.exitonclick()



# 6번
import turtle
t = turtle.Turtle()
t.shape("turtle")
side=200
t.forward(side)
t.left(120)
t.forward(side)
t.left(120)
t.forward(side)
t.left(120)
t._screen.exitonclick()



# 7번
import turtle
t = turtle.Turtle()
t.shape("turtle")
side = 50
angle = 90
t.forward(side); t.right(angle); t.forward(side); t.right(angle);t.forward(side); 
t.right(angle); t.forward(side) #줄의 끝이어서 ;가 없음.
t.forward(side); t.right(angle); t.forward(side); t.right(angle); t.forward(side)
t.right(angle); t.forward(100); t.right(180) #줄의 끝이어서 ;가 없음.
t.forward(side); t.right(angle); t.forward(side); t.right(angle); t.forward(side); 
t.right(angle); t.forward(side) #줄의 끝이어서 ;가 없음.
t.forward(side); t.right(angle); t.forward(side); t.right(angle); t.forward(side)
t.write("닫으려면 화면 클릭"); t._screen.exitonclick() 