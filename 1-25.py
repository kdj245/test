import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(9)

def f(x):
    return x**2 +1

t.goto(200,0)
t.goto(0,0)
t.goto(0,200)
t.goto(0,0)

for x in range(150):
    t.goto(x, int(0.01*f(x)))
    
t._screen.exitonclick()


import turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(1)

def draw_line():
    t.fd(100)
    t.backward(100)
    
for x in range(12):
    t.right(30)
    draw_line()

t._screen.esitonclick()



def happyBirthday(person):
    print("Happy birthday to you!")
    print("Happy birthday to you!")
    print("Happy birthday, dear "+ person)
    print("Happy birthday to you!")

happyBirthday("김덕주")



def sumProblem(x, y):
    sum = x + y
    sentence = "정수" + str(x) + "+" + str(y) + "의합은?"
    print(sentence)

def main():
    a = int(input("첫 번째 정수: "))
    b = int(input("두 번째 정수: "))
    sumProblem(a, b)

main()




PI = 3.1425926535

def circleArea(radius):
    return 2 * PI * radius * radius
def circleCircumference(radius):
    return 2 * PI * radius

def main():
    print("반지름이 5인 원의 면적:", circleArea(5))
    print("반지름이 5인 원의 둘레:", circleCircumference(5))

main()



def add(a, b):
    print("(%d + %d)" % (a,b), end=" ")
    return a + b

def subtract(a, b):
    print("(%d + %d)" % (a,b), end=" ")
    return a - b

def multiply(a, b):
    print("(%d + %d)" % (a,b), end=" ")
    return a * b

def divide(a, b):
    print("(%d + %d)" % (a,b), end=" ")
    return a / b

what = add(20, 10)
print("= ", what)

what = subtract(20, 10)
print("= ", what)

what = multiply(20, 10)
print("= ", what)

what = divide(20, 10)
print("= ", what)