class Car:
    def drive(self):
        self.speed = 60
        
# 클래스는 특정 개념을 표현만 할 뿐 사용을 하려면 인스턴스를 생성해야 한다.
myCar = Car()   # myCar는 Car의 인스턴스이다. 
myCar.speed = 0
myCar.color = "blue"
myCar.model = "E-Class"

print("자동차 객체를 생성하였습니다.")
print("자동차의 속도는", myCar.speed)
print("자동차의 색상은", myCar.color)
print("자동차의 모델은", myCar.model)

print("자동차를 주행합니다.")
myCar.drive()   # 객체 안의 drive() 메소드가 호출된다.
print("자동차의 속도는", myCar.speed)  # 60