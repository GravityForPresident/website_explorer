from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def getLinkList (url, szint):
	if browser == "firefox" or browser == "Firefox":
		driver = webdriver.Firefox()
	elif browser == "chrome" or browser == "Chrome":
		driver = webdriver.Chrome()
	elif browser == "ie" or browser == "IE" or browser == "Ie" or browser == "InternetExplorer" or browser == "internetexplorer" or browser == "Internetexplorer":
		driver = webdriver.Ie()

	driver.get(url)
	#assert "Python" in driver.title
	elems = driver.find_elements_by_tag_name('a')
	tempfile = open('tempFile.txt', "a")
	for elem in elems:
			my_string = str(elem.get_attribute("href"))
			if my_string.find("html") > -1:
				tempfile.write(szint + my_string + "\n")
	tempfile.close()
	driver.close()
	
with open('inputFile.txt', 'r') as inputfile:
	tiptext  = inputfile.readline().replace('\n', '')
	url = inputfile.readline().replace('\n', '')
	depth = inputfile.readline().replace('\n', '')
	browser = inputfile.readline().replace('\n', '')
inputfile.close()

outputfile = open('outputFile.txt', "w")
outputfile.write(url + "\n")
outputfile.close()
temp  = open('tempFile.txt', "w")
temp.write(url + "\n")
temp.close()

depth = int(depth)
level = ""

for i in range(0, depth):
	levelPlusOne = level + "\t"
	inputfile2  = open('outputFile.txt', "r")
	for line in inputfile2:
		if line.find(level) > -1:
			getLinkList(line, levelPlusOne)
		else:
			temp  = open('tempFile.txt', "a")
			temp.write(line)
			temp.close()
	inputfile2.close()
	
	inputfile2  = open('outputFile.txt', "w")
	temp  = open('tempFile.txt', "r")
	for line in temp:
		inputfile2.write(line)
	inputfile2.close()
	temp.close()
	
	temp  = open('tempFile.txt', "w")
	temp.write("")
	temp.close()
