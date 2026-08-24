import os 
pName = 'c:/data/'
if os.path.isdir(pName):
  print(f'{pName}路徑已存在,不必再建立')
else:
  print(f'{pName}路徑不存在,建立資料夾')
  os.makedirs(pName)
  print(f'{pName}路徑建立成功')
  