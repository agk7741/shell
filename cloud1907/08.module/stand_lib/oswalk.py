import os
import fnmatch

# [(), (), (), ()] -->> n,d,f = ()
files, images = [], ('*.py', '*.gif', '*.jpg', '*.raw')
for dirName, dir_list, file_list in os.walk('../example_train'):
    for ft in images:
        for file in fnmatch.filter(file_list, ft):
            files.append(file)
print(files)


alist = [1, 2, 3]
var01, var02, var03 = alist
_, _, var04 = alist
print(var04)





