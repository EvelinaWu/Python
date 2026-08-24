import os
pName = 'c:/data/'
if not os.path.exists(pName):
  os.mkdir(pName)
fa = open('c:/data/stu.txt','a')
fa.write('\n趙七海,66,87')
fa.write('\n陳九東,83,88')
fa.flush()
fa.close()