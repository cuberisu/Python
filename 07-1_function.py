# 함수

# 함수 정의
# 어떤 코드를 하나로 묶어서 변수로 저장하고 싶다면 함수를 이용하면 된다.
# 또는 코드가 복잡해질 때 단순화하기 위해서도 쓴다.
def print_address():
    print("서울특별시 종로구 1번지")
print_address() # 함수 호출

print("")

# 매개변수 전달받기
# 매개변수(parameter): 함수를 정의할 때 괄호 안에 넣는 변수
def info(name):
    print("서울특별시 종로구 1번지")
    print("이름:",name)
info("홍길동")  # 괄호 안의 내용이 name으로 대입된다.
# argument(인수): 함수 호출 시 넣은 값 (이지만 둘이 혼동해서 쓰임)

print("")

# 값 반환(리턴)
def f(x): 
    return x + 1 # 값을 들고 돌아가라! 라는 뜻
    # return만 적을 경우 None을 리턴하게 됨
    # print()로 처리하는 것보다 return으로 처리하는 것이 편리한 경우가 있음
print(f(5))    # 6 출력

print("")

# 함수에 여러 개의 입력 전달하기
def get_sum(start, end):    # 반복 범위를 입력받음
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum
print(get_sum(1, 10))   # 10 출력
# 반드시 매개변수를 2개 입력받아야 함

print("")

# 디폴트 매개변수 (기본 매개변수) 
# 매개변수를 입력받지 않아도 그 매개변수에 기본값이 들어가게 만든다.
# 디폴트 매개변수는 맨 마지막에 입력해야 함. (가변 매개변수보다도 뒤에 오는 게 좋다)
# def test(a = 10, b): 오류! 디폴트의 의미가 사라지기 때문이다.
def hello(name="철수", msg="좋은 아침!"):  # 인수의 입력이 없어도 되는 함수이다.
    print(name, ",", msg)
hello()   # 디폴트 인수를 입력x: 철수 , 좋은 아침! 출력
hello("영희") # 영희 , 좋은 아침! 출력
hello(msg="별일 없죠?") # 디폴트에 다른 값을 넣을 땐 이렇게 키워드 인수로 입력하는 편.
hello("철수", "별일 없죠?") # msg에 다른 값을 넣으려면 name에 값을 넣어야 하기 때문에 의미가 없어짐.

# 키워드 매개변수: 함수(매개변수=1) 형태로 입력하는 매개변수.

print("")

# 가변 매개변수
# 일반
def print_list(count, list):
    for i in range(count):
        for element in list:
            print(element, end=" ")
print_list(2, ["안녕", "하세요", "파이썬"])
# 안녕 하세요 파이썬 안녕 하세요 파이썬

print("")

# * 연산자: 쉼표로 구분된 여러 개의 매개변수를 튜플로 받을 수 있음
def print_values(count, *value):    # 리스트가 아니라 가변 매개변수를 넣는 함수
    for i in range(count):
        for element in value:
            print(element, end=" ")
hi_list = ["안녕", "하세요", "파이썬"]
print_values(2, hi_list)    # 리스트
# ['안녕', '하세요', '파이썬'] ['안녕', '하세요', '파이썬'] -> 리스트 형태로 출력
print("")
print_values(2, *hi_list)   # *은 리스트 전개 연산자
# *hi_list = '안녕', '하세요', '파이썬'
# 안녕 하세요 파이썬 안녕 하세요 파이썬 -> 각 요소가 출력

# 가변 매개변수 뒤에는 일반 매개변수가 올 수 없다.
# def print_values(*value, count)
# print_values(value1, value2, count) -> count도 value로 인식
# print_values(value1, value2, count=2) -> count 인식 가능 (키워드 매개변수)

print("")

# print() 함수의 end, sep 매개변수
print("안", "녕", "하", "세", "요")         # 안 녕 하 세 요 출력
print("안", "녕", "하", "세", "요", end="") # end의 기본값은 \n. 그래서 끝나고 줄바꿈이 되던 것.
print("안", "녕", "하", "세", "요", sep="") # sep의 기본값은 " ". 그래서 value마다 띄어쓰기가 됨.

# 딕셔너리 매개변수 (쓸 일은 거의 없음)
# 딕셔너리 매개변수는 가변 매개변수보다도 뒤에 와야 한다.
# 가변 매개변수는 튜플로 받고, 딕셔너리 매개변수는 딕셔너리로 받는다.
def 함수(*가변, **딕셔너리):
    print(가변, 딕셔너리)
함수("안", "녕", a=10, b=20, c=30)
# ('안', '녕') {'a': 10, 'b': 20, 'c': 30}