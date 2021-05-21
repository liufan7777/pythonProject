from pathlib import Path

import xlrd
import xlsxwriter


# 操作Excel的工具类
class Excel():
    #声明操作方法
    def __init__(self, type, file_name):
        # 读取excel
        if type == 'r':
            self.workbook = xlrd.open_workbook(file_name)
            self.sheet_names = self.workbook.sheet_names()
            self.list_data = []
        # 写入excel
        elif type == 'w':
            self.workbook = xlsxwriter.Workbook(file_name)

    def read(self):
        # 读取excel
        for sheet_name in self.sheet_names:
            # 通过每个sheetname获取到每个页的内容
            sheet = self.workbook.sheet_by_name(sheet_name)
            rosw = sheet.nrows
            # 遍历取数
            for i in range(0, rosw):
                rowvalues = sheet.row_values(i)
                self.list_data.append(rowvalues)
        # 将得到的list返回进行处理
        return self.list_data



# 测试excel内容提取
# if __name__ == '__main__':
#     files = "../element/element.xls"
#     e = Excel('r', files)
#     list_read = e.read()
#     for i in list_read:
#         print(i)
# 转换为json
def element_tojson(element):
    elements = {}
    for e in element:
        elements[e[0]] = {"type": e[1], "url": e[2]}
    return elements


if __name__ == '__main__':
    files = "../element/element.xls"
    e = Excel("r" , files)
    list_read = e.read()
    ele = element_tojson(list_read)
    print(ele["埋点接口"]["url"])
# 创建文件
def mkdir(p):
    path = Path(p)
    if not path.is_dir():
        path.mkdir()
