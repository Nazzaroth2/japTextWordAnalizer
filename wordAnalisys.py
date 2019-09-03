import time

startTime = time.time()

filepath = "extractedFiles\masterfile.txt"

fileDict = {}

def saveWordInDict(cleanWord):
    if cleanWord in fileDict:
        fileDict[cleanWord] += 1
    else:
        fileDict[cleanWord] = 1

def createDictList(dictList,ignoreListText):
    cleanDictList = []
    for word in dictList:
        if word in ignoreListText:
            continue
        else:
            cleanDictList.append(word[:-1])
    return cleanDictList

#create a dictList that ignores known words
with open("ignoreList.txt","r",encoding="utf-8") as ignoreList:
    with open("cleanNovelList.txt","r",encoding="utf-8") as dictFile:
        filteredDictList = createDictList(dictFile.readlines(),ignoreList.readlines())


#analize the text and create the counted Words Dict
with open(filepath,"r",encoding="utf-8") as textFile:
    for line in textFile:
        for word in filteredDictList:
            if word in line:
                if word != "\n":
                    saveWordInDict(word)



lapsedTime = time.time() - startTime


sortedDict = sorted(fileDict.items(), key=lambda kv: kv[1],reverse=True)
print(sortedDict)


print(lapsedTime)