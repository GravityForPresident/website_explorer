from selenium import webdriver
from selenium.webdriver.common.keys import Keys

with open('inputFile.txt', 'r') as inputfile:
	tiptext  = inputfile.readline().replace('\n', '')
	url = inputfile.readline().replace('\n', '')
	depth = inputfile.readline().replace('\n', '')
	browser = inputfile.readline().replace('\n', '')

if browser == "firefox" or browser == "Firefox":
	driver = webdriver.Firefox()
elif browser == "chrome" or browser == "Chrome":
	driver = webdriver.Chrome()
	
driver.get(url)
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
