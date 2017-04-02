import sys

inputFileName = sys.argv[1]
inputFile = open(inputFileName, 'r')
outputFileName = sys.argv[2]
outputFile = open(outputFileName, 'w')

lineCount = 1
for line in inputFile:
    if line == '%end text%\n':
        label = input("Classify this: ")
        outputFile.write(str(label) + '\n')
    else:
        print(line)
    lineCount = lineCount + 1

inputFile.close()
outputFile.close()
print("Finished!")
