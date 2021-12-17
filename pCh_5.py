# import 모듈명
# from 모듈명 import 함수명1, 함수명2...............

help(len)
dataset = list(range(1,6))
print(dataset)

print('len = ', len(dataset))
print('sum = ', sum(dataset))
print('max = ', max(dataset))
print('min = ', min(dataset))

import statistics
from statistics import variance, stde

print('평균 = ', statistics.mean(dataset))
print('중위 수 = ', statistics.median(dataset))
print('표본 분산 = ', variance(dataset))
print('표본 표준편차 = ', stdev(dataset))

import builtins
dir(builtins)
abs(10)
abs(-10)
abs(-181.1)

all([1, True, 100, -181.22])
all([1, True, 0, 0, 181.22])
all([1, False, 100, 181.22])
all([1, False, 0, 0, -181.22])

any([1, True, 100, -181.22])
any([1, False, 0, 181.22])
any([False, 0, 0])

bin(10)
bin(15)

x = [1, 2, 3, 4, 5]
print(x)
dir(x)
x.append(6)
print(x)
x.remove(6)
print(x)
x.insert(1 ,6)
print(x)

eval("10 + 20")
eval("10 + 20 * 30")
eval(10 + "20 * 30")
eval("20 * 30") + 10

hex(27)

oct(16)

ord('0')
ord('L')
ord('E')
ord('E')
ord('S')
ord('O')
ord('O')
ord('N')
ord('G')
ord('Y')
ord('U')

pow(10, 2)
pow(9, 2)
pow(10000, 2)

round(3.141511)
round(3.14141111, 3)

sorted([3,2,1,5])
sorted([3,2,1,5], reverse=True)

zip([1,3,5], [2,4,6])
list(zip([1,3,5], [2,4,6]))

# 사용자 정의 함수
def userFunc1():
    print('인수가 없는 함수')
    print('userFunc1')
userFunc1()
def userFunc2(x, y):
    print('userFunc2')
    z = x + y
    print('z = ', z)
userFunc2(20, 30) # 도출값 꼭 넣기!!
def userFunc3(x,y):
    print('userFunc3')
    tot = x + y
    sub = x - y
    mul = x * y
    div = x / y

    return tot, sub, mul, div
x = int(input('x 입력 : '))
y = int(input('y 입력 : '))
t, s, m, d = userFunc3(x,y)
print('tot = ', t)
print('sub = ', s)
print('mul = ', m)
print('div = ', d)

# 산포도 구하기
from statistics import mean, variance
from math import sqrt

dataset = [2, 4, 5, 6, 1, 8]
def Avg(data):
    avg = mean(data)
    return avg
print('산술평균 = ', Avg(dataset))

def var_sd(data):
    avg = Avg(data)
    diff = [(d - avg)**2 for d in data]
    var = sum(diff) / (len(data)-1)
    sd = sqrt(var)
    return var, sd
v, s = var_sd(dataset)
print('분산 = ', v)
print('표준편차 =  ', s)

# 피타고라스 정의
def pytha(s, t):
    a = s**2 - t**2
    b = 2* s * t
    c= s**2 + t**2
    print('3변의 길이 : ', a,b,c)
pytha(2, 1)

# 몬테가를로 시뮬레이션
import random
def coin(n):
    result = []
    for i in range(n):
        r = random.randint(0, 1)
        if (r == 1):
            result.append(1) # 앞면
        else:
            result.append(0) # 뒷면0
        return result
print(coin(10))

def montaCoin(n):
    cnt = 0
    for i in range(n):
        cnt += coin(1)[0] # coin 함수 호출

    result = cnt / n # 누적결과 시행 횟수로 나눈다

    return result
print(montaCoin(10))
print(montaCoin(30))
print(montaCoin(100))
print(montaCoin(1000))
print(montaCoin(10000))

# 특수함수(가변인수 함수)
# 튜플형 가변인수
def Func1(name, *names):
    print(name)
    print(names)
Func1('홍길동', '이순신', '유관순')
# 통계량 구하는 함수
from statistics import mean, variance, stdev
def statis(func, *data):
    if func == 'avg':
        return mean(data)
    elif func == 'var':
        return variance(data)
    elif func == 'std':
        return stdev(data)
    else:
        return 'TypeError'
print('avg = ', statis('avg', 1, 2, 3, 4, 5))
print('var = ', statis('var', 1, 2, 3, 4, 5))
print('std = ', statis('std', 1, 2, 3, 4, 5))
# 딕트형 가변인수
def emp_func(name, age, **other):
    print(name)
    print(age)
    print(other)
emp_func('이순규', 31, addr='인천시', height=181, weight=90)
