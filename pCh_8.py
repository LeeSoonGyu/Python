# 예외처리
# for i in () -> ()담긴 변수를 i에 하나 씩 끄집어 내라.
# print(i) -> 끄집어낸 변수를 처리 결과값이 i

# 예외 발생 코드
print(' 프로그램 시작 !!! ')
x = [10, 20, 30, 'num', 40, 50]
for i in x:
    print(i)
    y = i**2
    print('y = ', y)
print(' 프로그램 종료 ')
# 예외 처리 코드
print(' 프로그램 시작 !!! ')
for i in x :
    try:
        y = i**2
        print('i = ', i, 'y = ', y)
    except:
        print('숫자 아님 = ', i)
print(' 프로그램 종료 ')

# 종합 예외처리
# 유형별 예외처리
print('\n유형별 예외처리')
try:
    div = 1000 / 2.53
    print('div = %5.2f' %(div))# 정상
    f = open('c:\\test.txt')# 2차 파일 열기
    div = 1000 / 0  # 1차 산술적 예외
    num = int(input('숫자 입력 : '))# 기타 예외
    print('num = ', num)

# 다중 예외 처리 클래스
# except ZeroDivisionError as e:# 산술적 예외
#     print('오류 정보 : ', e)
except FileNotFoundError as e:# 파일 열기 예외처리
    print('오류 정보 : ', e)
except Exception as e:# 기타 예외 처리 // 통합적으로 쓸 수 있지만 어떤 오류인지를 알수는 없다.
    print('오류 정보 : ', e)
# finally:
#     print('finally 영역 - 항상 실행되는 영역')

# 텍스트 파일 입출력
# 현재 작업 디렉터리
import os
print('\n현재 경로 : ', os.getcwd())
# 예외 처리
try :
    ftest1 = open('ch08_data/data/ftest.txt', mode='r')
    print(ftest1.read())
    ftest2 = open('ch08_data/data/ftest2.txt', mode='w')
    ftest2.write('my first text~~~')
    ftest3 = open('ch08_data/data/ftest2.txt', mode='a')
    ftest3.write('\nmy second text ~~~')
    ftest4 = open('ch08_data/data/ftest4.txt', mode='w')
    ftest4.write('with open file test')
except Exception as e :
    print('Error 발생 : ', e)
finally:
    ftest1.close()
    ftest2.close()
    ftest3.close()
    ftest4.close()

# 추가적 데이터 생성해보기 ~~~~

# 텍스트 자료 읽기
import os
print('\n현재 경로 : ', os.getcwd())
try :
    ftest = open('ch08_data/data/ftest.txt', mode='r')
    full_text = ftest.read()
    print(full_text)
    print(type(full_text))
    ftest = open('ch08_data/data/ftest.txt', mode='r')
    lines = ftest.readlines()
    print(lines)
    print(type(lines))
    print('문단 수 : ', len(lines))
    docs = []
    for line in lines:
        print(line.strip())
        docs.append(line.strip())
    print(docs)
    ftest = open('ch08_data/data/ftest.txt', mode='r')
    line = ftest.readline()
    print(line)
    print(type(line))
except Exception as e :
    print('Error 발생 : ', e)
finally:
    ftest.close()

# with open 인용해보기
try :
    with open('ch08_data/data/ftest4.txt', mode='w', encoding='utf-8')as ftest:
        ftest.write('파이썬 파일 작성 연습')
        ftest.write('\n파이썬 파일 작성 연습2')
    with open('ch08_data/data/ftest4.txt', mode='r', encoding='utf-8')as ftest:
        print(ftest.read())
except Exception as e:
    print('Error 발생 : ', e)