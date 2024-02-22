#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and
#compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name

fileName = input("Enter file name: ")
fileToRead = open(fileName)

numOfLines = 0
sumOfFloatingPoints = 0.0

for line in fileToRead:
    if line.startswith("X-DSPAM-Confidence:"):
        numOfLines = numOfLines + 1
        indexOfZero = line.find('0')
        lastIndex = line.find(line[-1])
        floatingPoint = line[indexOfZero: lastIndex + 1]
        floatingPoint = float(floatingPoint)
        sumOfFloatingPoints = sumOfFloatingPoints + floatingPoint
average = sumOfFloatingPoints / numOfLines
print("Average spam confidence:", average)


#Use this file name, it's downloaded
#assignment_7_2_file.txt

# line = "X-DSPAM-Confidence: 0.6961"
# indexOfZero = line.find('0')
# lastDigit = line[-1]
# lastIndex = line.find(lastDigit)
# floatingPoint = line[indexOfZero: lastIndex+1]
# floatingPoint = float(floatingPoint)
# print(floatingPoint)