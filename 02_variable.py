# 변수 (variable)
""" 
변수: 값을 저장하는 상자.
컴퓨터 메모리 공간에 만들어진다.

변수에 이름 붙이기: python_recommends_snake_case

sum                 # 영문 알파벳 이름으로 시작
_count              # 밑줄 문자로 시작할 수 있다
number_of_pictures  # 중간에 밑줄 문자를 넣을 수 있다
King3               # 맨 처음이 아니라면 숫자도 넣을 수 있다
"""

# 변수 선언하기

# 파이썬은 변수 선언 시 자료형을 명시하지 않는다.
# 생성된 변수에는 얼마든지 다른 값을 저장할 수 있다.


# 변수에 숫자 저장하기
a = 100
a = 200
print(a)    # 200 출력

b = 300
b = a
print(b)    # 200 출력

a = a + 1
print(a)    # 201 출력

sum = a + b
print(sum)  # 401 출력
print(a + b)  # 401 출력


# 변수에 문자열 저장하기
# 쌍따옴표든 홑따옴표든 감싸면 문자형이 된다.
name = "홍길동"
address = '서울시 종로구 1번지'
print(name)
print(address)

# 숫자도 따옴표로 감싸면 문자형이 된다.
x = '10'
y = '1'
print(x + y)    # 101 출력