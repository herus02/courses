import os

def rename_files():
  # (1) get file names from a folder
  file_list = os.listdir(r'/home/felipe/Pictures/prank')
  print file_list

  # (2) for each file, rename filename
  save_path = os.getcwd()
  os.chdir(r'/home/felipe/Pictures/prank')
  for file_name in file_list:
    os.rename(file_name, file_name.translate(None, '0123456789'))
  os.chdir = save_path

rename_files()