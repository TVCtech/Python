import os,sys

path = os.path.dirname(sys.argv[0])
script_name = os.path.basename(__file__)

f_list=[]

for files in os.listdir(path) :
    file_path = os.path.join(path, files)
    if files == script_name: # check you are not opening this py script
        break
    else:
        with open(file_path) as file :
            for line in file:
                line = line.strip() 
                f_list.append(line) 

print(f_list)