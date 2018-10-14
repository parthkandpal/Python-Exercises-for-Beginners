import shutil
#Copying files
shutil.copy('F:\\Python Tree\\Folder 1\\New Text Document 1.txt', 'F:\\New folder\\')
#Copying folder

shutil.copytree('F:\\Python Tree\\Folder 1', 'F:\\New folder\\')

#Moving file
#shutil.move('F:\\Python Tree\\Folder 1','F:\\Another Tree')





# os.walk() method for Traversing Tree
import os

for folderName, subfolders, filenames in os.walk('F:\\Python Tree'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')