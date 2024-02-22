#9.4 Write a program to read through the mbox-short.txt
#and figure out who has the sent the greatest number of mail messages.
#The program looks for 'From ' lines
#and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the
#sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary
#using a maximum loop to find the most prolific committer.

fileName = input("Enter file name: ")
fileToRead = open(fileName)

countMail = dict()
maxMail = 0
maxMailSender = None

for line in fileToRead:
    if line.startswith("From:"):
        line = line.rstrip()
        split = line.split()
        countMail[split[1]] = countMail.get(split[1], 0) + 1

for mail, number in countMail.items():
    # print("Mail sender - ", mail)
    # print("Number of mails sent - ", number)
    if maxMail < number:
        maxMail = number
        maxMailSender = mail

print("Maximum mail sender is - ", maxMailSender)
print("Number of mail sent at max is - ", maxMail)
#Use this file name, it's downloaded
#assignment_9_4_file.txt