x = 1   #변수 x = 슷자형 1 선언
y = 2   #변수 y = 숫자형 2 선언

print(x)    #변수 x를 출력
print(y)    #변수 y를 출력
print(x,y)  #변수 x와 y를 출력

z = "안녕"  #변수 z = 문자형 "안녕"으로 선언
print(z)    #ㅁ누자형 z을 출력

# 여러주석 Shift  + Alt + A
# 한줄한줄 Ctrl + /


x = 5   #변수 x = 정수형 7를 선언
y = 3   #변수 y = 정수형 3을 선언

z = 1.2 #변수 z = 실수형 1.2를 선언

print("1)", x+y+z)      #정수형 x,y와 실수수형 z를 더한값 출력
print("2)", x-y-z)      #정수형 x,y와 실수수형 z를 빼기한값 출력 - print("2)",(x-y)-z)
print("3)", x*y*z, "\n") #정수형 x와 y를 곱한 값에 출력후 한줄 공백라인
print("4)", x%y%z)      #x를 y로 나누고 남는 값에서 z나눠서 남는 값 출력
                        #- prit("4)", (x%y)%z)
print("5)", x**y**z)    #x의 y곱에 z곱 - print("5)", x**(y**z))
print("6)", x**y)