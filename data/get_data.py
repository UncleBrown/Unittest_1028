#!/usr/bin/python3 
#-*- coding:utf-8

from data import data_config
from lib.OperationExcel import OperationExcel
from lib.OperationJson import OperationJson

class GetData():
    
    def __init__(self):
        self.op_excel = OperationExcel()
    
    def get_case_id(self,row):
        col = data_config.get_id()
        case_id = self.op_excel.get_cell_value(row,col)
        return case_id
    
    #获取sheet行数（case个数）
    def get_case_lines(self):
        lines = self.op_excel.get_sheet_lines()
        return lines
    
    #获取是否执行
    def get_case_run(self,row):
        flag = None
        col = data_config.get_run_info() #获取[是否运行]列数
        #print(f"col:{type(int(col))}")
        result = self.op_excel.get_cell_value(row, col)
        #判断单元格数值
        if result == "yes":
            flag = True
        else:
            flag = False
        return flag
        
    #是否携带header
    def get_case_header(self,row):
        col = data_config.get_is_header() #是否携带header 列
        header_col = data_config.get_header() #header参数 列
        is_header = self.op_excel.get_cell_value(row, col) #获取是都携带header参数
        #对是否携带header进行判断
        if is_header == "yes":
            header = self.op_excel.get_cell_value(row,header_col)
        else:
            header = None
        return header
    #获取请求方式
    def get_case_url_method(self,row):
        col = data_config.get_url_method()
        url_method = self.op_excel.get_cell_value(row, col)
        return url_method
    
    #获取url
    def get_case_url(self,row):
        col = data_config.get_url()
        case_url = self.op_excel.get_cell_value(row, col)
        return case_url
    
    #获取请求数据
    def get_case_data(self,row):
        col = data_config.get_url_data()
        #print(f"url数据行：{col}")
        data = self.op_excel.get_cell_value(row, col)
        #print(f"data:{data}")
        if data == "":
            return None
        return data
        #print(f"data:\n{data}\n")
    #获取测试用例（请求数据）Json关键字对应数值，默认case/rdata.json
    def get_case_data_for_json(self,row):
        oper_json = OperationJson()
        json_key = self.get_case_data(row)
        #print(f"json_key:{json_key}")
        request_json = oper_json.get_json_data(json_key)
        #print(f"request_json:{request_json}")
        return request_json
        
    #获取预期结果
    def get_case_expect(self,row):
        col = data_config.get_expect()
        expect = self.op_excel.get_cell_value(row,col)
        #如果expect不为空则跳过if循环，执行return
        if expect == "":
            return None
        return expect
        
        
if __name__ == "__main__":
    
    excel_data = GetData()
    lines = excel_data.get_case_lines()
    runinfo = excel_data.get_case_run(1)
    print(runinfo)
    
    
