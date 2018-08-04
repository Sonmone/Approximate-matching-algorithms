'''This project adopts neighbourhood search method to predict possible correct spelling posWords
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
#Enghlish alphabet used in this project
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for word in misfile.readlines():
    mislist.append(word.replace("\n", "")) #add each word into mislist[]
for word in corfile.readlines():
    corlist.append(word.replace("\n", "")) #add each word into corlist[]
for word in dicfile.readlines():
    diclist.append(word.replace("\n", "")) #add each word into diclist[]

def getNeighPoint(posResult): #get the point of GED algorithm of each result
    result = [] #storage the correctness in first unit, the length of predicted words in second unit
    if posResult:
        for posword in posResult:
            for corword in corlist:
                if posword == corword:
                    result = [1, len(posResult)]
        if not result:
            result = [0, len(posResult)]
        return result
    else:
        result = [0, 0]
        return result

class NEIGHA(object): #the class of neighbourhood search algorithm
    def repMethod(self, misword):
        lenOfMword = len(misword) #length of misspelled word
        repwords = []
        for index in range(lenOfMword):
            for char in alphabet:
                strMisword = list(misword)
                strMisword[index] = char
                tryword = ''.join(strMisword)
                for dicword in diclist:
                    if tryword == dicword:
                        if tryword not in repwords:
                            repwords.append(tryword)
        return repwords
    def insMethod(self, misword):
        lenOfMword = len(misword) #length of misspelled word
        inswords = []
        for index in range(lenOfMword + 1):
            for char in alphabet:
                strMisword = list(misword)
                strMisword.insert(index, char)
                tryword = ''.join(strMisword)
                for dicword in diclist:
                    if tryword == dicword:
                        if tryword not in inswords:
                            inswords.append(tryword)
        return inswords
    def delMethod(self, misword):
        lenOfMword = len(misword) #length of misspelled word
        delwords = []
        for index in range(lenOfMword):
            for char in alphabet:
                strMisword = list(misword)
                strMisword.pop(index)
                tryword = ''.join(strMisword)
                for dicword in diclist:
                    if tryword == dicword:
                        if tryword not in delwords:
                            delwords.append(tryword)
        return delwords


if __name__ == '__main__': #main function access
    # find possible correct spelling words in dictionary
    prepoint = 0 #the points of correctly predicting words
    prelen = 0 #the length of all prediction
    for misword in mislist:
        neighResult = []
        neigha = NEIGHA()
        neighResult.extend(neigha.repMethod(misword))
        neighResult.extend(neigha.insMethod(misword))
        neighResult.extend(neigha.delMethod(misword))
        neighPoint = getNeighPoint(neighResult)
        prepoint += neighPoint[0]
        prelen += neighPoint[1]
        print("Misspelled Word：" + misword)
        print("Correct Word: " + corlist[mislist.index(misword)])
        print("Predicted Word:", end = " ")
        if neighResult:
            print(neighResult)
        else:
            print("No Prediction")
        print("Score:", end = " ")
        print(str(neighPoint[0]) + " of " + str(neighPoint[1]))
        print("********************************************")
    print("Precision:", end = " ")
    print("%.2f%%" % ((prepoint / prelen) * 100))
    print("Recall:", end = " ")
    print("%.2f%%" % ((prepoint / len(mislist)) * 100))
