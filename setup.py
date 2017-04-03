import os
import pickle
import numpy
import string

def run():
    trainingDataMatrix = None
    trainingLabelsMatrix = None
    testDataMatrix = None
    testLabelsMatrix = None
    bigramList = None
    unigramList = None

    '''
    Check if the cache directory has been created and create it if not
    '''
    if os.path.isdir('cache') == False:
        os.makedirs('cache')

    '''
    Check to see if all the files exist. Recreate them all if something is missing
    '''
    if (os.path.isfile('cache/trainingDataMatrix.p') and os.path.isfile('cache/trainingLabelsMatrix.p') and os.path.isfile('cache/testDataMatrix.p') and os.path.isfile('cache/testLabelsMatrix.p') and os.path.isfile('cache/bigramList.p') and os.path.isfile('cache/unigramList.p')):

        '''
        All the files exist, so load them from the cache
        '''

        print('Loading data from the cache...')

        trainingDataMatrix = pickle.load(open('cache/trainingDataMatrix.p', 'rb'))
        trainingLabelsMatrix = pickle.load(open('cache/trainingLabelsMatrix.p', 'rb'))
        testDataMatrix = pickle.load(open('cache/testDataMatrix.p', 'rb'))
        testLabelsMatrix = pickle.load(open('cache/testLabelsMatrix.p', 'rb'))
        bigramList = pickle.load(open('cache/bigramList.p', 'rb'))
        unigramList = pickle.load(open('cache/unigramList.p', 'rb'))

    else:

        print('Creating label matrix strings...')

        trainingData = open('data/trainingText.txt', 'r')
        trainingLabels = open('data/trainingLabels.txt', 'r')
        testData = open('data/testText.txt', 'r')
        testLabels = open('data/testLabels.txt', 'r')

        trainingLabelsString = ''
        for line in trainingLabels:
            trainingLabelsString += ' '
            trainingLabelsString += line
            trainingLabelsString += ';'
        trainingLabelsString = trainingLabelsString[1 : len(trainingLabelsString) - 1]

        testLabelsString = ''
        for line in testLabels:
            testLabelsString += ' '
            testLabelsString += line
            testLabelsString += ';'
        testLabelsString = testLabelsString[1 : len(testLabelsString) - 1]
        
        print('Creating bigram/unigram objects...')

        bigramList = []
        unigramList = []

        currentString = ''
        for line in trainingData:
            if line != '%end text%\n':
                currentString = currentString + ' ' + line
            else:
                splitStrings = currentString.split()
                n = len(splitStrings)
                i = 0
                while i < n:
                    if splitStrings[i] == 'RT':
                        del splitStrings[i]
                        n = n - 1
                    elif '@' in splitStrings[i]:
                        del splitStrings[i]
                        n = n - 1
                    elif '#' in splitStrings[i]:
                        del splitStrings[i]
                        n = n - 1
                    elif 'http' in splitStrings[i]:
                        del splitStrings[i]
                        n = n -1
                    else:
                        splitStrings[i] = splitStrings[i].translate(string.maketrans("",""), string.punctuation)
                        splitStrings[i] = splitStrings[i].lower()
                        i = i + 1
                for i in range(0, len(splitStrings)):
                    if i < (len(splitStrings) - 1):
                        if splitStrings[i] not in unigramList:
                            unigramList.append(splitStrings[i])
                        tempList = []
                        tempList.append(splitStrings[i])
                        tempList.append(splitStrings[i+1])
                        if tempList not in bigramList:
                            bigramList.append(tempList)
                    else:
                        if splitStrings[i] not in unigramList:
                            unigramList.append(splitStrings[i])
                currentString = ''

        print('Creating data matrix strings...')

        trainingData = open('data/trainingText.txt', 'r')

        trainingDataString = ''
        currentString = ''
        for line in trainingData:
            if line == '%end text%\n':
                trainingDataString += ' '
                splitStrings = currentString.split()
                n = len(splitStrings)
                i = 0
                retweet = 0
                at = 0
                hashtag = 0
                link = 0
                while i < n:
                    if splitStrings[i] == 'RT':
                        del splitStrings[i]
                        del splitStrings[i]
                        retweet = 1
                        n = n -2
                    elif '@' in splitStrings[i]:
                        del splitStrings[i]
                        at = 1
                        n = n -1
                    elif '#' in splitStrings[i]:
                        del splitStrings[i]
                        hashtag = 1
                        n = n - 1
                    elif 'http' in splitStrings[i]:
                        del splitStrings[i]
                        link = 1
                        n = n - 1
                    else:
                        splitStrings[i] = splitStrings[i].translate(string.maketrans("",""), string.punctuation)
                        splitStrings[i] = splitStrings[i].lower()
                        i = i + 1
                trainingDataString = trainingDataString + str(retweet) + ' ' + str(at) + ' ' + str(hashtag) + ' ' + str(link) + ' '
                for i in range(0, len(unigramList)):
                    if unigramList[i] in splitStrings:
                        trainingDataString += '1 '
                    else:
                        trainingDataString += '0 '
                tempList = []
                for i in range(0, len(splitStrings) - 1):
                    tempItem = []
                    tempItem.append(splitStrings[i])
                    tempItem.append(splitStrings[i+1])
                    tempList.append(tempItem)
                for i in range(0, len(bigramList)):
                    if bigramList[i] in tempList:
                        trainingDataString += '1 '
                    else:
                        trainingDataString += '0 '
                currentString = ''
                trainingDataString = trainingDataString[0 : len(trainingDataString) - 1]
                trainingDataString += ';'
            else:
                currentString = currentString + ' ' + line
        trainingDataString = trainingDataString[1 : len(trainingDataString) - 1]

        testDataString = ''
        currentString = ''
        for line in testData:
            if line == '%end text%\n':
                testDataString += ' '
                splitStrings = currentString.split()
                n = len(splitStrings)
                i = 0
                retweet = 0
                at = 0
                hashtag = 0
                link = 0
                while i < n:
                    if splitStrings[i] == 'RT':
                        del splitStrings[i]
                        del splitStrings[i]
                        retweet = 1
                        n = n -2
                    elif '@' in splitStrings[i]:
                        del splitStrings[i]
                        at = 1
                        n = n -1
                    elif '#' in splitStrings[i]:
                        del splitStrings[i]
                        hashtag = 1
                        n = n - 1
                    elif 'http' in splitStrings[i]:
                        del splitStrings[i]
                        link = 1
                        n = n - 1
                    else:
                        splitStrings[i] = splitStrings[i].translate(string.maketrans("",""), string.punctuation)
                        splitStrings[i] = splitStrings[i].lower()
                        i = i + 1
                testDataString = testDataString + str(retweet) + ' ' + str(at) + ' ' + str(hashtag) + ' ' + str(link) + ' '
                for i in range(0, len(unigramList)):
                    if unigramList[i] in splitStrings:
                        testDataString += '1 '
                    else:
                        testDataString += '0 '
                tempList = []
                for i in range(0, len(splitStrings) - 1):
                    tempItem = []
                    tempItem.append(splitStrings[i])
                    tempItem.append(splitStrings[i+1])
                    tempList.append(tempItem)
                for i in range(0, len(bigramList)):
                    if bigramList[i] in tempList:
                        testDataString += '1 '
                    else:
                        testDataString += '0 '
                currentString = ''
                testDataString = testDataString[0 : len(testDataString) - 1]
                testDataString += ';'
            else:
                currentString = currentString + ' ' + line
        testDataString = testDataString[1 : len(testDataString) - 1]

        print('Converting to matrices...')
        trainingDataMatrix = numpy.matrix(trainingDataString)
        trainingLabelsMatrix = numpy.matrix(trainingLabelsString)
        testDataMatrix = numpy.matrix(testDataString)
        testLabelsMatrix = numpy.matrix(testLabelsString)

        print('Writing to cache...')
        pickle.dump(trainingDataMatrix, open('cache/trainingDataMatrix.p', 'wb'))
        pickle.dump(trainingLabelsMatrix, open('cache/trainingLabelsMatrix.p', 'wb'))
        pickle.dump(testDataMatrix, open('cache/testDataMatrix.p', 'wb'))
        pickle.dump(testLabelsMatrix, open('cache/testLabelsMatrix.p', 'wb'))
        pickle.dump(bigramList, open('cache/bigramList.p', 'wb'))
        pickle.dump(unigramList, open('cache/unigramList.p', 'wb'))

        print('Cache created!')
    
    return (trainingDataMatrix, trainingLabelsMatrix, testDataMatrix, testLabelsMatrix)
