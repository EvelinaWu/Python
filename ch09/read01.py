import os
fName = 'c:/data/test.txt'
if os.path.isfile(fName):
  fr = open(fName,'r')
  str1 = fr.read(7)
  print(str1)
  print(fr.read())
  fr.close()
else:
  print(f'{fName}檔案路徑不存在')
  
# with open('c:\\data\\stu1.txt','r', encoding='utf-8') as fr:
#   content = fr.read(7)
#   content += fr.read()
#   print(content)
  