import turtle
t = turtle.Turtle()
t.shape("turtle")
for i in range(6): 
    t.forward(100) 
    t.left(360/6)


import turtle
t = turtle.Turtle()
t.shape("turtle")
s = turtle.textinput("","몇각형을 원하시나요? : ")
n = int(s)
s = turtle.textinput("","한변의 크기를 입력해주세요 : ")
len = int(s)
for i in range(n): 
    t.forward(len) 
    t.left(360/n)
    
    

import turtle
import random
t = turtle.Turtle()
t.shape("turtle")
for i in range(30): 
    length = random.randint(1,100) 
    t.forward(length)
    angle = random.randint(1,4) 
    t.right(90 * angle)


# 중간에 무엇이잘못됐는지 아직잘모르겟습니다.
# 확인되면 수정후 재업하겟습니다