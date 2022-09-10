import os
import file_sorter as fs

# change to allow custom paths

img_list = []

dir = "/home/runner/Image-File-Sorter/sample pictureset/"


for path, subdirectory, filenames in os.walk(dir):
    for f in filenames:
        date = fs.get_date(f)
        date_and_file = fs.date_associator(date, f)
        img_list.append(date_and_file)

for n in img_list:
    print(1)