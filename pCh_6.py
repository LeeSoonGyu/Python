# 함수와 클래스의 정의 // 함수 클래스의 차이 구분해서 볼 것!!!
# 1) 함수정의
def lee_func(a, b) : # 외부함수
    x = a # 변수 선언 : 자료 저장
    y = b # 변수 선언 : 자료 저장
    def plus() : # 내부함수
        p = x + y
        return p
    def miuns() : # 내부함수
        m = x - y
        return m
    return plus, miuns # 내부 함수 호출
# 함수 호출
p, m = lee_func(-100, 200)
print('합 : ', p())
print('빼기 : ', m())
# 클래스 정의
class leesoongyu_class :
    x = y = 0 # 클래스 변수 및 자료저장
    def __init__(self, a, b): # 생성자 : 객체 생성 및 멤버변수 초기화
        self.x = a
        self.y = b
    def plus(self):
        p = self.x + self.y # 변수 연산
        return p
    def minus(self):
        m = self.x - self.y # 변수 연산
        return m
# 객체 생성
sk = leesoongyu_class(90, 20)
# 멤버 호출
print('합 : ', sk.plus())
print('빼기 : ', sk.minus())

# 클래스 정의 임의 변형
a = 50
b = 80
class gyu_class :
    x = y = 0 #클래스 변수 생성 및 자료저장
    def cal_func(self, a, b):
        self.x = a
        self.y = b # 생성자 : 객체 생성 및 멤버변수 초기화
        return a and b
    def plus(self):
        p = self.x + self.y
        return p
    def minus(self): # 내부 함수 호출 없이 바로 생성의 차이가 있다 (함수는 호출을 해줘야함)
        m = self.x - self.y
        return m
# soon = gyu_class(50, 80) # 객체 생성
# 함수 호출
print('합 = ', plus())
print('빼기 = ', minus())

# 클래스 구성요소
class Car :
    # 멤버변수
    cc = 0 # 엔진 cc
    door = 0 # 문짝 갯수
    carType = None # null
    # 생성자
    def __init__(self, cc, door, carType):
        # 멤버 변수 초기화
        self.cc = cc
        self.door = door
        self.carType = carType # 차 종류
    # 메서드
    def display(self):
        print('자동차는 %d cc이고, 문짝은 %d 개, 타입은 %s'%(self.cc, self.door, self.carType))
# 객체 생성
car1 = Car(2000, 4, '승용차')
car2 = Car(3000, 5, 'SUV')
# 멤버 호출
car1.display()
car2.display()

# 생성자 이용 멤버변수 초기화
class multiply:
    x = y = 0 # 멤버변수
    def __init__(self, x, y): # 생성자 초기화 및 객체만 생성
       self.x = x
       self.y = y
    def mul(self): # 메서드
        return self.x * self.y
lee = multiply(10, 20) # 생성자
print('곱셈 = ', lee.mul())

# 메서드 이용 멤버 변수 초기화
class multply2:
    x = y = 0 # 멤버 변수
    def __init__(self):
        pass # 생성자 없음, 기본 생성자 제공
    def data(self, x, y): # 메서드 멤버 변수 초기화
        self.x = x
        self.y = y
    def mul(self): # 메서드 곱셈
        return self.x * self.y
gyu = multply2() # 기본 생성자
gyu.data(10, 20) # 멤버 변수 적용
print('곱셈 = ', gyu.mul())

# 메서드 이용 멤버 변수 초기화 임의 변형
x = 100
y = 200
class multply2:
    x = y = 0
    def data(self, x, y): # 메서드 멤버 변수 초기화
        self.x = x
        self.y = y
        return x and y
    def mul(self): # 메서드 곱셈
        return self.x * self.y
# gyu = multply2() # 기본 생성자
# gyu.data(10, 20) # 멤버 변수 적용
print('곱셈 = ', gyu.mul())

# self
class multply3: # 멤버변수 없음, 생성자 없음
    def data(self, x, y): # 동적 멤버변수 생성 및 초기화
        self.x = x
        self.y = y
    def mul(self): # 곱셈 연산
        result = self.x * self.y
        self.display(result) # 메서드 호출
    def display(self, result): # 결과 출력
        print('곱셉 = %d'%result)
leesoongyu = multply3()
leesoongyu.data(100, 200)
leesoongyu.mul()

# 클래스 멤버
class DataPro:
    content = '날짜 처리 클래스' # 멤버 변수
    def __init__(self, year, month, day): # 생성자
        self.year = year
        self.month = month
        self.day = day
    def display(self): # 객체 메서드
        print('%d-%d-%d'%(self.year, self.month, self.day)) # 한개씩 대입을 위해 () 필수!!
    @classmethod # 클래스 메서드 / 이 함수는 함수 이름을 매개변수() 받는다. / 함수 장식자
    def data_string(cls, dataStr): # '20211015'
        year = dataStr[:4]
        month = dataStr[4:6]
        day = dataStr[6:]
        print(f'{year}년{month}월{day}일')
# 객체 멤버
data = DataPro(2021,10,15) # 생성자
print(data.content)
print(data.year)
data.display()
print(DataPro.content)
DataPro.data_string('20211015')

# 캡슐화
class Account:
    # 은닉 멤버변수
    __balance = 0 # 잔액
    __accName = None # 예금주
    __accNo = None # 계좌번호
    # 생성자 / 멤버 변수 초기화
    def __init__(self, bal, name, no):
        self.__balance = bal # 잔액 초기화
        self.__accName = name # 예금주
        self.__accNo = no # 계좌번호
    # 계좌정보 확인 Getter
    def getBalance(self):
        return self.__balance, self.__accName, self.__accNo
    # 입금하기 Setter
    def deposit(self, money):
        if money < 0 :
            print('금액확인')
            return # 종료(exit)
        self.__balance += money
    # 출금하기 Setter
    def withdraw(self, money):
        if self.__balance < money:
            print('잔액 부족')
            return # 종료(exit)
        self.__balance -= money
