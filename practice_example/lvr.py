# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:16:34 2017

@author: User
"""

import pandas
import os
import sys
import re
import shutil

# 建議先將csv檔做編碼的轉換。 否則容易遇到UnicodeDecodeError

file_path = 'D:/download/LVR/analyze/O_新竹市/2015S1-O_lvr_land_A2.CSV'

df = pandas.read_csv(file_path,encoding = 'utf8')

citys = { 'C':'基隆市','A':'臺北市','F':'新北市','H':'桃園縣','O':'新竹市','J':'新竹縣','K':'苗栗縣','B':'臺中市','M':'南投縣','N':'彰化縣','P':'雲林縣','I':'嘉義市','Q':'嘉義縣','D':'臺南市','E':'高雄市','T':'屏東縣','G':'宜蘭縣','U':'花蓮縣','V':'臺東縣','X':'澎湖縣','W':'金門縣','Z':'連江縣'}

source = 'D:/download/LVR/rawData'
target = 'D:/download/LVR/analyze'

#按縣市分
if os.path.isdir(source) and os.path.isdir(target):
    folderList = os.chdir(source)
    for folder in os.listdir():
        print('============={}============'.format(folder))
        for fileName in os.listdir(source + '/' +folder) :
            print(fileName)
            for city in citys:
                cityCode = city
                cityName = citys.get(city)
                parsePattern = city+'_lvr_land_A\.CSV'
                
                pattern = re.compile(parsePattern)
                match = pattern.match(fileName)
                if match :
                    try:
                        targetFolder = target+'/'+cityCode+'_'+cityName
                        if not(os.path.isdir(targetFolder)):
                            os.makedirs(targetFolder) 
                            
                        shutil.copy(source + '/' + folder + '/' + fileName, targetFolder + '/' + folder + '-'+fileName)
                        
                    except IOError as e:
                        print("Unable to copy file. %s" % e)
                    except:
                            print("Unexpected error:", sys.exc_info())

else:
    print("Please make sure path:{} and {} can be found!".format(source,target)) 

# Get-Content tmp.log | Out-File -Encoding UTF8 new.log

#每季的資料按縣市分
#if os.path.isdir(source) and os.path.isdir(target):
#    folderList = os.chdir(source)
#    for folder in os.listdir():
#        print("=========={}=========".format(folder))
#        # 建立目標目錄
#        if not(os.path.isdir(target+'/'+folder)):
#            targetFolder = target+'/'+folder
#            os.mkdir(targetFolder)
#            
#        for fileName in os.listdir(source + '/' +folder) :
#            for city in citys:
#                
#                cityCode = city
#                cityName = citys.get(city)
#                parsePattern = city+'_lvr_land\w*\.CSV'
#                
#                pattern = re.compile(parsePattern)
#                match = pattern.match(fileName)
#                if match :
#                    try:
#                        targetFolder = target+'/'+folder+'/'+cityCode+'_'+cityName
#                        if not(os.path.isdir(targetFolder)):
#                            os.makedirs(targetFolder) 
#                            
#                        shutil.copy(source + '/' + folder + '/' + fileName, targetFolder + '/' + fileName)
#                        
#                    except IOError as e:
#                        print("Unable to copy file. %s" % e)
#                    except:
#                            print("Unexpected error:", sys.exc_info())
#                    
#else:
#    print("Please make sure path:{} and {} can be found!".format(source,target))    