from genericpath import isfile
import os

path = str(os.listdir('.'))



list_of_files = []

for root, dirs, files in os.walk(path):
	for file in files:
		list_of_files.append(os.path.join(root,file))
for name in list_of_files:
    print(name)