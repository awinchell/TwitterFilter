output = open('trainingLabels.txt', 'w')
input1 = open('trainingLabels1.txt', 'r')
input2 = open('trainingLabels2.txt', 'r')
input3 = open('trainingLabels3.txt', 'r')
input4 = open('trainingLabels4.txt', 'r')

for line in input1:
    output.write(line)

for line in input2:
    output.write(line)

for line in input3:
    output.write(line)

for line in input4:
    output.write(line)

input1.close()
input2.close()
input3.close()
input4.close()
output.close()
