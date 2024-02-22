#Write a program that prompts for a file name, then opens that file and reads through the file,
#and print the contents of the file in upper case.
#Use the file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt
# Use words.txt as the file name

fileName = input("Enter file name: ")
fileToRead = open(fileName)

#filename.read() returns the whole contents of a file
fileContents = fileToRead.read()
print("Contents of the file ---->\n", fileContents)
fileContentsCAPITAL = fileContents.upper()
print("Contents of the file in Capital---->\n", fileContentsCAPITAL)


#Use this file name, it's downloaded
#assignment_7_1_file.txt