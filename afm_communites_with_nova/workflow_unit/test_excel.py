# -*- coding:UTF-8 -*-
'''
Created on Jun 28, 2018

@author: Xor
'''
import unittest

from excel import read_excel_file, validate_matrix

class TestExcelMethods(unittest.TestCase):
    def test_read_excel_file(self):
        data_matrix = read_excel_file('../data/test.xlsx', 'setpoints')
        print(data_matrix)
        print(validate_matrix(data_matrix, 3))
    
if __name__ == '__main__':
    unittest.main()