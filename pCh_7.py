# 정규 표현식
# 문자열 찾기
import re # 모듈추가(방법1)
from re import findall # 모듈추가(방법2)
st1 = '1234 abc홍길동 ABC_555_6 이사도시'
# 1). 숫자 찾기
print(findall('1234', st1))
print(findall('[0-9]', st1))
print(findall('[0-9]{3}', st1))
print(findall('[0-9]{3,}', st1))
print(findall('\\d{3,}', st1))
# 2). 문자열 찾기
print(findall('[가-힣]', st1))
print(findall('[가-힣]{3}', st1))
print(findall('[가-힣]{3, }', st1))
print(findall('[a-z]', st1)) # 대소문자 구분
print(findall('[A-Z]', st1)) # 대소문자 구분
print(findall('[a-z|A-Z]{3}', st1))
# 3). 특정 위치의 문자열 찾기
st2 = 'test1abcABC 123mbc 45test'
# 접두어 // 접미어
print(findall('^test', st2)) # 접두어
print(findall('st$', st2)) # 접미어
print(findall('^abc', st2)) # 왜 안나오는걸까??
print(findall('bc$', st2)) # 왜 안나오는 걸까??
# 종료 문자 찾기 : abc, mbc
print(findall('.bc', st2))
print(findall('.st', st2))
# 시작 문자 찾기
print(findall('t.', st2))
print(findall('1.', st2))
# 4). 단어 찾기(\\w) - 한글+영문+숫자
st3 = 'test^홍길동 abc 대한*민국 123$tbc'
words = findall('\\w{3,}', st3)
print(words)
# 문자열 제외 : x+(x가 1개 이상 반복)
print(findall('[^^*$]+', st3)) # 특수문자 제외

# 문자열 검사
from re import match # re 모듈 import
# 1). 패턴이 일치된 경우
jumin = '123456-3234567'
result = match('[0-9]{6}-[1-4][0-9]{6}', jumin)
print(result)
if result :
    print('주민번호 일치')
else:
    print('잘못된 주민번호')
# 2). 패턴과 불일치일 경우
jumin1 = '123456-571456'
result1 = match('[0-9]{6}-[1-4][0-9]{6}', jumin1)
print(result1)
if result1 :
    print('주민번호 일치')
else:
    print('잘못된 주민번호')
# 문자열 치환
from re import sub
st4 = 'test^홍길동 abc 대한*민국 123$tbc'
# 1). 특수문자 제거
text1 = sub('[\^*$]+', '', st4)
print(text1)
# 2). 숫자 제거
text2 = sub('[0-9]', '', text1)
print(text2)

# 텍스트 처리
# 올바른 문장 선택
from re import split, match, compile
multi_line = """https://www.naver.com
https://www.daum.net
www.leesoongyu.com"""
# 1). 구분자 이용 문자열 분리
web_site = split('\n', multi_line) #split('pattern',string)
print(web_site)
# 2). 패턴 객체 만들기
pat = compile('https://')
# 3). 패턴 객체 이용 정상 웹 주소 선택하기
sel_site = [site for site in web_site if match(pat, site)]
print(sel_site)

# 자연어 전처리
from re import findall, sub
# 텍스트
texts = ['우리나라 대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!',
'나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 이순규']
# 단계 1 : 소문자 변경
texts_re = [t.lower() for t in texts]
print('texts_re : ', texts_re)
# 단계 2 : 숫자 제거
texts_re1 = [sub('[0-9]', ' ', text)for text in texts_re]
print('texts_re1 : ', texts_re1)
# 단계 3 : 문장 부호 제거
texts_re2 = [sub('[,.?!:;]', '', text)for text in texts_re1]
print('texts_re2 : ', texts_re2)
# 단계 4 : 특수 문자 제거 re.sub() 이용
spec_str = '[@#$%^&*()]'
texts_re3 = [sub(spec_str, '', text)for text in texts_re2]
print('texts_re3 : ', texts_re3)
# 단계 5 : 영문자 제거
texts_re4 = [''.join(findall('[^a-z]', text))for text in texts_re3]
print('texts_re4 : ', texts_re4)
# 단계 6 : 공백 제거
texts_re5 = [' '.join(text.split())for text in texts_re4]
print('texts_re5 : ', texts_re5)

# p.203 실습해볼것!!