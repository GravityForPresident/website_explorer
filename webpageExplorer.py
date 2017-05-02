from selenium import webdriver
from selenium.webdriver.common.keys import Keys

with open('inputFile.txt', 'r') as inputfile:
	url = inputfile.readline().replace('\n', '')
	depth = inputfile.readline().replace('\n', '')
	browser = inputfile.readline().replace('\n', '')

driver = webdriver.Chrome()
driver.get(url)
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
