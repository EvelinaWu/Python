import os
fName = 'c:/data/stu.txt' #要讀取的檔案
if os.path.isfile(fName):
  with open(fName,'a+') as fa: #如果這檔案不存在會自己生成 +就是這個意思
    fa.seek(16)
    str1 = fa.readline()
    print(str1,end='') #從位置去讀東西
    fa.seek(0)
    str1 = fa.readlines()
    print(str1,end='')
    
else:
  print(None)
  
  #UTF-8編碼格式在