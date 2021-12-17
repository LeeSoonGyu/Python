# Ch_2

var1 = " Hello python"
print(var1)
print(id(var1))

var1 = 100
print(var1)
print(id(var1))

var2 = 150.25
print(var2)
print(id(var2))

var3 = True
print(var3)
print(id(var3))

import keyword
python_keyword = keyword.kwlist
print(keyword.kwlist)

var1 = "Hello python"
print(var1)
print(type(var1))

var1 = 100
print(var1)
print(type(var1))

var2 = 150.25
print(var2)
print(type(var2))

var2 = 150.0
print(var2)
print(type(var2))

var3 = True
print(type(var3))

a = int(10.5)
b = int(20.42)
add = a + b
print('add = ', add)

a = float(10)
b = float(20)
add2 = a + b
print('add2 = ', add2)

print(int(True))
print(int(False))
print(int(True))

st = '10'
print(int(st)**2)
# print(st*2) -> 문자열이 두번찍힘.

num1 = 100
num2 = 20
add = num1 + num2
print('add = ', add)
sub = num1 - num2
print('sub = ', sub)
mul = num1 * num2
print('mul = ', mul)
div = num1 / num2
print('div = ', div)
div2 = num1 % num2
print('div2 = ', div2)
div3 = num1 // num2
print('div3 = ', div3)
square = num1**2
print(square)

bool_result = num1 == num2
print(bool_result)
bool_result = num1 != num2
print(bool_result)

bool_result = num1 > num2
print(bool_result)
bool_result = num1 >= num2
print(bool_result)
bool_result = num1 < num2
print(bool_result)
bool_result = num1 <= num2
print(bool_result)

log_result = num1 >= 50 and num2 <= 10
print(log_result)
log_result = num1 >= 50 or num2 <= 10
print(log_result)
log_result = num1 >= 50
print(log_result)
log_result = not(num1 >= 50)
print(log_result)

i = tot = tot2 = 10
print(i)
print(tot2)
i += 1
print(i)
i -= 1
print(i)
i *= 2
print(i)
i /= 2
print(i)

print('출력1', end=" , ")
print('출력2')
print('출력3')

v1, v2 = 100, 200
print(v1, v2)
v2, v1 = v1, v2
print(v1, v2)

lst = [1, 2, 3, 4, 5]
v1, *v2 = lst
print(v1, v2)
v1, v2, *v3 = lst
print(v1, v2, v3)
v1, *v2, v3 = lst
print(v1, v2, v3)

num = input("숫자 입력 : ")
print('num type = ', type(num))
print('num = ', num)
print('num = ', num * 2)

num1 = int(input("숫자 입력 : "))
print('num1 = ', num1*2)

num2 = float(input("숫자 입력 : "))
result = num1 + num2
print('result = ', result)

help(print)

print("value = ", 10 + 20 + 30 + 40 + 50)
print("010", "1234", "5678", sep="-")
print("010", "1234", "5678", sep="")
print("010", "1234", "5678", sep=",")
print("value = ", 10, end=", ")
print("value = ", 20)

print("원주율 = ", format(3.14159, "8.3f"))
print("원주율 = ", format(3.14159, "5.3f"))
print("금액 = ", format(10000, "10d"))
print("금액 = ", format(10000, "15d"))
print("금액 = ", format(100000, "5d"))
print("금액 = ", format(125000, "3,d"))
print("금액 = ", format(125000, "30,d"))

name = "이순규"
age = 31
price = 125.456
print("이름 : %s, 나이 : %d, data = %.2f"%(name, age, price))
print("이름 : {}, 나이 : {}, data={}".format(name, age, price))
print("이름 : {1}, 나이 : {0}, data={2}".format(name, age, price))
print("이름 : {1}, 나이 : {0}, data={2}".format(age, name, price))

oneLine = "this is one line string"
print(oneLine)
multLine = """this is
mult line
string"""
print(multLine)
multLine2 = "this is\nmulti line\nstring"
print(multLine2)

string = "PYTHON"
print(string[0])
print(string[5])
print(string[7])
print(string[-1])
print(string[-6])

print(oneLine)
print("문자열 길이 : ", len(oneLine))
print(oneLine[0:4])
print(oneLine[0:7])
print(oneLine[0:6])
print(oneLine[:4])
print(oneLine[:])
print(oneLine[::2])
print(oneLine[0::2])
print(oneLine[0:-1:2])
print(oneLine[-6:-1])
print(oneLine[-6:])
subString = oneLine[-11:]
subString1 = oneLine[-5:]
print(subString)
print(subString1)

print('t 글자 수 : ', oneLine.count('t'))
print('s 글자 수 : ', oneLine.count('s'))
print(oneLine.startswith('this'))
print(oneLine.startswith('that'))
print(oneLine.replace('this', 'that'))

multLine = """this is
mult line
string"""
sent = multLine.split('\n')
print('문장 : ', sent)

print(oneLine)
words = oneLine.split(' ')
print('단어 : ', words)
sent2 = ','.join(words)
print(sent2)
print(type(sent2))

oneLine2 = 'this is \\two\\ line string'
print(oneLine2)

print('escape 문자 차단')
print('\n출력 이스케이프 문자')
print('\\n출력 이스케이프 기능 차단1')
print(r'\n출력 이스케이프 기능 차단2')
print('path = ', 'C:\Python\test')
print('path = ', 'C:\\Python\\test')
print('path = ', r'C:\Python\test')
print('path = ', 'C:\Python\\\test')


