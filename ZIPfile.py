import zipfile, os
os.chdir(r'F:\\')
exampleZip = zipfile.ZipFile('example.zip')
print(exampleZip.namelist())
print(os.listdir('F:\\'))

textInfo = exampleZip.getinfo('New Text Document 1.txt')
print(textInfo)

print(textInfo.file_size)

print(textInfo.compress_size)

#exampleZip.close()

#Extracting from ZIP Files

exampleZip.extractall('F:\\anotherzip')  #if path is not given will extract in current dir
exampleZip.extract('New Text Document 1.txt')

import zipfile
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)  #zipfile.ZIP_DEFLATED. (This specifies the deflate compression algorithm, which works well on all types of data.)
newZip.close()