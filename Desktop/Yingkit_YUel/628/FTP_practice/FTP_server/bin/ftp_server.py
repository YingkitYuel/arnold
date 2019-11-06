import os, sys

#因为在执行ftp_server这个文件的时候，系统将该文件所在的路径添加至环境变量，
# 即bin，若直接from core import，则在bin下找不到，所以应该将core添加至环境变量
PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)

from core import main



if __name__ == '__main__':
    main.ArgvHandler()