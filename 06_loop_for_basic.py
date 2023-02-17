# 반복문
# for 문의 여러 가지 형태
# for 문은 반복 횟수가 정해져 있을 때 유용하다.

# 들여쓰기는 스페이스 4칸이 좋다.
# :(콜론)을 주의하자.

for i in [1, 2, 3, 4, 5]:
    print(i, end=" ") # end=""는 print()문의 자동 개행을 막아준다. (한줄에 전부 출력)
    # 1 2 3 4 5
    
print("")

# range() 함수
# range(start=0, stop, step=1)
# start: 시작값 / stop: 종료값(stop 자신은 포함되지 않음) / step: 한 번에 증가되는 값
for i in range (1, 6, 1):
    print(i, end=" ")
    # 1 2 3 4 5

print("")

# 숫자를 하나만 적으면 stop값이고, start=0, step=1로 지정된다.
for i in range(5):  
    print(i, end=" ")
    # 0 1 2 3 4

print("")

# 숫자를 2개만 적으면 step=1로 지정된다.
# 팩토리얼 계산: n!은 1부터 n까지의 정수를 모두 곱한 것.
n = int(input("팩토리얼을 계산할 정수를 입력하세요: "))
fact = 1
for i in range(1, n+1): 
    fact = fact * i
print(n, "! 은", fact, "입니다.")