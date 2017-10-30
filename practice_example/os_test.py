# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:48:56 2017

@author: User
"""

import os
from datetime import datetime
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


#Rename file
os.rename('myfile.txt','ck.txt')
os.rename('ck.txt','myfile.txt')

#檢視檔案
print(os.stat('myfile.txt'))
mod_time=os.stat('myfile.txt').st_mtime

#formate timestamp
print(datetime.fromtimestamp(mod_time))

    
#刪除檔案 
fileName = 'myfile.txt'
if os.path.isfile(fileName):
    os.remove(fileName)
    #os.unlink(fileName)
else:
    print("{} not found!!".format(fileName))
    

#刪除資料夾多個檔案  
os.chdir('D:/')  
os.makedirs('CKLINS/Folder1')
os.chdir('CKLINS/Folder1')
for i in range(0,10):
    fileName = 'file{}'.format(i)
    print(fileName)
    open(fileName,'w').close()
os.chdir('D:/')     
    
if os.path.isdir('D:/CKLINS/Folder1'):
    shutil.rmtree('D:/CKLINS/Folder1')  # remove dir and all contains
else:
    raise ValueError("file {} is not a file or dir.".format('D:/CKLINS/Folder1'))
    
    
#os.walk 回傳一個由三個元素的tuple所組成的串列(資料夾名稱, 下一個資料夾串列, 本資料夾內所有的檔案串列)

for dirpath, dirnames, filenames in os.walk('C:\\Users\\cklin'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()
    
#envrionment
print(os.environ)
print(os.environ.get('HOMEPATH'))

filename = 'test.txt'
file_path = os.environ.get('HOMEPATH') + filename
print(file_path) #bad
file_path = os.path.join(os.environ.get('HOMEPATH'),filename)
print(file_path)


print(os.path.basename('C:\\Java\\jdk1.7.0_79'))
print(os.path.dirname('C:\\Java\\jdk1.7.0_79'))
print(os.path.split('C:\\Java\\jdk1.7.0_79'))
print(os.path.splitext('C:\\Java\\jdk1.7.0_79\\bin\\java.exe'))
print(dir(os.path))


    

    
    