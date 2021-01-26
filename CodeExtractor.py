#Extracts code from a variety, but not all, programming files
import os
from time import sleep

def clear():
	os.system("cls")

def makeFile(name, ext, output):
	try:
		file = open(output + ".txt", "w")
		otherFile = open(name + "." + ext, "r")
		file.write(otherFile.read())
		file.close()
		otherFile.close()
		print("extraction succesful!")
	except:
		print("extraction failed...")

while True:
	myList = []
	print("Code Extractor | JuanR4140\n---")
	print("Enter path to file (C:/Users/juanr/Desktop/MyFiles/)")
	path = input("> ")
	try:
		os.chdir(path)
		myList.append(path)
	except:
		print("error")
		sleep(2)
		clear()
		continue
	print("Enter code extension (py, js, cpp)")
	ext = input("> ")
	myList.append(ext)
	#print(os.listdir())
	print("Enter file name")
	fname = input("> ")
	myList.append(fname)
	print("Enter output file name")
	output = input("> ")
	myList.append(output)
	print("---")
	print("is this correct?")
	print("1. file path -> " + myList[0])
	print("2. file extension -> " + myList[1])
	print("3. file name -> " + myList[2])
	print("4. output file name -> " + myList[3])
	print("file name + path -> " + myList[0] + myList[3] + "." + myList[1])
	print("file name -> " + myList[2] + "." + myList[1])
	print("Y/N")
	corrections = input("> ")
	if corrections.lower() == "y":
		clear()
		print("extracting code, please wait..")
		makeFile(myList[2], myList[1], myList[3])
		input()
		quit()
	else:
		print("try again then!")
		sleep(2)
		clear()
		continue
