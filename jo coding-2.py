a = "Python's favorit food perl"
b= "Python\'s favorit food perl"    #\는 ㅏ따옴표 오류를 막아준다.
print(type(a))      #str 문자열 자료형 다양한 사용법",',"""",등등
print(b)

c = "life is too short \nyou need python"
print(c)            #\n은 줄바꿈 이스케이프 코드이다.
                    #\t는 문자열 사이에 탭 간겨을 줄 때 사용
                    #\\ 문자\를 그래도 표현할때 사용
                    #\' 문자'를 그래도 표현할때 사용


d = """life is' too short
you need '
    python
            eeee"""
            
print(d)            #"""는 이스케이프 코드를 안써도 코드들을 인식한다. 사용하기 편함


a = "Python"
b = "is fun"
print(a+b)
print(a*10)

#indexing

a = "Life is too short, You need python"

print(a[1])         #긴 문자열이 있으면 인덱싱이 된다. 첫숫자부터 0~이다.
print(a[-1])        #-는 역방향이다.
print(a[0:4])       #(a[x:y:z]) x이상y미만 z는 간격이다.
print(a[:8:2])        #비워두면 0부터 시작이다.                 이를 슬라이싱이라고 한다.
print(a[::-1])      #역으로 재생(간격이 -이기때문이다.)