# object 생성
acc = Account(1000000000, '이순규', '111-222-3333-44') # 생성자
# Getter 호출
# acc.__balance # 오류
bal = acc.getBalance()
print('계좌정보 : ', bal)
# Setter 호출
acc.deposit(1500000000) # 15000원 입금
bal = acc.getBalance()
print('계좌정보 : ', bal)
# Setter 호출
acc.withdraw(300000000) # 3000원 출금
bal = acc.getBalance()
print('계좌정보 : ', bal)
acc.withdraw(3000000000) # 30000원 출금

# 상속
# 부모 클래스
class Super:
    # 생성자 : 동적멤버 생성
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 메서드
    def display(self):
        print('name : %s, age : %d'%(self.name, self.age))
sup = Super('부모', 55)
# sup.display() # 부모 멤버 호출
# 자식 클래스
class Sub(Super): # 부모 클래스 상속
    gender = None # 자식 멤버
    # 생성자
    def __init__(self, name, age, gender, year):
        Super.__init__(self, name, age)
        # super().__init__(name, age)
        # self.name = name
        # self.age = age
        self.gender = gender
        self.year = year
    # 메서드 확장
    def display1(self):
        print('name : %s, age : %d, gender : %s, year : %d'%(self.name, self.age, self.gender, self.year))
l = Sub('자식',31,'남자',1991)
sup.display() # 부모 멤버 호출
l.display1() # 자식 멤버 호출

# Super 클래스
# 부모 클래스
class Parent:
    # 생성자 (객체+초기화)
    def __init__(self, name, job):
        self.name = name
        self.job = job
    # 메서드
    def display(self):
        print('name : %s, job : %s'%(self.name, self.job))
p = Parent('이순규', '백수')
p.display()
# 자식 클래스
class Children(Parent): # 부모 클래스 상속
    gender = None # 자식 클래스 멤버변수 추가
    year = 0
    # 자식 클래스 생성자
    def __init__(self, name, job, gender, year):
        Parent.__init__(self, name, job) # 부모 클래스 생성자 호출
        self.gender = gender
        self.year = year
    # 멤버 함수(메서드)
    def display(self): # 함수 재정의
        print('name : %s, jod : %s, gender : %s, year : %d'%(self.name, self.job, self.gender, self.year))
# 자식 클래스 객체 생성
o = Children('이순신', '해군 장군', '남자', 2021)
o.display()

# Super 클래스(2)
# 부모 클래스
class Parent:
    # 생성자 (객체+초기화)
    def __init__(self, name, job):
        self.name = name
        self.job = job
    # 메서드
    def display(self):
        print('name : %s, job : %s'%(self.name, self.job))
p = Parent('이순규', '백수')
p.display()
# 자식 클래스
class Children(Parent): # 부모 클래스 상속
    gender = None # 자식 클래스 멤버변수 추가
    year = 0
    # 자식 클래스 생성자
    def __init__(self, name, job, gender, year):
        super().__init__(name, job) # 부모 클래스 생성자 호출
        self.gender = gender
        self.year = year
    # 멤버 함수(메서드)
    def display(self): # 함수 재정의
        print('name : %s, jod : %s, gender : %s, year : %d'%(self.name, self.job, self.gender, self.year))
# 자식 클래스 객체 생성
o = Children('이순신', '해군 장군', '남자', 2021)
o.display()

# Super 클래스(3)
# 부모 클래스
class Parent:
    # 생성자 (객체+초기화)
    def __init__(self, name, job):
        self.name = name
        self.job = job
    # 메서드
    def display(self):
        print('name : {}, job : {}'.format(self.name, self.job))
p = Parent('이순규', '백수')
p.display()
# 자식 클래스
class Children(Parent): # 부모 클래스 상속
    gender = None # 자식 클래스 멤버변수 추가
    year = 0
    # 자식 클래스 생성자
    def __init__(self, name, job, gender, year):
        super().__init__(name, job) # 부모 클래스 생성자 호출
        self.gender = gender
        self.year = year
    # 멤버 함수(메서드)
    def display(self): # 함수 재정의
        print('name : {}, jod : {}, gender : {}, year : {}'.format(self.name, self.job, self.gender, self.year))
# 자식 클래스 객체 생성
o = Children('이순신', '해군 장군', '남자', 2021)
o.display()

# Super 클래스(4) 외부상수 출력 응용
# 부모 클래스
class Parent:
    # 생성자 (객체+초기화)
    def __init__(self, name, job):
        self.name = name
        self.job = job
    # 메서드
    def display(self):
        print('name : {}, job : {}'.format(self.name, self.job))
p = Parent('이순규', '백수')
p.display()
# 자식 클래스
name = '이순신'
job = '해군 장군'
gender = '남자'
year = 2021
class Children(Parent): # 부모 클래스 상속
    gender = None # 자식 클래스 멤버변수 추가
    year = 0
    # 자식 클래스 생성자
    def __init__(self, name, job, gender, year):
        super().__init__(name, job) # 부모 클래스 생성자 호출
        self.gender = gender
        self.year = year
    # 멤버 함수(메서드)
    def display(self): # 함수 재정의
        print('name : {}, jod : {}, gender : {}, year : {}'.format(self.name, self.job, self.gender, self.year))
result = display()
print('먹어봐 좀 : ', display)