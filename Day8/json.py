import os,json

def loadJsonData(filePath):
    blankJson = {}
    if os.path.exists(filePath):
        try:
            f = open(filePath, "r")
            data = json.load(f)
            f.close()
            return data
        except ValueError:
            print("Decode eroor")
            return blankJson

def saveJsonData(filePath,data):
    blankJson = {}
    stringifyJsonData = json.dumps(data)
    f = open(filePath,"w")
    f.write(stringifyJsonData)
    f.close()