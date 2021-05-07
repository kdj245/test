# a.count = 함수이다. 무언가를 찾을때 사용

a = "hobby"
print(a.count('b'))         #a변수에서 b가 몇개 들어가있는지 세어봐라

a = "hobby"
 #   01234
print(a.find('b'))          #a변수에서 b가 몇번째에 있는지 찾아라
                            #맨처음 1개만 찾을수 있다.
a = "hobby"
 #   01234
print(a.find('x'))          #변수에 없을경우 -1이 나온다.



#문자열 삽입 (join) 

a = " , " 
print(a.join('abcd'))               #a,b,c,d 즉 ,를 기준으로 쪼개준다           

#소문자를 대문자로 변경 (upper)
a = "hi"
print(a.upper())                    #lower는 대문자를 소문자로 바꿔준다.

