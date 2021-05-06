#반복문 : for, while
#break, continue
#print("철수 : 안녕 영희야 뭐해?")
#print("영희 : 안녕 철수야, 숨만쉬고 있어.")

#for i in rang(10):
#   print("철수 : 안녕 영희야 뭐해?")
#print("영희 : 안녕 철수야, 숨만쉬고 있어.")

i = 0
for i in rang(5):           #i는 첫번째인지 몇번째인지 i라는 변수에 넣어라.
                            #rang(5)는 5번 반복하라는 뜻
    print(i)
    print("철수: 안녕 영희양 뭐해?")
    print("영희 : 안녕 철수야, 숨만쉬고 있어.")

    if i == 1:
        continue
    
    print("워니: 안녕 철수야 영희야!")

i = 0
for i in range(100):
    print(i)
    print("철수: 안녕 영희양 뭐해?")
    print("영희 : 안녕 철수야, 숨만쉬고 있어.")
    i = i + 1

    if i > 2:
        break

i = 0
while i < 3:        #i가 3보다 작으면
    print(i)
    print("철수: 안녕 영희양 뭐해?")
    print("영희 : 안녕 철수야, 숨만쉬고 있어.")
    i = i + 1
    
i = 0
while True:         #무한루프
    print(i)
    print("철수: 안녕 영희양 뭐해?")
    print("영희 : 안녕 철수야, 숨만쉬고 있어.")
    i = i + 1
    
    if i > 2:
        break
    
