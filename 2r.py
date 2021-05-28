
x = "Hello"     #변수 x에 문자 Hello 선언
y = "Bye"       #변수 y에 문자 Bye 선언
z = """안녕하세요. 아이헬로. 방가방가 굳모닝~."""      #변수 z에 문자 2행 선언함

print(x)
print(y)
print(z)
print("\n")     #공백
print(x + y + z)
print("\n")     #공백
print(z)


print("안녕" + "잘 지내니")
#print("너 혹시 몇 살이니?" + 19)   #형식에러 : 무나형만 문자형에 연결할수 있다.
#"문자열과 숫자형은 연결할수 없다."
print("너 혹시 몇 살이니?" + str(19)+"살이야")  #정수 19를 문자형으로 변환해준다.

x = 24      #숫자
y = "24"    #문자
print(str(x) + y)   #x를 문자형으로 변환해서 문자열로 합쳐서 출력해준다.
print(x + int(y))   #문자형인 y를 숫자형으로 변환해서 사칙연산(+)으로 합의 값을 출력해준다.

#블리안 : boolean - 조건에 따라서 할것
x = True
y = False
print(x), print(y)
print("\n")
a = 5
b = 6
if a > b:
    print("a가 크다.")
print("False이기 때문에 출력이 안됀다.", "\n")

#조건에 따라서 사용
#str은 문자형
#int는 숫자형을 사용할때쓴다
#이땨 저번에도 했다시피 문자형을 사용하면 어지간해서 다 가능하다.