for i  in range(2, 101):
    if 1%2 == 0 :
        print(i, end = " ")


year = 0
balance = 1000

while balance <= 2000:
    year = year + 1
    interest = balance * 0.07
    balance = balance + interest
print(year, "년이 걸립니다.")



n = 1234
sum = 0
while n > 0 :
    digit = n % 10
    sum = sum + digit
    n = n // 10
    print(sum)


ans = 0
while ans != 3*9 :
    ans = int(input("3 x 9는? "))
print("맞았습니다.")