
x = 3 

#1)
if x > 2:           #x가 2보다 크면 Hello라고 출력
    print ("Hello", "\n")

#2)
if x> 5:
    print("Hello", "\n")        #x가 5보다 크면 Hello라고 출력하고
else:           #다른루트인듯
    print("Hi","\n")            #Hi라고 출력해라

#3)
if x > 5:
    print("Hello", "\n")        #x가 5보다 큰지 보구
elif x == 3:                #==은 같다로 사용
    print("Bye", "\n")
else:                       #그게아니라면
    print("Hi", "\n")       #Hi로 간다.

#elif는 else if의 약자로 else문의 조건식을 여러개로 지정하여 
#조건마다 다른코드를 실행할 수 있다. 단독으로 사용불가능
#와우 홀리 어메이징 휘아하~ ㅋㅋ..


#if 출력문, 참거짓으로 할수도 있다.

x = 5
y = 2
z = 1

if x > y:           #2가 1보다 크면
    print("x(5)는 y(2)보다 크다.")  #출력이 된다.
print("y가 x보다 크지 않기(False)때문에 출력 안된다.", "\n")

if x < y:       #y가 x보다 크지 않다.
    print("x보다 y가 크다.","\n")       #출력이 된다.
print("y가 x보다 크지 않기(False)때문에 출력 안된다.","\n")

if x < y:       #y가 x보다 크지 않다.(True)
    print("x보다 y가 크지 않다.","\n")  #출력이 된다.
print("not이 붙어서 True이기 때문에 출력된다.","\n")

if x > z and x > y :    #x가 z보다 크고 x가 y보다 크면
    print("y가 z보다 크고 x가 y보다 크다.")
print("두가지 모두 맞으면 (True) 출력된다.","\n")

if z > y and x > y :    #0이 1보다 크도 2가 1보다 크면
    print("z가 y보다 크다(Flase) 그리고 x가 y보다 크다.(True)")
#하나라도 틀리면(Flase) 출력 안된다.
print("z가 y보다 크다 (Flase), x가 y보다 크다 (True) 두가지 모두맞아야 (True) 출현된다","\n")

if z > y or x > y :     #0이 1보다 크거나 또는 2가 1보다 크면
    print("z가 y보다 크거나(False) 또는 x가 y보다 크다. (True)")
print("두 가지 중 하나만 맞으면 (True) 출력된다.", "\n")

#여러줄 주석 Shift + Alt + A
# 한줄한줄 Ctrl + /
