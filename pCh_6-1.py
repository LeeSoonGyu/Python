# 메서드의 재정의 (부모클래스 처럼 자식클래스도 상속)
# 부모클래스
class Employee:
    name = None
    pay = 0
    def __init__(self, name):
        self.name = name
    def pay_calc(self):
        pass
# 자식 클래스 (정규직)
class Permanent(Employee):
    def __init__(self, name):
        super().__init__(name) # 부모클래스 호출
    def pay_calc(self, base, bonus):
        self.pay = base + bonus # 급여 = 기본급 + 상여금
        print('총 수령액 : ', format(self.pay, '3,d'), '원')
# 자식 클래스 (임시직)
class Temporary(Employee):
    def __init__(self, name):
        super().__init__(name) # 부모 클래스 호출
    def pay_calc(self, tpay, time):
        self.pay = tpay * time # 급여 = 시급 * 시간
        print('총 수령액 : ', format(self.pay, '3,d'), '원')
# 객체 생성
p = Permanent('이순신')
p.pay_calc(3000000, 200000)
t = Temporary('홍길동')
t.pay_calc(15000, 80)

# 다형성
# 부모 클래스 생성
class Flight:
    def fly(self): # 부모 원형 함수
        print('날다, fly 원형 메서드.')
# 자식 클래스 : 비행기
class Airplane(Flight):
    def fly(self): # 함수 재정의
        print('비행기가 날다.')
# 자식 클래스 : 새
class Bird(Flight):
    def fly(self):
        print('새가 날다.')
# 자식 클래스 : 종이비행기
class Paperairplane(Flight):
    def fly(self):
        print('종이비행기가 날다.')
# 객체 생성
flight = Flight() # 부모 클래스 객체
air = Airplane() # 자식 클래스 객체
bird = Bird() # 자식 클래스 객체
paper = Paperairplane() # 자식 클래스 객체
# 다형성
flight.fly()
flight = air
flight.fly()
flight = bird
flight.fly()
flight = paper
flight.fly()

# 내장클래스 builtins 모듈
# 리스트 열거형 객체
lst = [1, 3, 5]
for i, c in enumerate(lst):
    print('색인 : ', i, end=',')
    print('내용 : ', c)
# 딕트 열거형 객체
dit = {'name' : '홍길동', 'job' : '회사원', 'addr' : '서울시'}
for i, k in enumerate(dit):
    print('순서 : ', i, end=',')
    print('키 : ', k, end=',')
    print('값 : ', dit[k])

# 내장클래스 import 모듈
# 모듈 내장클래스 import
import datetime # 모듈 import
from datetime import date, time
# date 클래스
help(date)
today = date(2021, 10, 18) # date 객체 생성
print(today) # date 객체 정보
# date 객체 멤버 변수 호출
print(today.year)
print(today.month)
print(today.day)
# date 객체 메서드 호출
w = today.weekday() # Monday == 0 ... Sunday == 6
print('요일 정보 : ', w)
# time 클래스
help(time)
currTime = time(11, 12, 10) # time 객체 생성
print(currTime) # time 객체 정보
# time 객체 멤버변수 호출
print(currTime.hour)
print(currTime.minute)
print(currTime.second)
# time 객체 메서드 호출
isotime = currTime.isoformat()
print(isotime)