from selenium import webdriver
from selenium.webdriver.common.keys import Keys

with open('inputFile.txt', 'r') as inputfile:
	tiptext  = inputfile.readline().replace('\n', '')
	url = inputfile.readline().replace('\n', '')
	depth = inputfile.readline().replace('\n', '')
	browser = inputfile.readline().replace('\n', '')

inputfile.close()

if browser == "firefox" or browser == "Firefox":
	driver = webdriver.Firefox()
elif browser == "chrome" or browser == "Chrome":
	driver = webdriver.Chrome()
elif browser == "ie" or browser == "IE" or browser == "Ie" or browser == "InternetExplorer" or browser == "internetexplorer" or browser == "Internetexplorer":
	driver = webdriver.Ie()

driver.get(url)
#assert "Python" in driver.title
elems = driver.find_elements_by_tag_name('a')
outputfile = open('outputFile.txt', "a")
for elem in elems:
		my_string = str(elem.get_attribute("href"))
		outputfile.write(my_string + "\n")

driver.close()
