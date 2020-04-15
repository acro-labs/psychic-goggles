# Firstly, run these two commands on your terminal (Mac) or command prompt (Windows):

# pip install os
# pip install shutil
import os
import shutil
from os import listdir
from os.path import isfile, join


def sort_files_in_a_folder(mypath):
    '''
		A function to sort the files in a download folder
		into their respective categories
		
	'''
    path = os.path.expanduser(mypath)
    files = [f for f in listdir(path) if not f.startswith(".") and isfile(join(path, f))]

    file_type_variation_list = []
    folder_list = []
    filetype_to_folder_dict = {}
    for file in files:
        filetype = file.split('.')[-1]
        if filetype not in file_type_variation_list:
            file_type_variation_list.append(filetype)
            new_folder_name = path + '/' + filetype + '_folder'
            filetype_to_folder_dict[str(filetype)] = str(new_folder_name)
            if os.path.isdir(new_folder_name) == True:  # folder exists
                continue
            else:
                os.mkdir(new_folder_name)

    print('filetype_to_folder_dict', filetype_to_folder_dict)

    for file in files:
        src_path = path + '/' + file
        filetype = file.split('.')[-1]
        if filetype in filetype_to_folder_dict.keys():
            dest_path = filetype_to_folder_dict[str(filetype)]
            shutil.move(src_path, dest_path)
            print(src_path + '>>>' + dest_path)


if __name__ == "__main__":
    mypath = "~/Desktop"
    sort_files_in_a_folder(mypath)
