from genericpath import isfile
import os

req_path=input("Enter your dir path : ")
if os.path.isfile(req_path):
    print(f"the given {req_path} path is file not a directory")
else:
    all_f_ds=os.listdir(req_path)
    print(f"all files {all_f_ds}")
    if len(all_f_ds)==0:
        print(f"the given path is an empty path")
    else:
        #print("implemetning logic")
        req_ex=input("Enter req file extenstion .py .sh .log : ")
        req_files=[]
        for each_file in all_f_ds:
            if each_file.endswith(req_ex):
                req_files.append(each_file)
        print(f"all requ files {req_files}")
