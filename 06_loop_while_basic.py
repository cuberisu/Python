# 반복문
# while 문
# while 문은 반복 조건이 정해져 있을 때 유용하다.

# 비밀번호 입력
pw = 'python'
while(True):    # 조건이 참이면 반복을 계속한다.
    user = input("암호를 입력하세요: ")
    if user == pw:
        print("로그인 성공")
        break

print("")

# 1부터 10까지의 합을 계산하는 while loop
num = 1
sum = 0
while num <= 10:    # 조건이 참이면 반복을 계속한다.
    sum = sum + num
    num = num + 1
print("1부터 10까지의 합:", sum)

print("")

# 계속할까요?
total = 0
answer = "y"
while answer == "y":    # n 입력할 때까지 반복
    number = int(input("합산할 정수를 입력하세요: "))
    total = total + number
    answer = input("계속 더할까요?(y/n): ")
print("입력한 숫자의 총합은", total, "입니다.")

print("")

# 프로그램이 가지고 있는 정수를 사용자가 알아맞추는 게임
answer = 55
tries = 0
guess = 0
while guess != answer:
    guess = int(input("숫자를 맞추세요: "))
    tries = tries + 1
    if guess > answer:
        print("높음!")
    if guess < answer:
        print("낮음!")
print("정답입니다! 시도 횟수:", tries)