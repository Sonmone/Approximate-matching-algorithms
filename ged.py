'''This project adopts global edit distance method to predict possible correct spelling posWords
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

def ifEqual(misChar, corChar): #judge if the character in misword equals the character in corword
    if misChar == corChar:
        return matVal
    else:
        return repVal

def getGedaList(scoreList): #get the highest socre possible correct spelling words
    maxScoreList = []
    posWords = []
    temp = scoreList[0]
    for score in scoreList:
        if (score > temp).any():
            temp = score
    for index in range(len(scoreList)):
        if scoreList[index] == temp:
            maxScoreList.append(index)
    for val in maxScoreList:
        if diclist[val] not in posWords:
            posWords.append(diclist[val])
    return posWords

def getGedaPoint(posResult): #get the point of GED algorithm of each result
    result = [] #storage the correctness in first unit, the length of predicted words in second unit
    for posword in posResult:
        for corword in corlist:
            if posword == corword:
                result = [1, len(posResult)]
    if not result:
        result = [0, len(posResult)]
    return result

class GEDA(object): #the class of Global Edit Distance Algorithm
    global insVal #cost of insert
    global delVal #cost of delete
    global repVal #cost of replace
    global matVal #cost of match
    insVal = -1
    delVal = -1
    repVal = -1
    matVal = 1

    def minDistance(self, misword, corword):
        lenOfMword = len(misword) #length of misspelled word
        lenOfCword = len(corword) #length of correct spelling word
        arrTemp = numpy.zeros([lenOfCword, lenOfMword]) #the array storages GED
        for i in range(lenOfCword):
            arrTemp[i][0] = insVal * i #initialize GED array
        for j in range(lenOfMword):
            arrTemp[0][j] = delVal * j #initialize GED array
        for i in range(1, lenOfCword): #adjust GED array
            for j in range(1, lenOfMword):
                arrTemp[i][j] = max((arrTemp[i][j - 1] + delVal), (arrTemp[i - 1][j] + insVal), (arrTemp[i - 1][j - 1] + ifEqual(misword[j - 1], corword[i - 1])))
        return arrTemp[lenOfCword - 1][lenOfMword - 1] #return the score


if __name__ == '__main__': #main function access
    # find possible correct spelling words in dictionary
    prepoint = 0
    prelen = 0
    for misword in mislist: #traverse all the misspelled text
        gedaScore = [] #store the distance(score) of each dictionary entry
        gedaResult = [] #store the results of each misspelled word
        gedaPoint = [] #store the points when predicting correctly
        for dicword in diclist:
            geda = GEDA()
            gedaScore.append(geda.minDistance(misword, dicword))
        gedaResult = getGedaList(gedaScore)
        gedaPoint = getGedaPoint(gedaResult)
        prepoint += gedaPoint[0]
        prelen += gedaPoint[1]
        print("Misspelled Word：" + misword)
        print("Correct Word: " + corlist[mislist.index(misword)])
        print("Predicted Word:", end = " ")
        print(gedaResult)
        print("Score:", end = " ")
        print(str(gedaPoint[0]) + " of " + str(gedaPoint[1]))
        print("********************************************")
    print("Precision:", end = " ")
    print("%.2f%%" % ((prepoint / prelen) * 100))
    print("Recall:", end = " ")
    print("%.2f%%" % ((prepoint / len(mislist)) * 100))
