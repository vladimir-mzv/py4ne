import glob
import re

#print(filenames)

for i in glob.glob("/home/mzv/config/config_files/*.txt"):
    #print(i)
    f = open(i)
    for j in f:
      #  print(j)
        if "ip address " in j:
             print(re.sub('[^0-9,.\ ]','', j))
