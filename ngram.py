'''This project adopts n-gram distance method to predict possible correct spelling posWords
   in the dictionary of given misspelled words.
   Besides, it also calculates the precision and recall to evaluate this method.
'''

import numpy #a package used in list[]

misfile = open("data\misspell.txt") #open the misspelled text
corfile = open("data\correct.txt") #open the correct spelling text
dicfile = open("data\dictionary.txt") #open the dictionary text
mislist = [] #array to storage misspelled words
corlist = [] #array to storage correct spelling words
diclist = [] #array to storage dictionary words
for word in misfile.readlines():
    mislist.append(word.replace("\n", "")) #add each word into mislist[]
for word in corfile.readlines():
    corlist.append(word.replace("\n", "")) #add each word into corlist[]
for word in dicfile.readlines():
    diclist.append(word.replace("\n", "")) #add each word into diclist[]

def Slice(n, word):
    lisWord = list(word)
    lisWord.insert(0, "#")
    lisWord.insert(len(word) + 1, "#")
    resList = []
    for index in range(len(lisWord) - n + 1):
        str = ''
        for lim in range(index, index + n):
            str += lisWord[lim]
        resList.append(str)
    return resList

def InnerSection(miswordSlice, trywordSlice):
    result = []
    visitMis = []
    visitTry = []
    for i in range(len(miswordSlice)):
        if i not in visitMis:
            for j in range(len(trywordSlice)):
                if j not in visitTry:
                    if miswordSlice[i] == trywordSlice[j]:
                        visitMis.append(i)
                        visitTry.append(j)
                        result.append(miswordSlice[i])
    return len(result)

def getNGramList(scoreList): #get the highest socre possible correct spelling words
    maxScoreList = []
    posWords = []
    temp = scoreList[0]
    for score in scoreList:
        if score < temp:
            temp = score
    for index in range(len(scoreList)):
        if scoreList[index] == temp:
            maxScoreList.append(index)
    for val in maxScoreList:
        if diclist[val] not in posWords:
            posWords.append(diclist[val])
    return posWords

def getNGramPoint(posResult): #get the point of GED algorithm of each result
    result = [] #storage the correctness in first unit, the length of predicted words in second unit
    for posword in posResult:
        for corword in corlist:
            if posword == corword:
                result = [1, len(posResult)]
    if not result:
        result = [0, len(posResult)]
    return result

class NGRAMA(object): #the class of n-gram distance algorithm
    def NgramDistance(self, n, misword, tryword):
        lenOfMword = len(misword) #length of misspelled word
        lenOfCword = len(tryword) #length of temporary trying spelling word
        ngMisword = []
        ngTryword = []
        ngMisword = Slice(n, misword)
        ngTryword = Slice(n, tryword)
        distance = len(ngMisword) + len(ngTryword) - 2 * InnerSection(ngMisword, ngTryword)
        return distance


if __name__ == '__main__': #main function access
    # find possible correct spelling words in dictionary
    prepoint = 0 #the points of correctly predicting words
    prelen = 0 #the length of all prediction
    for misword in mislist:
        ngramScore = []
        ngramResult = []
        ngramPoint = []
        for dicword in diclist:
            ngram = NGRAMA()
            ngramScore.append(ngram.NgramDistance(3, misword, dicword))
        ngramResult = getNGramList(ngramScore)
        ngramPoint = getNGramPoint(ngramResult)
        prepoint += ngramPoint[0]
        prelen += ngramPoint[1]
        print("Misspelled Word：" + misword)
        print("Correct Word: " + corlist[mislist.index(misword)])
        print("Predicted Word:", end = " ")
        print(ngramResult)
        print("Score:", end = " ")
        print(str(ngramPoint[0]) + " of " + str(ngramPoint[1]))
        print("********************************************")
    print("Precision:", end = " ")
    print("%.2f%%" % ((prepoint / prelen) * 100))
    print("Recall:", end = " ")
    print("%.2f%%" % ((prepoint / len(mislist)) * 100))
