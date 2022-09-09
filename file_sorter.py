import os
import time
import fileinput

# def file_access():


def get_date(filename):  # pass file as parameter here
    # get date of file

    # get Linux epoch time in seconds
    c_time = os.path.getctime(filename)

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
    get_date("img1")
    print("file_sorter.py main")


# only runs if file_sorter.py is run and not main.py
if __name__ == '__main__':
    main()
