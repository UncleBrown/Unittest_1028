#/usr/bin/python3
#-*- coding:utf8 -*-


from lib.OperationExcel import OperationExcel
from lib.OperationJson import OperationJson
from data.get_data import GetData
from lib.run_method import RunMethod
import json
    
class All_Run():
    
    def __init__(self):
        self.oper_excel = OperationExcel()
        self.oper_json = OperationJson()
        self.get_data = GetData()
        self.run = RunMethod()
        
    def go_on_run(self):
        #获取case行数
        case_lines = self.oper_excel.get_sheet_lines()
        #剔除0行（标题），循环取数据
        for i in range(1,case_lines):
            #case_id = self.get_data.get_case_id(i)
            case_url = self.get_data.get_case_url(i)
            case_runinfo = self.get_data.get_case_run(i) #case是否执行，返回值True/Flase
            case_method = self.get_data.get_case_url_method(i)
            case_header = self.get_data.get_case_header(i)
            #case_header = {'content-type': "application/json"}
            case_data = self.get_data.get_case_data_for_json(i)
            
            #print(type(case_header))
            #print(json.loads(case_header))
            #print(f"case_header:{case_header}\n")
            if case_runinfo:
                #method,url,data=None,header=None
                res = self.run.run_main(case_method,case_url, case_data, case_header)
            else:
                print(f"[info]:用例第{i}调不执行")
            return res
if __name__ == "__main__":
    r = All_Run().go_on_run()
    print(r)
