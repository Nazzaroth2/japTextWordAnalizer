import time

startTime = time.time()

filepath = "extractedFiles\masterfile.txt"

fileDict = {}

def saveWordInDict(cleanWord):
    if cleanWord in fileDict:
        fileDict[cleanWord] += 1
    else:
        fileDict[cleanWord] = 1


with open(filepath,"r",encoding="utf-8") as textFile:
    with open("cleanNovelList.txt","r",encoding="utf-8") as dictFile:
        for line in textFile:
            # print(line[:-1])
            for word in dictFile:
                cleanWord = word[:-1]
                if cleanWord in line:
                    if word != "\n":
                        saveWordInDict(cleanWord)
                        # print(word[:-1])
            dictFile.seek(0)

lapsedTime = time.time() - startTime
print(lapsedTime)

sortedDict = sorted(fileDict.items(), key=lambda kv: kv[1],reverse=True)
print(sortedDict)