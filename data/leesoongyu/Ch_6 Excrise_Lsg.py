# 1.
# 처리조건
# 1). 멤버변수 : 가로(width),세로(height)
# 2). 생성자 : 가로(width),세로(height) 멤버 변수 초기화
# 3). 메서드(area_calc) : 사각형의 넓이 구하는 함수 / 사각형 넓이 = 가로 * 세로
# 4). 메서드(circum_calc) : 사각형의 둘레는 구하는 함수 / 사각형 둘레 = (가로 + 세로) * 2

print('사각형의 넓이와 둘레를 계산합니다.')
w = int(input('사각형의 가로 입력 : '))
h = int(input('사각형의 세로 입력 : '))
class total_calc :
    w = h = 0
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area_calc(self):
        a = self.w * self.h
        return a
    def circum_calc(self):
        b = (self.w + self.h) * 2
        return b
gyu = total_calc(w, h)
lee = gyu.area_calc()
soon = gyu.circum_calc()
print('사각형의 넓이 : ', lee)
print('사각형의 둘레 : ', soon)

# 2.
# 산포도
from statistics import mean
from math import sqrt
data = [5, 9, 1, 7, 4, 6]
def Avg(data):
    avg = mean(data)
    return avg
def var_func(data):
    avg = Avg(data)
    diff = [(d - avg)**2 for d in data]
    var = sum(diff) / (len(data)-1)
    return var
def std_func(data):
    sd = sqrt(var)
    return sd
var = var_func(data)
sd = std_func(data)
print('분산 : ', var)
print('표준편차 : ', sd)

# 3.
# 1). 멤버변수 : 이름(name), 성별(gender), 나이(age)
# 2). 생성자 : 이름, 성별, 나이 초기화
# 3). 메서드 : display(이름, 성별, 나이 출력가능)
name = input('이름 : ')
age = int(input('나이 : '))
gender = input('성별(male/female) : ')
class Person :
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def display(self):
        if self.gender == 'female':
            f_gender = '여자'
        else:
            f_gender = '남자'
        print('이름 : {}, 성별 : {}\n 나이 : {}'.format(self.name, f_gender, self.age))
p = Person(name, age, gender)
p.display()

# 4.
# 1). 키보드로 정규직과 임시직을 구분한다.
# 2). 정규직인 경우에는 기본급과 상여금을 입력해서 급여를 계산한다.
# 3). 임시직인 경우에는 작업시간과 시급을 입력해서 급여를 계산한다.
class Employee:
    name = None
    pay = 0
    def __init__(self, name):
        self.name = name
class Permanent(Employee):
    def __init__(self, name):
        super().__init__(name)
    def pay_calc(self, base, bonus):
        self.pay = base + bonus
        return self.pay
class Temporary(Employee):
    def __init__(self, name):
        super().__init__(name)
    def pay_calc(self, tpay, time):
        self.pay = tpay * time
        return self.pay
empType = input('고용형태 선택(정규직<P>, 임시직<T> : ')
if empType == 'P' or empType == 'p' :
    name = input('이름 : ')
    base = int(input('기본급 : '))
    bonus = int(input('상여금 : '))
    p = Permanent(name)
    print("고용형태 : 정규직")
    print("이름 : ", p.name)
    print("급여 : ", format(p.pay_calc(base, bonus), ',d'))
elif empType == 'T' or empType == 't' :
    name = input('이름 : ')
    tpay = int(input('시급 : '))
    time = int(input('시간 : '))
    t = Temporary(name)
    print("고용형태 : 임시직")
    print("이름 : ", t.name)
    print("급여 : ", format(t.pay_calc(tpay, time), ',d'))
else:
    print('=' * 30)
    print('입력 오류')

# 5.
from myCalcPackage.calcModule import Add, Sub, Mul, Div

x = 10; y = 5
print('Add = ', Add(x,y))
print('Sub = ', Sub(x,y))
print('Mul = ', Mul(x,y))
print('Div = ', Div(x,y))
