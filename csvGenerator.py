import sys
import os
from os import walk

def promptUser():
	print("----- CSV Generator -----")
	text = input("Enter path of file containing text:")

	return text

def echoCommaSeperated(path):
	if(path != '.DS_Store'):
		f = open(path, "r")
		text = f.read()
		text = text.splitlines()
		csvData = ""
		for line in text:
			if "CLASS " in line and "SUB CLASS" not in line:
				classNum = line[6:9]

				BI = line[43:52]
				lastSpace = BI.rfind(' ')
				BI = BI[lastSpace+1:52]
				if(line[52:53] == '-'):
					BI = '-'+BI
				
				EI = line[113:121]
				lastSpace = EI.rfind(' ')
				EI = EI[lastSpace+1:121]
				if(line[121:122] == '-'):
					EI = '-'+EI


				csvData += classNum+","+BI+","+EI+"\n"

		csv = open(path[0:-4]+".csv", "w")
		csv.write(csvData)
		csv.close()


#path = promptUser()
mypath = os.path.dirname(os.path.realpath(__file__))
f = []
for(dirpath, dirnames, filenames) in walk(mypath):
	for file in filenames:
		echoCommaSeperated(file)

