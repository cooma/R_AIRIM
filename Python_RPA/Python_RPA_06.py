from os import listdir,makedirs
from os.path import isdir
from shutil import copyfile

#경로 설정
orig_dir = "E:\\python\\scandata\\" #원본 데이터 경로
out_dir = "E:\\python\\organized\\"

#orig_dir에 있는 파일 리스트를 file_list에 옮깁니다.

file_list = listdir(orig_dir)
'''
for f_name in file_list:
    f_date = f_name[5:-4]
    f_date = f_date.split('_')
    f_date = f_date[0]
    f_date = f_date.split('-')

    year  = f_date[0]
    month = f_date[1]
    day   = f_date[2]

    #새로운 변수(경로) 생성
    target_dir = out_dir + year + "\\" + month + "\\" + day
    if not isdir(target_dir):
        #makedirs 파일 만들기
        makedirs(target_dir)
    #copyfile(기존 파일 경로,옮길 파일 경로)
    copyfile(orig_dir+f_name, target_dir+ "\\" + f_name)
    print(orig_dir+f_name + " => " + target_dir+"\\" + f_name)
'''
#폴더 내 목록보기
from os import listdir
files = listdir("E:\\python\\organized")
print(files)

#해당 경로에 폴더가 있는지 확인하는 함수
from os.path import exists
if exists("E:\\python\\organized"):
    print("ok")

#해당 경로에 폴더를 생성
'''
from os import makedirs
makedirs("E:\\python\\freefold")
'''
#파일 복사 copyfile(현재, 카피)
from shutil import copyfile
copyfile("E:\\python\\scandata\\TEST_2019-12-02_9-3-3.pdf","E:\\python\\freefold\\copied.pdf")

#폴더 복사, 단 폴더가 이미 존재하는 경우 에러 출력

from shutil import copytree
copytree("E:\\python\\freefold","E:\\python\\freefold2")

#폴더 삭제, 단 폴더가 없는경우 에러 출력
from shutil import rmtree
rmtree("E:\\python\\freefold2")
#파일 삭제,
from os import unlink
unlink("E:\\python\\freefold\\copied.pdf")
