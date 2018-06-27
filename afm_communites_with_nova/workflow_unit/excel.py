# -*- coding:UTF-8 -*-
'''
Created on Jun 28, 2018

@author: Xor
'''
import xlrd
import xlwt
from openpyxl import load_workbook
import numpy as np

def read_excel_file(file_path, sheet_name):
    workbook = load_workbook(file_path)
    # print(workbook.worksheets)
    booksheet = workbook[sheet_name]
    local_rows = booksheet.rows
    data_list = list()
    for local_row in local_rows:
        line = [col.value for col in local_row]
        data_list.append(line)
#         print(line, type(line))
#     print(data_list)
    data_matrix = np.matrix(data_list)
#     print(data_matrix)
    return data_matrix
    