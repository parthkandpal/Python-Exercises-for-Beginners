import os
print(os.path.join('c:\\','usr','bin','spam'))

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']

for files in myFiles:
    print(os.path.join('C:\\usr\\bin', files))


#The Current Working Directory

print(os.getcwd())
os.chdir('C:\\Windows\\System32')
print(os.getcwd())

#os.chdir('C:\\ThisFolderDoesNotExist')


os.chdir('C:\\Users\\PARTH KANDPAL\\PycharmProjects\\LearningPython')
print(os.getcwd())
#Creating New Folders with os.makedirs()
os.makedirs('D:\\Python\\learningPython\\python')

#Handling Absolute and Relative Paths
print(os.path.abspath('.'))

print(os.path.abspath('.\\Scripts'))

print(os.path.isabs('.'))

os.path.relpath('C:\\Windows', 'C:\\')

os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')



path = 'C:\\Windows\\System32\\calc.exe'
os.path.basename(path)      #calc.exe
os.path.dirname(path)       #C:\Windows\System32

calcFilePath = 'C:\\Windows\\System32\\calc.exe'
os.path.split(calcFilePath)

#Finding File Sizes and Folder Contents

os.path.getsize('C:\\Windows\\System32\\calc.exe')

os.listdir('C:\\Windows\\System32')


totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
      totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))

print(totalSize)

#Checking Path Validity
os.path.exists(path)
os.path.isfile(path)
os.path.isdir(path)



#Open Read Write file
#Open

file_Object=open('C\\Users\\PARTH KANDPAL\\PycharmProjects\\LearningPython\\File.txt')
#Read

content=file_Object.read()
readlines=file_Object.readlines()

#Writing to Files
#write and Append  i.e 'w' and 'a'
file=open('myfile.txt', 'w')
file.write("Hello world \n")
file.close()


file=open('myfile.txt', 'a')
file.write("Appending file and adding more text\n")
file.close()

file=open('myfile.txt')
read=file.read()
print(read)

#Saving Variables with the shelve Module33

import shelve
shelfile=shelve.open('myfile')





















