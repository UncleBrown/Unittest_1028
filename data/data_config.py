#!/usr/bin/python3 
#-*- coding:utf-8

class GlobalVar():
    #case_id
    case_id = 0
    casename = 1
    case_url = 2
    case_run_info = 3
    case_url_method = 4
    case_is_header = 5
    case_header = 6
    case_id_depend = 7
    case_data_depend = 8
    case_url_data = 9
    case_expect = 10
    case_result = 11
    
def get_id():
    return GlobalVar.case_id

def get_url():
    return GlobalVar.case_url

def get_run_info():
    return GlobalVar.case_run_info

def get_url_method():
    return GlobalVar.case_url_method

def get_is_header():
    return GlobalVar.case_is_header

def get_header():
    return GlobalVar.case_header

def get_id_depend():
    return GlobalVar.case_id_depend

def get_data_depend():
    return GlobalVar.case_data_depend

def get_url_data():
    return GlobalVar.case_url_data

def get_expect():
    return GlobalVar.case_expect

def get_result():
    return GlobalVar.case_result
