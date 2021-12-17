# 1. 모듈 추가
# 형식) import 패키지명.모듈명
import leesoongyu.scatteringpan
# 데이터 셋
data = [1, 3, 1.5, 2, 1, 3.2]
# 산술평균 함수 호출
print('평균 : ', leesoongyu.scatteringpan.Avg(data))
# 분산과 표준편차 함수 호출
var, sd = leesoongyu.scatteringpan.var_sd(data)
print('분산 : ', var)
print('표준편차 : ', sd)
# 2. 모듈 추가 (방법2)
# 형식) from 패키지명.모듈명 import 함수명
from leesoongyu.scatteringpan import Avg, var_sd
print('평균 : ', Avg(data))
var, sd = var_sd(data)
print('분산 : ', var)
print('표준편차 : ', sd)