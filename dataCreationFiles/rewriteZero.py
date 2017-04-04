trainOutput = open('trainingLabels.txt', 'w')
trainInput = open('trainingLabelsOld.txt', 'r')
testOutput = open('testLabels.txt', 'w')
testInput = open('testLabelsOld.txt', 'r')

for line in trainInput:
    if int(line) == 1:
        trainOutput.write('1\n')
    if int(line) == 0:
        trainOutput.write('-1\n')

for line in testInput:
    if int(line) == 1:
        testOutput.write('1\n')
    if int(line) == 0:
        testOutput.write('-1\n')

testInput.close()
testOutput.close()
trainInput.close()
trainOutput.close()
