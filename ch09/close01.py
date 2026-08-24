import os
pName = 'c:/data/'
if not os.path.exists(pName):
  os.mkdir(pName)
  fName = open('c:\\data\\file01.txt','w')
  fName.close()
  
  
  with open('c:\\data\\file02.txt','w') as fName:
    print()
  