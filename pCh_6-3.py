# 시작점 만들기
# 평균과 제곱근 모듈 import
from statistics import mean
from math import sqrt
# 산술 평균 함수
def Lee(data):
    lee = mean(data)
    return lee
# 분산, 표준편차 함수
def gyu_ss(data):
    lee = Lee(data)
    diff = [(d - lee)**2 for d in data]
    gyu = sum(diff) / (len(data)-1)
    ss = sqrt(gyu)
    return gyu, ss
# 프로그램 시작점
if __name__=="__main__":
    data = [1, 3, 5, 7]
    print('평균 : ', Lee(data))
    gyu, ss = gyu_ss(data)
    print('분산 : ', gyu)
    print('표준편차 : ', ss)
# 시작점이 없는 경우
data = [1, 3, 5, 7]
print('평균 : ', Lee(data))
gyu, ss = gyu_ss(data)
print('분산 : ', gyu)
print('표준편차 : ', ss)
