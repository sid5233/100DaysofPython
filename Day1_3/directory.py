import os 
cwd = os.getcwd()
print("current working dir is ",cwd)

if os.path.exists('Dir3'):
    print("file exist bhai")
else:
    os.mkdir('Dir3')



os.chdir("D:\\Repositories")
print(os.listdir())
os.chdir(cwd)
print("current working dir is ",cwd)

# os.rename('Dir3',"renamedDir3")

import shutil
shutil.rmtree('Dir1')
print("changed to default", os.listdir())