# 지역변수와 전역변수
# 지역변수: 그 함수에서만 쓰이는 변수
# 전역변수: 모든 곳에서 쓰이는 변수

def calculate_area (radius):
    # global area   # 이거(전역변수 선언) 없으면 13째 줄 0 나옴
    area = 3.14 * radius**2
    return area     # 지역변수 반환

area = 0
r = float(input("원의 반지름: "))
calculate_area(r)
print("원의 넓이:", area)   # 0 출력 / 10째 줄 없으면 에러남 / global 선언 했다면 정상적 출력
print("원의 넓이:", calculate_area(r))    # 정상적 출력