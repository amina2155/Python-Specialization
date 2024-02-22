#10.2 Write a program to read through the mbox-short.txt
#and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time
#and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


fileName = input("Enter file name: ")
fileToRead = open(fileName)

mapTime = dict()

for line in fileToRead:
    if line.startswith("From"):
        line = line.split()
        line = line[5: -1]
        line = "".join(line)
        if line == "": continue
        line = line.split(':')
        hour = line[0]
        hour = int(hour)
        mapTime[hour] = mapTime.get(hour, 0) + 1

for hour, number in mapTime.items():
    print("Number of mails sent at - ", hour, "is ", number)



# Use this file name, it's downloaded
# assignment_10_2_file.txt