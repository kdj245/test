#도전문제 1장입니다.
print("안녕하세요?")
print("programming에 입문하신 것을 축하드립니다.")

print(3.141592*10.0*10.0)
print((1/100)*1234)

import turtle #turtle모듈을 불러온다.
t = turtle.Turtle() #turtle을 t로 선얼 import turtle as t 할 수 있다.
t.shape("turtle");  #turtle모듈의 아이콘을 거북이 모양으로 선언
                    #기본 아이콘은 classsic, 삼각형은 triangle. 원은 circle
t.forward(100); # 100픽셀만큼 직진 (이동 길이=각 변으니 길이)
t.left(120);    # 120도 회전(회전각도 즉, 외각이 120도를 이뤄야 정삼각형 내각60도가 만들어진다.)
t.forward(100);
t.left(120);
t.forward(100);
t.left(120);



import turtle 
t = turtle.Turtle() 
t.shape("turtle");  
                    
t.forward(100); # 100픽셀만큼 직진 (이동 길이=각 변으니 길이)
t.left(90);    # 90도 회전
t.forward(100);
t.left(90);
t.forward(100);
t.left(90);
t.forward(100);
t.left(90);


import turtle 
t = turtle.Turtle() 
t.shape("turtle");  
                    
t.forward(100); 
t.left(60);    
t.forward(100);
t.left(60);
t.forward(100);
t.left(60);
t.forward(100);
t.left(60);
t.forward(100);
t.left(60);
t.forward(100);
t.left(60);