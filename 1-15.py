import random
tries = 0
guess = 0
answer = random.randint(1,100)
print("1부터 100 사이의 숫자를 맞추시오: ")

while guess != answer: 
    if tries < 10: 
        guess = int(input("숫자를 입력하시오: "))
        tries = tries + 1
        if guess < answer: 
            print("낮음!") 
        elif guess > answer:
            print("높음!")
    else: 
            print("시도횟수를 초과하였습니다.") 
            break
        
       
if guess == answer: 
    print("축하합니다. 시도횟수= ", tries)
else: 
    print("정답은 ", answer)
    
    


import random
while True:
    q = random.randint(0,1) 
    x = random.randint(1,100)
    y = random.randint(1,100)
    if (q == 1) & (x > y): 
        print(x, "-", y, "=", end= " ") 
        answer = int(input()) 
        if answer == x - y: 
            print("잘했어요!!")
        else: 
            print("다음번에는 잘할 수 있죠?") 
    else: 
        print(x, "+", y, "=", end= " ") 
        answer = int(input()) 
        if answer == x + y: print("잘했어요!!")
        else: 
            print("다음번에는 잘할 수 있죠?")


