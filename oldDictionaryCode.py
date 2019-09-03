# with open("novelWordList.txt","r",encoding="utf-8") as wordDict:
#     text = wordDict.read()
#
# lineList = text.split('\n')


# for i in range(10):
#     clean01 = lineList[i].split('\t')
#     word = clean01[1]
#     print(word)


# cleanList = []
# for line in lineList:
#     newLine = line.split('\t')
#     cleanList.append(newLine[1])



# verbIndicator = ['る','ぶ','ぐ','く','む','ぬ','す','つ','う','ず']
# with open("cleanNovelList.txt","r+",encoding="utf-8") as cleanDict:
#     with open("possibleVerbList.txt","w",encoding="utf-8") as verbList:
#         for word in cleanDict:
#             word = word[:-1]
#             if word[-1:] in verbIndicator:
#                 verbList.writelines(word + "\n")

with open("newNovelList.txt","w",encoding="utf-8") as newNovelFile:
    with open("cleanNovelList.txt","r",encoding="utf-8") as cleanDict:
        # dataCleanDict = cleanDict.readlines()
        # cleanDict.seek(0)
        with open("possibleVerbList.txt","r",encoding="utf-8") as verbList:
            readVerbList = verbList.readlines()
            for word in cleanDict:
                if word not in readVerbList:
                    newNovelFile.writelines(word)




#ABOVE CODE WAS ONLY USED TO CLEAN UP WORD LIST

# #f.readline() gives a generator, that yields one word after another
# #now i only need to search every word through the novel texts
# #and count their occurences
# with open("cleanDict.txt","r",encoding="utf-8") as wordDict:
#     for i in range(10):
#         word = wordDict.readline()
#         print(line)