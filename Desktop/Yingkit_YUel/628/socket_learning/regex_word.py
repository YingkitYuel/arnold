from regex import regex

from excelutil import excelutil


# 发动机正则
# .{0,5}换.{0,10}(发动机|引擎).{0,10}
# .{0,5}换.{0,10}(变速箱|变速器).{0,10}
# .{0,5}换.{0,10}空调.{0,10}
def readfile(file):
    util = excelutil(file, 'r')
    lines = util.read_lines_to_list()
    return lines


d 
def find_word(lines, expression):
    temp=[]
    util = excelutil(mode='w')
    for line in lines:
        buff = ""
        for sentence in line[5].split('\n'):
            for word in regex.finditer(expression, sentence):
                if word.group(0)[2:len(word.group(0))] not in temp:
                    temp.append(word.group(0)[2:len(word.group(0))])
                buff = buff + word.group(0) + "\n"
        util.write_nextline([line[0], line[5], buff], save=False)
    for x in temp:
        print(x)
    util.save()


if __name__ == '__main__':
    lines = readfile('更换空调.xls')
    find_word(lines, r'(更换)([\u4e00-\u9fa5]*)(空调)([^;|；|\(|（|，|,|>|<]*)')
    # a = '更换发动机，'
    # for x in regex.finditer(r'发动机[\（\）\《\》\——\；\，\。\“\”\<\>\！]', a):
    #     print(x.group(0))
