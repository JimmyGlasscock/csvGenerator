import sys

def promptUser():
	print("----- CSV Generator -----")
	text = input("Enter path of file containing text:")

	return text

def echoCommaSeperated(path):
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
			
			EI = line[113:121]
			lastSpace = EI.rfind(' ')
			EI = EI[lastSpace+1:121]

			csvData += classNum+","+BI+","+EI+"\n"

	csv = open("classNum.csv", "w")
	csv.write(csvData)
	csv.close()


path = promptUser()
echoCommaSeperated(path)