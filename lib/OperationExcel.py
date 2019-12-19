#!/usr/bin/python
#-* coding:utf-8 -*-

import xlrd

# #打开excel
# data = xlrd.open_workbook("../case/ymir_web_server.xlsx")
# #获得sheet对象
# sheet = data.sheet_by_index(0)
# #
# print(sheet.nrows)

class OperationExcel():
    
    def __init__(self,filename=None,sheet_id=None):
        
        #容错处理
        if filename:
            self.filename = filename
            self.sheet_id = sheet_id
            #self.data = self.get_data()
        else:
            self.filename = "../case/ymir_web_server.xlsx"
            self.sheet_id = 0
        
    #获取sheet内容 
    def get_data(self):
        data = xlrd.open_workbook(self.filename)
        tables = data.sheet_by_index(self.sheet_id)
        return tables
    
    #获取单元格行数
    def get_sheet_lines(self):
        lines = self.get_data().nrows
        return lines
    
    #获取单元格内容
    def get_cell_value(self,row,col):
        value = self.get_data().cell_value(row,col)
        return value
    
     
if __name__ == "__main__":
    filename = "../case/ymir_web_server.xlsx"
    op_excel = OperationExcel(filename,0)
    result = op_excel.get_data()
    print(result.nrows)    