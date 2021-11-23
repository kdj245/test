age = int(input("나이를 입력하시오: "))
if age >= 15:
    print("이 영화를 보실 수 있습니다. 영화의 가격은 10000원입니다.")
else:
    print("이 영화를 보실 수 없습니다. 다른 영화를 보시겠어요?")

        


import turtle

t = turtle.Turtle() # 거북이를 만든다.

t.width(3) # 거북이가 그리는 선의 구께를 3을 한다.

t.shape("turtle") # 커서의 모양을 거북이로 한다.

t.shapesize(3, 3) # 거북이를 3배 확대한다.

# answer값이 아니라 true값인거같습니다.
# 무한 루프이다.
while True:
    command = input("명령을 입력하시오: ")
    if command == "l" or command == "left": # l 또는 left 입력하면
        t.left(90)
        t.forward(100)
    if command == "r" or command == "right": # r 또는 right 입력하면
        t.right(90)
        t.forward(100)