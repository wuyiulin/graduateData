#coding:utf-8

fname1 = r'F:\GitHubData\graduateData\true_data.txt'
#fname2 = r'F:\graduateData\trun.txt'
import numpy as np
from sklearn import linear_model
import linecache
import matplotlib.pyplot as plt
import time
from sklearn.preprocessing import PolynomialFeatures

row = 270
#row3 = row/3
Hour = 0
Minute = 0
Sec = 0
X_axix = np.zeros((90), dtype=np.float64)
Y_axix = np.zeros((90), dtype=np.float64)
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



#多餘文件處理區
while Line_amount > (row-1):
    with open(fname1, 'r') as old_file:
        with open(fname1, 'r+') as new_file:
            current_line = 1
            while current_line < (row+1):
                 old_file.readline()
                 current_line += 1
            seek_point = old_file.tell()
            new_file.seek(seek_point, 0)
            old_file.readline()
            next_line = old_file.readline()
            while next_line:
                new_file.write(next_line)
                next_line = old_file.readline()
            new_file.truncate()
        new_file.close()
    Line_amount = Line_amount - 1
    #old_file.close()
Line_amount = len(open(fname1,'r').readlines())
print('這是已處理後的行數:'+str(Line_amount))



#開檔計算數據並預測
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

    minX = min(X_axix)
    maxX = max(X_axix)
    '''
    X = np.arange(minX,maxX).reshape((int(Count/3), 1))
    print('這是X: '+str(X))
    '''
    #Y_axix.reshape((1,-1)
    print(list(Coe_X_axix))
    print(list(Coe_Y_axix))



    #選取分析方法
    #regr = linear_model.LinearRegression()
    regr = linear_model.LogisticRegression()
    '''
    poly_reg = PolynomialFeatures(degree = 2)
    X_poly = poly_reg.fit_transform(X_axix)
    '''
    regr.fit((Coe_X_axix), list(Coe_Y_axix))
    #regr.fit((X_poly), (Y_axix))


    print('Coefficients: \n', regr.coef_)
    #print(Count)
    Y_axix_pred = regr.predict(Coe_X_axix)
    R_squared = regr.score((Coe_X_axix), list(Coe_Y_axix))
    print(Y_axix_pred)
    H = int(regr.predict(Count)/3600)
    M = int((regr.predict(Count)/60)%60)
    S = int(regr.predict(Count)%60)
    print('預估明天回家時間: '+str(H)+':'+str(M)+':'+str(S))
    print('R_squared: '+str(R_squared))



    #畫圖區
    plt.figure()
    plt.xlim((0, 90))
    plt.ylim((0, 86399))
    T = np.arctan2(Y_axix,X_axix)
    plt.scatter(X_axix, Y_axix, s=100, c=T, alpha=.5)
    plt.xlabel('nearly 90day')
    plt.ylabel('Total Sec')
    plt.plot(X_axix, Y_axix_pred, 'blue', 20)
    #plt.plot(X, regr.predict(poly_reg.fit_transform(X)), 'blue', 20)
    x_trick = np.arange(0, 90, 5)
    y_trick = np.arange(0, 86300, 10000)
    plt.xticks(x_trick)
    plt.yticks(y_trick)
    plt.show()
    