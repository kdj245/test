a = "i eat %d apples."  % 3     #따옴표를 안달아줘도 돼서 편하다
print(a)            #숫자는%d

b = "i eat " + str(3) + " apples."
print(b)

number = 5
day = "three"
a = "i ate %d apples. so i was sick for %s days." %(number, day)
print(a)

# %s = 문자열을 나타낼때     이게 사기케라 뭘넣어도 가능함
# %d = 정수를 나타낼때
# %f = 부동소수를 나타낼때 사용


#포맷팅 
a = "asd{age} asd{name} asd".format(name="Lbp",age=3)   

print(a)


name = "int"        #f이후 쓰면 들어간다 format약자 취급
a = f"나의 이름은 (name)입니다."

print(a)

#정렬과 공백
a = "%10s" % "hi"       #칸수를 띄어쓰기할때 사용 10칸 띄어쓰기 쓸일없음 ㅋ
print(a)

a = "%0.2f" %3.4235        #%0.2f처럼 소숫점을 자를때 사용
print(a)

