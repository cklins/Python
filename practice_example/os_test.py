# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:48:56 2017

@author: User
"""

import os
import sys
import shutil

print(os.getcwd())

os.chdir('D:\\') # for windows
os.chdir('D:/') # for unix

#listdir() 列出該目錄下的所有檔案 目錄
print(os.listdir())

# mkdir 只能建一層目錄
os.mkdir('CKLINS/Folder1')  #==>error

# makedirs 可以建多層目錄
os.makedirs('CKLINS/Folder1')

## rmdir 只能刪一層空目錄
os.rmdir('CKLINS/Folder1')

# removedirs 可以多層空目錄
os.removedirs('CKLINS/Folder1')

os.chdir('D:/')


#建立檔案
fileName='myfile.txt'
if not os.path.exists(fileName):
    open(fileName,'w').close

    
#刪除檔案 
fileName = 'myfile.txt'
if os.path.isfile(fileName):
    os.remove(fileName)
    #os.unlink(fileName)
else:
    print("{} not found!!".format(fileName))
    

#刪除資料夾多個檔案    
os.makedirs('CKLINS/Folder1')
os.chdir('CKLINS/Folder1')
for i in range(0,10):
    fileName = 'file{}'.format(i)
    print(fileName)
    open(fileName,'w').close()
    
if os.path.isdir('D:/CKLINS/Folder1'):
    shutil.rmtree('D:/CKLINS/Folder1')  # remove dir and all contains
else:
    raise ValueError("file {} is not a file or dir.".format('D:/CKLINS/Folder1'))
    
    

    

    
    