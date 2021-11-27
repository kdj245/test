
import random
number = random.randint(1,8)

list = ["한 점의 의심도 없이 맞습니다.", "할 수 있습니다.", "물론입니다.", 
"글쎄요 열심히 해야할것입니다." "안 될 것 같습니다.", "조금 더 노력하세요.", "행운을 빕니다.", 
"다음 달에 할 수 있을 겁니다."]

while True:
    name = input("이름: (종료하려면 엔터키)")
    if name == '':
        break;
    question = input("무엇에 대하여 알고 싶은가요? ")
    print(name, "님", "\"", question ,"\"에 대하여 질문 주셨군요.")
    print("운명의 주사위를 굴려볼께요.")
    print(list[number-1])
    
    


import turtle
t = turtle.Turtle()
t.shape("turtle")

def shape(length): # length는 한변의 길이입니다.
    s = turtle.textinput("","몇각형을 원하시나요? : ")
    n = int(s)
    
    for i in range(n):
        t.forward(length)
        t.left(360/n)

t.up() # 펜을 든다
t.goto(-200,0) # (-200, 0)으로 이동한다. 
t.down() # 펜을 내린다. 
shape(100); # square() 함수를 호출한다.

t.up() 
t.goto(0,0) 
t.down()
shape(100);

t.up() 
t.goto(200,0) 
t.down()
shape(100);
