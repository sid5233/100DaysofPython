# f = open("sample.txt", "r")
# print(f.read())
# f.close()


# f = open("D:\\Repositories\\100DaysofPython\\sample.txt", "r")
# for  x in f:
#     print(x)
# print(f.read())
# f.close()

# If the file exist
# import os
# if os.path.exists("samplee.txt"):
#     f =open("sample.txt","r")
#     print(f.read())
#     f.close()
# else:
#     print("File does not exist")

#File in append mode if dont exist it will create one
# f = open("sample1.txt","a")
# f.write("We are creting new file")
# f.close()


#Deleting the file
import os
if os.path.exists("sample1.txt"):
    os.remove("sample1.txt")
else:
    print("File does not exist")
