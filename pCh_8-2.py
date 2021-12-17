# 파일 자료 처리
import os
print(os.getcwd())
# 1. 텍스트 디렉터리 경로지정
print(os.getcwd()) # 기본 작업 디렉터리
txt_data = 'ch08_data/txt_data/' # 상대경로 지정
# 2. 텍스트 디렉터리 목록 반환
sub_dir = os.listdir(txt_data) # txt_data 목록반환
print(sub_dir)
# 3. 각 디렉터리 텍스트 자료 수집 함수
def textpro(sub_dir):
    first_txt = [] # first 디렉터리 텍스트 저장
    second_txt = [] # second 디렉터리 텍스트 저장
    # 3-1 디렉터리 구성
    for sdir in sub_dir:
        dirname = txt_data + sdir # 디렉터리 구성
        file_list = os.listdir(dirname) # 파일 목록 반환
        # 3-2 파일 구성
        for fname in file_list:
            file_path = dirname + '/' + fname # 파일 구성
            # 3-3 file 선택
            if os.path.isfile(file_path):
                try :
                    # 3-4 텍스트 자료 수집
                    file = open(file_path, 'r')
                    if sdir == 'first':
                        first_txt.append(file.read())
                    else:
                        second_txt.append(file.read())
                except Exception as e:
                    print('예외 발생 : ', e)
                finally:
                    file.close()
    return first_txt, second_txt # 텍스트 자료반환
# 4. 함수 호출
first_txt, second_txt = textpro(sub_dir)
# 5. 수집한 텍스트 자료 확인
print('first_tex 길이 = ', len(first_txt))
print('second_tex 길이 = ', len(second_txt))
# 6. 텍스트 자료 결합
tot_texts = first_txt + second_txt
print('tot_texts 길이 = ', len(tot_texts))
# 7. 전체 텍스트 내용
print(tot_texts)
print(type(tot_texts))

# pickle 저장
# 1. pickle 모듈
import pickle # file save
# 2. file save : write binary
pfile_w = open('ch08_data/data/tot_texts.pck', mode='wb')
pickle.dump(tot_texts, pfile_w)
# 3. file load : read binary
pfile_r = open('ch08_data/data/tot_texts.pck', mode='rb')
tot_texts_read = pickle.load(pfile_r)
print('tot_texts 길이 = ', len(tot_texts_read))
print(type(tot_texts_read))
print(tot_texts_read)

# 이미지 파일 이동
import os # dir or file path
os.getcwd()
from glob import glob # *, ? 파일 검색
# 1. image 파일 경로
print(os.getcwd())
img_path = 'ch08_data/images' # 이미지 원본 디렉터리
img_path2 = 'ch08_data/images2' # 이미지 이동 디렉터리
# 2. 디렉터리 존재 유무
if os.path.exists(img_path):
    print('해당 디렉터리가 존재합니다.')
    # 3. image 파일저장, 파일이동 디렉터리 생성
    images = [] # png 파일 저장
    os.mkdir(img_path2) # 디렉터리 생성
    # 4. images 디렉터리에서 png 검색
    for pic_path in glob(img_path + '*.png'): # png검색
        # 5. 경로와 파일명 분리, 파일명 추가
        img_path = os.path.split(pic_path)
        images.append(img_path[1]) #png 파일명 추가
        # 6. 이진파일 읽기
        rfile = open(file=pic_path, mode='rb')
        output = rfile.read()
        # 7. 이진파일 쓰기 -> ch08_data/png 폴더이동
        wfile = open(img_path2 + img_path[1], mode='wb')
        wfile.write(output)
    rfile.close(); wfile.close() # 파일 객체 닫기
else:
    print('해당 디렉터리가 없음')
print('png file = ', images)