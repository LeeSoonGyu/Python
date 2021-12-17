# Ch_3

var = 10
if var >= 5 :
    print('var = ', var)
    print('var은 5보다 크다')
    print('조건이 참인 경우 실행')

print('항상 실행')
var1 = 3
if var1 >= 5 :
    print('var = ', var1)
    print('var1은 5보다 크다')
    print('조건이 참인 경우 실행')

print('항상 실행')

# 100~85 : '우수', 84~70 : '보통', 69이하 : '저조'
score = int(input('점수 입력 : '))
if score >= 85 and score <= 100 :
    print('우수')
else :
    if score >= 70 :
        print('보통')
    else :
        print('저조')

jump = int(input('점수 입력 : '))
grade = ""
if jump >= 85 and jump <= 100 :
    grade = "우수"
elif jump >= 70 :
    grade = "보통"
else :
    grade = "저조"
print('당신의 점수는 %d이고, 등급은 %s'%(jump, grade))

# score1 = int(input('점수 입력 : '))
# grade1 = ''
# score3 = (score1,grade1) if <= 100 else <-- if else 사용 불가 ㅠㅠ

num = 9
result = 0
if num >= 5 :
    result = num * 2
else :
    result = num + 2
print('result = ', result)
result2 = num * 2 if num >= 5 else num + 2
print('result2 = ', result2)

cnt = tot = 0
while cnt < 5 :
    cnt += 1 # cnt = cnt + 1
    tot += cnt # tot = tot + cnt
    print(cnt, tot)

cnt = tot = 0
dataset = [] # [] <- 빈 리스트
while cnt < 100 : # 100회 반복 시행문
    cnt += 1 # 카운터, cnt = cnt + 1
    if cnt % 3 == 0 :
        tot += cnt # 누적변수, tot = tot + cnt
        dataset.append(cnt)
print('1 ~ 100 사이 3의 배수 합 = %d' % tot)
print('dataset = ', dataset)

numData = [] # 빈 리스트
while True :
    num = int(input("숫자 입력 : "))
    if num % 10 == 0 : # 종료 조건식
        print("프로그램 종료")
        break
    else :
        print(num)
        numData.append(num) # 리스트 추가
print(numData)

import random
help(random)
help(random.random())
r = random.random()
print('r = ', r) # 랜덤 난수 발생

cnt1 = 0
while True :
    r = random.random()
    print(r)
    if r < 0.01 :
        # cnt += 1
        break
    else :
        cnt1 += 1
print('난수 갯수 = ', cnt1)

help(random.randint)
# [1, 5] / {1, 5} / (1, 5)
# [1 <= x <= 5] / {1 <= x < 5} / (1 < x < 5)
help(random.choice)
names = ['홍길동', '이순신', '유관순']  # 파이썬은 0부터시작 기억!!!!!!
print(names)
print(names[2])
if '유관순' in names :
    print('유관순 있음')
else :
    print('유관순 없음')
idx = random.randint(0,2)
print(names[idx])

i = 0
while i < 10 :
    i += 1
    if i == 3 :
        continue
    if i == 6 :
        break
    print(i, end="")

string = "홍길동"
print(len(string))
for s in string :
    print(s)
lstset = [1, 2, 3, 4, 5]
for s in lstset :
    print('원소 = ', s)

range(10)
list(range(10))
num1 = range(10)
print('num1 : ', num1)
num2 = range(1,10)
print('num2 = ', num2)
list(range(1,10))
num3 = range(1, 10, 2)
print('num3 = ', num3)
list(range(1,10,2))

for n in num1 :
    print(n, end=" ")
print()
for n in num2 :
    print(n, end=" ")
print()
for n in num3 :
    print(n, end=" ")

lst = []
for i in range(10) :
    a = random.randint(1,10)
    lst.append(a)
print('lst = ', lst)

for i in range(10) :
    print(lst[i] * 0.25)

for i in range(2, 10) :
    print('---[단]---'.format(i))
    for j in range(1, 10) :
        print('%d * %d = %d'%(i, j, i*j))

address = """나는 이순규 입니다.
주소는 인천시 입니다.
나이는 31세 입니다."""

sents = []
words = []

for sen in address.split(sep="\n") :
    sents.append(sen)
    for word in sen.split() :
        words.append(word)
print('문장 : ', sents)
print('문장 수 : ', len(sents))
print('단어 : ', words)
print('단어 수 : ', len(words))