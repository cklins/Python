# 安裝 Python 及其他加載套件

## 下載及安裝 Python

這裡的測試使用 Windows 7 作業系統 及 Python 3.5.2, <br>
Python 可以在 `https://www.python.org/` 下載, <br>
本內容選擇 Python 3.5.2 中的 Windows x86-64 executable installer 安裝程式.<p>

下載後執行安裝程式, <br>
安裝時可選擇 Customize Installation, 如下:<p>
![GitHub Logo](/Python_Basic/images/install01.jpg)

加選 Add Python to environment variables 項目, 如下:<p>
![GitHub Logo](/Python_Basic/images/install02.jpg)


## 修改系統中的環境變數
若前項安裝已選擇 Add Python to environment variables 項目, 此步驟可省略, <br>
否則請進行以下設定:<p>

進入 `控制台` -> `系統` -> `進階系統設定` -> `環境變數`(按鈕)
<p>
選擇 `系統變數` -> `Path`
<p>
假設 Python 安裝在 c:\Python35 資料夾中,<br>
在原內容之後, 貼上 `;c:\Python35;c:\Python\Scripts` , 完成後按確定鍵退出.


## 測試是否安裝成功
在命令提示字元的視窗中, 輸入 `python` , 看看是否出現 Python 的提示符號 `>>>`.<br>
如果有即是安裝成功, 已進入 Python 互動使用者介面畫面;<br>
如果不成功請檢查 `系統變數` 中的 `Path` 是否正確設定.
<p>
同時按下 `Ctrl鍵` 及 `z鍵`, 再按下 `Enter鍵` 即可退出 Python 互動使用者介面. 



## 下載及安裝 Python 加載套件
在 http://www.lfd.uci.edu/~gohlke/pythonlibs/ 下載加載的套件, 本內容下載以下套件:<p>
(1) numpy-1.11.2+mkl-cp35-cp35m-win_amd64.whl <br>
(2) matplotlib-1.5.3-cp35-cp35m-win_amd64.whl <br>
(3) scipy-0.18.1-cp35-cp35m-win_amd64.whl <br>
(4) scikit_learn-0.18-cp35-cp35m-win_amd64.whl <br>
(5) pandas-0.19.1-cp35-cp35m-win_amd64.whl <br>
(6) libsvm-3.21-cp35-cp35m-win_amd64.whl <p>

假設以上檔案存在 D槽的 pyinstall 資料夾中.

在命令提示字元的視窗中, 執行以下命令:
```
d:
cd\pyinstall

pip install numpy-1.11.2+mkl-cp35-cp35m-win_amd64.whl
pip install matplotlib-1.5.3-cp35-cp35m-win_amd64.whl 
pip install scipy-0.18.1-cp35-cp35m-win_amd64.whl 
pip install scikit_learn-0.18-cp35-cp35m-win_amd64.whl 
pip install pandas-0.19.1-cp35-cp35m-win_amd64.whl 
pip install libsvm-3.21-cp35-cp35m-win_amd64.whl
```
安裝畫面如下:<p>
![GitHub Logo](/Python_Basic/images/install03.jpg)

## 關於libsvm
參考: https://github.com/cjlin1/libsvm/tree/master/python


## 安裝 Anaconda<p>
![GitHub Logo](/Python_Basic/images/install04.jpg)


## Anaconda 啟用虛擬環境<p>
![GitHub Logo](/Python_Basic/images/install05.jpg)<p>
![GitHub Logo](/Python_Basic/images/install06.jpg)<p>