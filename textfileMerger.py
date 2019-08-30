import os
import glob

def openFile(path):
    with open(path) as file:
        fileContent = file.read()
    return fileContent

def getFilePath(dirPath,fileNum):
    searchString = fileNum + "*.txt"
    filePath = glob.glob(os.path.join(dirPath,searchString))
    return filePath

def getFilesAmount(dirPath):
    filesAmount = len(os.listdir(dirPath))
    return filesAmount

def getFilledString(fileIntNum):
    return "{:03d}".format(fileIntNum)


dirPath = "extractedFiles"

with open(os.path.join(dirPath,"masterfile.txt"),"a",encoding="utf-8") as masterFile:
    for fileNumInt in range(1,getFilesAmount(dirPath)):
        filePath = getFilePath(dirPath,getFilledString(fileNumInt))[0]
        with open(filePath,"r",encoding="utf-8") as chapterFile:
            masterFile.write(chapterFile.read())


