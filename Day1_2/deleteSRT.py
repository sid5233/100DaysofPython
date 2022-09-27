import os
path="D:\\DevOps\\Python\\Udemy - Python REST APIs with Flask, Docker, MongoDB, and AWS DevOps"
print("------------------")
for r,d,f in os.walk(path) :
    print(r)
