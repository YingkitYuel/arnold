import base64
import hashlib
import os
import shutil
import urllib.request

import math
import requests
import time


def image_to_base64(image_path):
    with open(image_path, 'rb') as img_file:
        img_string = base64.b64encode(img_file.read())
    return img_string


def movefile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(dstfile)  # 分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)  # 创建路径
        shutil.move(srcfile, dstfile)  # 移动文件
        print("move %s -> %s" % (srcfile, dstfile))


def copyfile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(dstfile)  # 分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)  # 创建路径
        shutil.copyfile(srcfile, dstfile)  # 复制文件
        print("copy %s -> %s" % (srcfile, dstfile))


def download(url, filename, suffix=None):
    if suffix:
        filename = str(filename) + '.' + suffix
    else:
        filename = str(filename)
    print(filename)
    try:
        urllib.request.urlretrieve(url, str(filename))
    except urllib.error.HTTPError:
        time.sleep(60)
        urllib.request.urlretrieve(url, str(filename))
    finally:
        return


def request_download(url, file):
    r = requests.get(url)
    with open(file, 'wb') as f:
        f.write(r.content)
    f.close()


def md5(src):
    m2 = hashlib.md5()
    src = src.encode(encoding='utf-8')
    m2.update(src)
    return m2.hexdigest()


# 如果key不存在返回''
def safekey(d, key):
    if key in d:
        return d[key]
    else:
        return ''


# 将一个list均分成几个list便于多线程使用
# @param full_list 需要被切割的list
# @param count 切割的数量，不一定与设置的count完全一直。例：4条数据，切割成3个。只能切割成2个，每个数组2条数据
# @return [[],[]]
def slice_list(full_list, count):
    result = []
    _len = len(full_list)
    # 向上取整
    every_list_len = math.ceil(_len / count)
    start_index = 0
    # group_id = 1
    for x in range(count):
        temp = full_list[start_index:start_index + every_list_len]
        if len(temp) > 0:
            # self.logger.debug('第' + str(group_id) + '组数据')
            # group_id = group_id + 1
            # for x in temp:
            #     self.logger.debug(x)
            start_index = start_index + every_list_len
        result.append(temp)
    return result


if __name__ == '__main__':
    # download("http://img.che300.com/inception_img/1557796126354744.jpeg?imageslim", 'E:\\test data\行驶证\第二批\\1', 'jpg')
    # request_download("http://img.che300.com/inception_img/1557796126354744.jpeg?imageslim",
    #                  'E:\\test data\行驶证\第二批\\1.jpg')
    movefile('C:\\Users\Administrator\Desktop\\1.png', 'd:/1.png')
