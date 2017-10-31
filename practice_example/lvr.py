# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:16:34 2017

@author: User
"""

import pandas

# 建議先將csv檔做編碼的轉換。 否則容易遇到UnicodeDecodeError

file_path = 'D:\\download\\LVR\\2017S3\\A_lvr_land_A2.CSV'

df = pandas.read_csv(file_path,encoding = 'utf8')
