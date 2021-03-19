import os
from os import walk
import re
os.chdir("/home/mzv/config/config_files")
_, _, filenames = next(walk("."))

#print(filenames)

for i in filenames:
    #print(i)
    f = open(i)
    for j in f:
      #  print(j)
        if "ip address " in j:
         #   print(j)
            print(re.sub('[^0-9,.\ ]','', j))
