import os
pName = 'c:/data/'
if os.path.isdir(pName):
    print(f'{pName}路徑為資料夾')
else:
    print(f'{pName}路徑不是資料夾')
    
fName = 'c:/windows/system.ini'
if os.path.exists(fName):
    print(f'{fName}路徑為檔案')
else:
    print(f'{fName}路徑不是檔案')