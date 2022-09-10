import os
import time
import fileinput

# def file_access():

def test_print():
    print("file_sorter.py main ran and printed")

def get_date(filepath):  # pass file as parameter here
    # get date of file

    # get Linux epoch time in seconds
    c_time = os.path.getctime(filepath)

    # convert to local time and create struct_time
    local_time = time.localtime(c_time)

    return local_time


def date_associator(local_time, filename):
    date_and_photo = tuple(local_time, filename)
    return date_and_photo


def sorter():
    # sorts images by date
    os.chdir(out_path)
    os.mkdir("$PATH/")


def main():
    current_directory = os.getcwd()
   
    # print(os.getcwd())
    
    current_directory = (current_directory + "{}").format("/sample pictureset")
    os.chdir(current_directory)
    
    current_file = (current_directory + "{}").format("/img1.jpeg")
    date =  get_date(current_file)
    # print(img1_date)

    print(date)

# only runs if file_sorter.py is run and not main.py
if __name__ == '__main__':
    main()
