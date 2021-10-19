x = 7
y = 6
print(x + y)

x = '7'
y = '6'
print(x + y)

import turtle 
t = turtle.Turtle()
t.shape("turtle")
radius = 50 # 변수 radius와 값을 선언
x = 30  # 변수 x와 값을 선언
t.circle(radius)    # 반지름이 50인 원이 그려진다.
t.fd(x) # fd는 forward와 같은 명령어이다. 앞으로 30만큼 움직인다.
t.circle(radius)    # 반지름이 50인 원이 그려진다.
x = 50              # 움직이는 거리를 담는 변수 x의 값을 50픽셀로 수정한다.
t.fd(x)             # 앞으로 50만큼 움직인다.
t.circle(radius)    # 반지름이 50인 원이 그려진다.

