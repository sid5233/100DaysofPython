import json

myself = '{"name": "sudarshan","age":29, "profession": "upcoming Devops engineer"}'

myObject = json.loads(myself)
print("Data Type myObject : ", type(myObject))
print("My profession is :", myObject["profession"]) 


myObject["profession"] = "Best DevOps Engineer"
newMyself = json.dumps(myObject)

print("New Person JSON String : ", newMyself)
print("Data Type : ", type(json.dumps(newMyself)))


# String NUMBER lIST BOOLEAN OBJECT NULL