import turtle 
t = turtle.Turtle()

def circle(length):
    t.circle(length) 
    t.left(60)

def drawit(x, y):
    t.penup() 
    t.goto(x,y) 
    t.pendown()
    t.begin_fill() 
    t.color("green") 
    circle(50) 
    t.end_fill()

s = turtle.Screen() # 그림이 그려지는 화면(s는 대문자네 ㅋㅋ)
s.onscreenclick(drawit) # 마우스 클릭시 이벤트 처리함수 생성

