#coding:utf-8

fname1 = r'F:\graduateData\Data.txt'
fname2 = r'F:\graduateData\trun.txt'
N = 6
M = 5
Hour = 0
Minute = 0
Sec = 0
data_Sum = 0
Line_amount = 0
import linecache 
Line_amount = len(open(fname1,'r').readlines())
print('這是未處理前的行數:'+str(Line_amount))


while Line_amount > (M):
    with open(fname1, 'r') as old_file:
        with open(fname1, 'r+') as new_file:
            current_line = 1
         # 定位到需要刪除的行
            while current_line < (N+1):
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
    old_file.close()
Line_amount = len(open(fname1,'r').readlines())
print('這是已處理後的行數:'+str(Line_amount))
with open(fname1, 'r') as old_file:
    f = open(fname2,'w+')
    #hour = 0
    #minute = 0
    #sec = 0
    date_List = old_file.readlines()
    date_List.reverse()
    #print(old_file.readlines())
    print(date_List)
    #str = ';'.join(list)
    Count = 0
    print(date_List[0])
    while Count < (N) :
        Hour = Hour + float(date_List[Count])*60*60
        #print('這是小時:'+str(Hour))
        Minute = Minute + float(date_List[Count + 1])*60
        Sec = Sec + float(date_List[Count + 2])
        data_Sum = float(data_Sum) + Hour + Minute + Sec
        print('這是時間總和：'+ str(data_Sum))
        Count = Count + 3
    #print(Hour)

    #f.write(str)
    #print(f.readlines())