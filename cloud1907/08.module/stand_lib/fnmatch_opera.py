import os
import fnmatch

# for files in os.listdir('../example_train'):
#     if fnmatch.fnmatch(name=files, pat='*.py'):
#         print(files)

images = ('*.gif', '*.png', '*.jpg', '*.raw')
text = ('*.txt', '*.docx', '*.xlsx', '*.pptx')
for files in os.listdir('../example_train'):
    for ft in images:
        if fnmatch.fnmatch(name=files, pat=ft):
            print(files)
