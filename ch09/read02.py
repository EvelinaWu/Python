import os
fName = 'c:/data/test.txt'
if os.path.isfile(fName):
  with open(fName,'r',encoding='utf-8') as fr:
      str1= fr.readline()
      print(str1,end='')
      str2 = fr.readline(7)
      print(str2)
      print(fr.read())

else:
  print(None)
  
# with open('c:\\data\\stu1.txt','r', encoding='utf-8') as fr:
#   content = fr.read(7)
#   content += fr.read()
#   print(content)
  