# 조건문: if-else 문

# 들여쓰기는 스페이스 4칸이 좋다.
# :(콜론)을 주의하자.

# if-else 문의 기본 구조
# 성적 평가
score = int(input("성적을 입력하세요: "))
if score >= 60:
    print("합격입니다.")
else:
    print("불합격입니다.")
    
num = int(input("정수를 입력하세요: "))

'''
관계 연산자(relational operator)
==, !=, >, <, >=, <= 등
'''

# 나머지 연산자의 활용
# 짝수 홀수 판단
if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

# and, or 논리 연산자 사용하기
# 윤년 판단
year = int(input("연도를 입력하세요: "))
if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    print(year, "년은 윤년입니다.")
else: 
    print(year, "년은 윤년이 아닙니다.")

# 연속적인 if-else 문
# 양수, 0, 음수 조건 판단
num = int(input("정수를 입력하세요: "))
if num > 0:
    print("양수입니다.")
elif num == 0:
    print("0 입니다.")
else:
    print("음수입니다.")