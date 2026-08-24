import os
fName = 'c:/data/stu.txt'
if os.path.isfile(fName):
  fr = open(fName,'r')
  lst = fr.readlines()
  for lines in lst:
    print(lines.strip())
  fr.close()
  
else:
  print(f'{fName}檔案路徑不存在')