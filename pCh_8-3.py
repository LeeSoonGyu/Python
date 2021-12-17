# 특수 파일 처리
# CSV 파일 처리
# 1. 패키지 소환
import pandas as pd # pandas 패키지 import
import os
# 현재 작업 디렉터리 확인
print(os.getcwd())
# 2. csv파일 읽기
score = pd.read_csv('ch08_data/data/score.csv')
print(score.info()) # 파일 정보
print(score.head()) # 칼럼명 포함 앞부분 5개 행 보여줘!
# 3. 칼럼 추출
kor = score.kor # 객체.칼럼명
eng = score['eng'] # 객체['칼럼명']
mat = score['mat']
dept = score['dept']
# 4. 과목별 최고 점수
print('max kor = ', max(kor))
print('max eng = ', max(eng))
print('max mat = ', max(mat))
print('max dept = ', max(dept))
# 5. 과목별 최하 점수
print('min kor = ', min(kor))
print('min eng = ', min(eng))
print('min mat = ', min(mat))
print('min dept = ', min(dept))
# 6. 과목별 평균 점수
from statistics import mean
print('국어 점수 평균 : ', round(mean(kor), 3))
print('영어 점수 평균 : ', round(mean(eng), 3))
print('수학 점수 평균 : ', round(mean(mat), 3))
print('dept 점수 평균 : ', round(mean(dept), 3))
# 7. dept 빈도수
dept_count = {} # 빈 set
for key in dept :
    dept_count[key] = dept_count.get(key, 0) + 1
print(dept_count) # dict

# excel 파일 처리
# 1. excel 파일 읽기
import pandas as pd # pandas 패키지 import
import os
print(os.getcwd())
sam = pd.ExcelFile('ch08_data/data/sam_kospi.xlsx')
# 2. excel 파싱
kospi = soon.parse('sam_kospi')
print(kospi.info())
# 3. 칼럼추출
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = 'C:/Windows/Fonts/malgun.TTF'
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family = font)

price = [305, 450, 320, 460, 330, 480, 380, 520]
year = ['2018 1분기', '2019 1분기','2018 2분기', '2019 2분기','2018 3분기', '2019 3분기','2018 4분기', '2019 4분기']
plt.title('2018년도 vs 2019년도 매출현황 비교')
plt.bar(year, price, width=0.7,  color = 'skyblue') # .bar 세로형 막대