
x = "Hello"     #변수 x에 문자 Hello 선언
y = "Bye"       #변수 y에 문자 Bye 선언
z = """안녕하세요. 저는 21학번 새내기입니다"""      #변수 z에 문자 2행 선언

print(x)
print(y)
print(z)
print("\n")     #공백행
print(x + y + z)
print("\n")     #공백행
print(z)



print("안녕" + "잘 지내니")
#print("너 혹시 몇 살이니?" + 19)   #형식에러 : 무나형만 문자형에 연결할수 있다.
#"문자열과 숫자형은 연결할수 없다."
print("너 혹시 몇 살이니?" + str(19)+"살이야")  #정수 19를 문자형으로 변환해준다.


x = 19      #숫자
y = "19"    #문자
print(str(x) + y)   #x를 문자형으로 변환해서 문자열로 합쳐서 출력해준다.
print(x + int(y))   #문자형인 y를 숫자형으로 변환해서 사칙연산(+)으로 합의 값을 출력해준다.


#블리안 : boolean - 조건에 따라서 할것
x = True
y = False
print(x), print(y)
print("\n")
a = 3
b = 4
if a > b:
    print("a가 크다.")
print("False이기 때문에 출력이 안됀다.", "\n")