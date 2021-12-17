# 파일 시스템
# os 모듈의 파일과 디렉터리 관련 함수
import os
os.getcwd() # 현재 작업 경로 확인
# 작업 디렉터리 변경
os.chdir('ch08_data')
os.getcwd()
# 현재 작업 디렉터리 목록 : list반환
os.listdir('.')
# 디렉터리 생성 : 'test'생성
os.mkdir('test3')
os.listdir('.')
os.mkdir('leesoongyu')
os.listdir('.')
# 디렉터리 이동 : 'leesoongyu' 이동
os.chdir('leesoongyu')
os.getcwd()
# 여러 디렉터리 생성
os.makedirs('test/test1/test2/test3/test4/test5/test6/test7')
os.listdir('.')
# 디렉터리 이동
os.chdir('test')
os.getcwd()
os.listdir('.')
# 디렉터리 삭제
os.rmdir('test3')
os.listdir('.')
# 상위 디렉터리로 이동
os.chdir('../..')
os.getcwd()
# 여러 디렉터리 삭제
os.removedirs('test/leesoongyu')

# 경로 관련
import os.path
os.getcwd()
os.path.abspath('lecture/step01_try_except.py')
os.getcwd()
os.path.dirname('lecture/step01_try_except.py')
os.path.exists('D:\\Pywork\\workspace')

# glob 모듈
import glob
os.getcwd()
glob.glob('test.py')
glob.glob('c:/test[0-9]')