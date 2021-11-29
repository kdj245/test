import turtle
t = turtle.Turtle()
t.shape("turtle")
def square(length,index): # length는 한변의 길이
    t.color(colorList[index])
    t.begin_fill() 
    for i in range(4):
        t.forward(length) 
        t.left(90)
        t.end_fill()
colorList = ["red", "blue", "green"]
x = -200
for i in range(len(colorList)):
    t.up() # 펜을 든다. 
    t.goto(x,0) # (-200, 0)으로 이동한다.
    t.down() # 펜을 내린다. 
    square(100,i); # square() 함수를 호출한다.
    x+=200