import time

startTime = time.time()

filepath = "extractedFiles\masterfile.txt"

fileDict = {}
conjDict = {}

def saveWordInDict(word,dict):
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1
    return dict

def filterList(dictList,ignoreList):
    filteredList = []
    for word in dictList:
        if word in ignoreList:
            continue
        else:
            filteredList.append(word)
    return filteredList

def checkForVerbConjugations():
    conjDict = {}
    with open("verbConjList.txt","r",encoding="utf-8") as verbConjFile:
        with open(filepath, "r", encoding="utf-8") as textFile:
            for line in textFile:
                for conjugation in verbConjFile:
                    kanji = findVerbKanji(conjugation[:-1],line)
                    if kanji != None:
                        print(kanji)

                    # conjDict = saveWordInDict(conjugation[:-1],conjDict)
                verbConjFile.seek(0)
    return conjDict

def findVerbKanji(conjugation,line):
    ignorablePossibleKanji = ['で','て','を','お','い','り','だ','が','し','と']
    conjPos = line.find(conjugation)
    if conjPos != -1:
        kanji = line[conjPos - 1]
        if kanji in ignorablePossibleKanji:
            return None
        else:
            return kanji



# conjDict = checkForVerbConjugations()


#open all necessery files:
with open("ignoreList.txt","r",encoding="utf-8") as file:
    ignoreList = file.readlines()
    for pos,word in enumerate(ignoreList):
        ignoreList[pos] = word[:-1]

with open("withoutVerbList.txt","r",encoding="utf-8") as file:
    withoutVerbList = file.readlines()
    for pos,word in enumerate(withoutVerbList):
        withoutVerbList[pos] = word[:-1]
    withoutVerbList = filterList(withoutVerbList, ignoreList)

with open("verbList.txt","r",encoding="utf-8") as file:
    verbList = file.readlines()
    for pos,word in enumerate(verbList):
        verbList[pos] = word[:-1]
    verbList = filterList(verbList, ignoreList)



#big if's if this can be used for all textfile opens or
#if this is too specific for the file i was working on
#when writing this code. needs testing with other textfiles
with open(filepath,"r",encoding="utf-8") as file:
    text = file.readlines()
    for pos,line in enumerate(text):
        if line == '\n':
            del text[pos]
    for pos,line in enumerate(text):
        if line == '\n':
            del text[pos]
    for pos, line in enumerate(text):
        text[pos] = line[:-1]



#analize the text and create the counted Words Dict
for line in text:
    #first loop searching for nouns and adverbs etc.
    for word in withoutVerbList:
        if word in line:
            fileDict = saveWordInDict(word,fileDict)
    #second loop searching for verbs in dictionary form
    for verb in verbList:
        if verb in line:
            fileDict = saveWordInDict(verb,fileDict)
    #third loop searching for conjugated verbs, but saving dictionary form




lapsedTime = time.time() - startTime


sortedDict = sorted(fileDict.items(), key=lambda kv: kv[1],reverse=True)
# sortedDict = sorted(conjDict.items(), key=lambda kv: kv[1],reverse=True)
print(sortedDict)


print(lapsedTime)