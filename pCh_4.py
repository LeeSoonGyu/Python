# Ch_4

str_var = str(object='string')
print(str_var)
print(type(str_var))
print(str_var[0])
print(str_var[-1])

str_var2 = 'string'
print(str_var2)
print(type(str_var2))
print(str_var2[0])
print(str_var2[-1])

lst = [1, 2, 3, 4, 5]
print(lst)
print(type(lst))
for i in lst :
    print(lst[:i])

x = list(range(1, 11))
print(x)
print(x[:5])
print(x[-5:])
print('index 2씩 증가')
print(x[::2])
print(x[::3])
print(x[1::2])
print(x[4::2])

a = ['a', 'b', 'c']
print(a)
b = [10, 20, a, 5, True, '문자열']
print(b[0])
print(b[2])
print(b[2][2])
print(b[2][0])
print(b[2][0:])
print(b[2][1:])

num = ['one', 'two', 'three', 'four']
print(num)
print(type(num))
print(len(num))
num.append('five') # 리스트에 추가. (append)추가함수
print(num)
num.remove('five') # 리스트에서 삭제. (remove)삭제함수
print(num)
num[3] = '4' # 리스트 위치 자리에 변수명 변경
print(num)
num.insert(0, 'zero') # 리스트 []자리에 변수를 추가. (insert)위치지정 추가함수
print(num)

x = [1, 2, 3, 4]
y = [1.5, 2.5]
z = x + y
print(z)
x.extend(y) # 확장(넓혀라). (extend)확장함수, 요소들만 추려 추가.
print(x)
x.append(y) # 요소들만 추려서 추가 X, 리스트 전체적으로 추가.
print(x)
# extend와 append의 차이 꼭 기억할 것!!
lst = [1, 2, 3, 4]
result = lst * 2
print(result)

print(result)
result.sort() # 오름차순 정렬. (sort)오름차순 정렬함수
# 내림차순 sort 같은 함수지만 추가적 입력 (reverse = True) 필요!!
print(result)
result.sort(reverse=True)
print(result)

import random
r = []
for i in range(5) :
    r.append(random.randint(1,5))
print(r)

if 4 in r:
    print('있음')
else:
    print('없음')

x = [2, 4, 1, 5, 7]
print(x)
print(x**2) # error 리스트 이므로 연산을 할 수 없다.
lst = [i**2 for i in x] # x리스트 변수를 i에 하나씩 대입하여 결과도출
print(lst)
num = list(range(1,11))
print(num)
lst2 = [i*2 for i in num if i % 2 == 0]
print(lst2)

t = (10, ) # ,를 쳐야 tuple로 인식을한다. ,없으면 문자 숫자열로 인식
print(t)
print(type(t))
t2 = (1, 2, 3, 4, 5, 3)
print(t2)
print(type(t2))
t3 = 1,2,3
print(t3)
print(type(t3))
print(t2[0], t2[1:4], t2[-1])
# t2[0] = 5 tuple은 요소(변수)변경이 안된다. <-> 리스트와 다름
print(t2)
for i in t2 :
    print(i, end=' ') # end 한줄에 붙여쓰는 함수

if 6 in t2:          # 요소(변수) 검사
    print("6 있다")
else:
    print("6 없다")

t4 = 1, 9, 4, 3
print(t4)
t5 = t4[0], t4[3], t4[2], t4[1]
print(t5)
t6 = t4[1], t4[2] # t4[1:3]
print(t6)

lst = list(range(1, 6))
print(lst)
t3 = tuple(lst)
print(t3)
print(type(t3))
print(len(t3), type(t3))
print(t3.count(3)) #  x.count(?), x란 데이터에 ?의 갯수가 몇개냐
print(t3.index(4))
print(t3[4])
print(t3.index(5))
print(t3.index(-1))
s = {1, 3, 5, 3, 1}
print(len(s))
print(s)
for d in s :
    print(d, end=' ')
print()

s2 = {3, 6}
print(s.union(s2))
print(s.difference(s2))
print(s.intersection(s2))
s3 = {1, 3, 5}
print(s3)
s3.add(7) # set에 변수 추가. add(추가 함수)
print(s3)
s3.discard(7) # set에 변수 삭제. discard(삭제 함수) / remove도 작동함
print(s3)

gender = ['남', '여', '남', '여']
print(gender)
sgender = set(gender)
print(sgender)
lgender = list(sgender)
print(lgender)
print(sgender[0])
print(lgender[1])
print(lgender[0])

dic = dict(key1 = 100, key2 = 200, key3 = 300)
dic['key1'] = 1000
print(dic)
print(type(dic))
person = {'name' : '이순규', 'age' : 31, 'address' : '인천시'}
print(person)
print(person['name'])

a = list(person) # 키값만 보여준다.
print(a)

person['age'] = 32
print(person)
del person['address'] # 키값과 벨류는 같이 움직인다.
print(person)
person['pay'] = 400
print(person)
print(person['age'])
print('age' in person)
print('height' in person)

for key in person.keys(): # 키값만 추출
    print(key)
for v in person.values(): # 벨류값만 추출
    print(v)
for i in person.items(): # 전부 추출
    print(i)

charset = ['abc', 'code', 'band', 'band', 'abc']
wc = {}
for key in charset:
    wc[key] = wc.get(key,0) + 1
print(wc)

# 얕은복사
name = ['이순규', '조청호', '이동욱']
print('name address = ',  id(name))
name2 = name
print('name2address =', id(name2))
print(name)
print(name2)
name2[0] = '박상철'
print(name)
print(name2)
# 깊은복사
import copy
name3 = copy.deepcopy(name)
print(name)
print(name3)
print('name address =', id(name))
print('name3 address=', id(name3))
name[1] = '정지훈'
print(name)
print(name3)

import random
dataset = []
for i in range(10):
    r = random.randint(1, 100)
    dataset.append(r)
print(dataset)

vmax = vmin = dataset[0]

for i in dataset:
    if vmax < i:
        vmax = i
    if vmin > i:
        vmin = i
print('max =', vmax, 'min =', vmin)

# 알고리즘(선택정렬 알고리즘), 오름차순 정렬
lee = [3, 5, 1, 2, 4]
n = len(lee)
print(n)

for i in range(0, n-1):
    for j in range(i+1, n):
        if lee[i] > lee[j]:
            tmp = lee[i]
            lee[i] = lee[j]
            lee[j] = tmp
    print(lee)
print(lee)
# 내림차순 정렬
gyu = [3, 5, 1, 2, 4]
c = len(gyu)
print(c)
for i in range(0, c-1):
    for j in range(i+1, c):
        if gyu[i] < gyu[j]:
            tmp = gyu[i]
            gyu[i] = gyu[j]
            gyu[j] = tmp
    print(gyu)
print(gyu)

# 이진검색 알고리즘
soon = [5, 10, 18, 22, 35, 55, 75, 103]
value = int(input('검색할 값 입력 : '))
low = 0 # start값
high = len(soon)-1 # end값 인덱스가 0부터이기 때문에 -1 넣어주기.
print(high)
loc = 0 # mid값
state = False

while (low <= high):
    mid = (low+high) // 2 # 실수를 버리기위한 연산
    if soon[mid] > value:
        high = mid - 1
    elif soon[mid] < value:
        low = mid + 1
    else:
        loc = mid
        state = True
        break
if state:
    print('찾은 위치 : %d 번째' %(loc+1)) #인덱스는 0부터 시작이기 때문에 1을 더해준다.
else:
    print('찾는 값은 없습니다.')