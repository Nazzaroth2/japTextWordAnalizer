# with open("wordDict","r",encoding="utf-8") as wordDict:
#     text = wordDict.read()
#
# lineList = text.split('\n')
#
# cleanList = []
# for line in lineList:
#     newLine = line.split('+')
#     cleanList.append(newLine[0])
#
# with open("cleanDict.txt","w",encoding="utf-8") as cleanDict:
#     for line in cleanList:
#         fullLine = line + '\n'
#         cleanDict.write(fullLine)


#ABOVE CODE WAS ONLY USED TO CLEAN UP WORD LIST

#f.readline() gives a generator, that yields one word after another
#now i only need to search every word through the novel texts
#and count their occurences
with open("cleanDict.txt","r",encoding="utf-8") as wordDict:
    for i in range(10):
        word = wordDict.readline()
        print(line)