#coding:utf-8

fname1 = r'E:\GithubRepo\graduateData\true_data.txt'
#fname2 = r'F:\graduateData\trun.txt'
import numpy as np
from sklearn import linear_model
import linecache 
import matplotlib.pyplot as plt
import time

row = 90
Hour = 0
Minute = 0
Sec = 0
X_axix = np.zeros((30), dtype=np.float64)
Y_axix = np.zeros((30), dtype=np.float64)
Line_amount = 0
"""
#把新的三行資料加進來
old_f = open( fname1, 'r')
write_old_line = old_f.readlines()
new_f = open( fname1, 'w')
new_f.write(time.strftime('%H\n%M\n%S\n', time.localtime()))
new_f.writelines(write_old_line)
new_f.close()
Line_amount = len(open(fname1,'r').readlines())
print('這是未處理前的行數:'+str(Line_amount))
"""
while Line_amount > (row-1):
    with open(fname1, 'r') as old_file:
        with open(fname1, 'r+') as new_file:
            current_line = 1
         # 定位到需要刪除的行
            while current_line < (row+1):
                 old_file.readline()
                 current_line += 1
 
         # 當前光標在被刪除行的行首，記錄該位置
            seek_point = old_file.tell()
 
         # 設置光標位置
            new_file.seek(seek_point, 0)
 
         # 讀需要刪除的行，光標移到下一行行首
            old_file.readline()
         
         # 被刪除行的下一行讀給 next_line
            next_line = old_file.readline()
 
         # 連續覆蓋剩餘行，後面所有行上移一行
            while next_line:
                new_file.write(next_line)
                next_line = old_file.readline()
 
         # 寫完最後一行後截斷文檔，因為刪除操作，文檔整體少了一行，原文檔最後一行需要去掉
            new_file.truncate()
        new_file.close()
    Line_amount = Line_amount - 1
    #old_file.close()
Line_amount = len(open(fname1,'r').readlines())
print('這是已處理後的行數:'+str(Line_amount))
with open(fname1, 'r') as old_file:
    #f = open(fname2,'w+')
    #hour = 0
    #minute = 0
    #sec = 0
    date_List = old_file.readlines()
    #date_List.reverse()
    #print(old_file.readlines())
    #print(date_List)
    #str = ';'.join(list)
    Count = 0
    Count = int(Count)
    print(date_List[0])
    while Count < (row):
        data_Sum = 0
        Hour = float(date_List[Count])*60*60
        #print('這是小時:'+str(Hour))
        Minute = float(date_List[Count + 1])*60
        Sec = float(date_List[Count + 2])
        data_Sum = Hour + Minute + Sec
        X_axix[int(Count/3)] = (int(Count/3))
        Y_axix[int(Count/3)] = data_Sum
        print('這是日期座標：'+ str(X_axix[int(Count/3)]))
        print('這是時間總和：'+ str(Y_axix[int(Count/3)]))
        #print(Count)
        Count = int(Count) + 3
    #print(Hour)
    #f.write(str)
    #print(f.readlines())
    Coe_X_axix = X_axix.reshape((int(Count/3), 1))
    Coe_Y_axix = Y_axix.reshape((int(Count/3), 1))
    #Y_axix.reshape((1,-1)
    print(list(Coe_X_axix))
    print(list(Coe_Y_axix))
    regr = linear_model.LogisticRegression()
    regr.fit((Coe_X_axix), list(Coe_Y_axix))
    r_squared = regr.score((Coe_X_axix), list(Coe_Y_axix))
    print('Coefficients: ', regr.coef_)
    #print(Count)
    print('估計值: '+ str(regr.predict(Count)))
    print('R-squared: '+ str(r_squared))
    #畫圖區
    plt.figure()
    plt.xlim((0, 30))
    plt.ylim((0, 86399))
    T = np.arctan2(Y_axix,X_axix)
    plt.scatter(X_axix, Y_axix, s=75, c=T, alpha=.5)
    plt.xticks(())
    plt.yticks(())
    plt.xlabel('nearly 30day')
    plt.ylabel('Total Sec')
    plt.plot(X_axix, Y_axix)
    plt.show()
