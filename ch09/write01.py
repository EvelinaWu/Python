import os
pName = 'c:/data/'
if not os.path.exists(pName):
  os.mkdir(pName)
  fw = open('c:\\data\\stu.txt','w')
  fw .write('王一心,85,90\n')
  fw .write('張三飛,75,87\n')
  fw .write('周五瑞,92,71')
  fw.flush()
  fw.close()
  
with open('c:\\data\\stu1.txt','w', encoding='utf-8') as fr:#新增encoding='utf-8'參數,避免中文亂碼
   fr.write('王一心,85,90\n')
   fr.write('張三飛,75,87\n')
   fr.write('周五瑞,92,71')