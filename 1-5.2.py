import turtle

t = turtle.Turtle() # 거북이를 만든다.

t.width(3) # 거북이가 그리는 선의 구께를 3을 한다.

t.shape("turtle") # 커서의 모양을 거북이로 한다.

t.shapesize(3, 3) # 거북이를 3배 확대한다.

flag = True

# 루프 제어변수인 flag를 둔다
while flag:
    command = input("명령을 입력하시오: ")
    if command == "l" or command == "left": #l 또는 left 입력하면
        t.left(90)
        t.forward(100)
    if command == "r" or command == "right": # r 또는 right 입력하면
        t.right(90)
        t.forward(100)
    if command == "q" or command == "quit": # q 또는 quit 입력하면 
        flag = False
        

import random

print("주사위 던지기 게임을 시작합니다.")
dice = random.randrange(6) + 1
print("주사위 눈은 "+str(dice)+"입니다.")
print("게임이 종료되었습니다.")

import random
time = random.randint(1,24)
print("좋은 아침입니다. 지금 시각은 "+str(time) + "시 입니다.")

#sunny = random.choice([Ture,Fales])
#if sunny:
#   print("현재 날씨가 화창합니다.")
#else:
#   print("현재 날씨가 화창하지 않습니다.")

#종달새가 노래를 할 것인지를 판단해보자.
if time >= 6 and time <9 and True:
        print("종달새가 노래를 한다.")
        
elif time >= 14 and time < 16 and True:
    print("종달새가 노래를 한다.")
else:
    print("종달새가 노래를 하지 않는다.")


id = "qwer"
pw = "123456"
s = input("아이디를 입력하십시오: ")
if s == id:
    p = input("패스워드를 입력하십시오:")
    if p == pw:
        print("환영합니다.")
    else:
        print("비밀번호가 잘못되었습니다.")
        
else:
    print("아이디를 찾을수 없습니다.")


import random
option = ["왼쪽 상단", "왼쪽하단", "중앙" ,"오른쪽 상단", "오른쪽하단"]
computer_choice = random.choice(option)
user_choice = input("어디를 수비하시겠어요?(왼쪽 상단, 왼쪽하단,  중앙, 오른쪽상단, 오른쪽 하단)")
if computer_choice == user_choice:
    print("수비에 성공하셨습니다.")
else:
    print("페널티킥에 성공하였습니다.")
    
